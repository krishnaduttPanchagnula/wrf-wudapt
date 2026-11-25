FROM docker.io/library/ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

# Fortran + netCDF toolchain for WRF/WPS, Python scientific stack for the pipeline.
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential gfortran make m4 bison flex csh git curl ca-certificates \
      libnetcdf-dev libnetcdff-dev netcdf-bin \
      libhdf5-dev libcurl4-openssl-dev libpng-dev zlib1g-dev cmake \
      python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Ubuntu 24.04 dropped libjasper-dev; WPS needs jasper/jasper.h for GRIB2 decoding.
RUN curl -Ls https://github.com/jasper-software/jasper/archive/refs/tags/version-2.0.33.tar.gz \
      | tar -xz -C /tmp \
    && cmake -S /tmp/jasper-version-2.0.33 -B /tmp/jasper-build -DCMAKE_INSTALL_PREFIX=/usr \
    && cmake --build /tmp/jasper-build -j 4 \
    && cmake --install /tmp/jasper-build

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
RUN pip install --no-cache-dir \
      numpy==1.26.4 pandas xarray netCDF4 scipy scikit-learn pyproj h5netcdf \
      rasterio rioxarray geopandas matplotlib requests pyyaml w2w
# w2w 0.5.0 uses NumPy 1.x type aliases that were removed in NumPy 2.
RUN sed -i 's/np\.float_/np.float64/g; s/np\.int_/np.int64/g; s/np\.in1d/np.isin/g' \
      /opt/venv/lib/python3.12/site-packages/w2w/w2w.py
# rasterio.reproject now returns ndarray; w2w 0.5.0 expects an xarray object.
RUN python3 - <<'PY'
p = "/opt/venv/lib/python3.12/site-packages/w2w/w2w.py"
s = open(p).read()
s = s.replace("ucp_2_wrf = ucp_2_wrf.where(ucp_2_wrf > kwargs['FRC_THRESHOLD'], 0)",
              "ucp_2_wrf = np.where(ucp_2_wrf > kwargs['FRC_THRESHOLD'], ucp_2_wrf, 0)")
s = s.replace("ucp_2_wrf.values[0, np.isnan(ucp_2_wrf[0, :, :])] = 0",
              "ucp_2_wrf[0, np.isnan(ucp_2_wrf[0, :, :])] = 0")
s = s.replace("hgt_urb2d.values[0, np.isnan(hgt_urb2d[0, :, :])] = 0",
              "hgt_urb2d[0, np.isnan(hgt_urb2d[0, :, :])] = 0")
s = s.replace(")[0].values", ")[0]")
s = s.replace("ucp_res.values[:, frc_mask == 0] = 0", "ucp_res[:, frc_mask == 0] = 0")
open(p, "w").write(s)
PY

WORKDIR /work
CMD ["/bin/bash"]
