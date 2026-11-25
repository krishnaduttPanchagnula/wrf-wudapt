#!/bin/bash
# End-to-end case runner inside the container: ./run.sh run 'bash scripts/run_case.sh'
# Steps mirror WPS/WRF docs; each stage's log is kept in the case directory.
set -euo pipefail
ROOT=/work
CASE="${1:-$ROOT/output/case_2022}"
# Dates are parameters: run two cases with different CASE_START/CASE_END, then compare.
CASE_START="${CASE_START:-2022-07-25}"
CASE_END="${CASE_END:-2022-07-25}"
CASE_END_HOUR="${CASE_END_HOUR:-18}"
RAW="$ROOT/data/raw"
WPS="$ROOT/src/WPS"
WRF="$ROOT/src/WRF"
GEOG="$RAW/geog"
GEOG_DATA="$GEOG/WPS_GEOG_LOW_RES"
mkdir -p "$CASE"

echo "[1/6] geography"
if [ ! -d "$GEOG_DATA" ]; then
  mkdir -p "$GEOG"
  tar -xzf "$RAW/geog_low_res_mandatory.tar.gz" -C "$GEOG"
fi
if [ ! -d "$GEOG_DATA/CGLC_MODIS_LCZ_global" ]; then
  tar -xzf "$RAW/cglc_modis_lcz_global.tar.gz" -C "$GEOG_DATA"
fi
sed -e "s|PATH_TO_WPS_GEOG|$GEOG_DATA|" \
    -e "s|2022-07-25_00:00:00|${CASE_START}_00:00:00|g" \
    -e "s|2022-07-25_18:00:00|${CASE_END}_${CASE_END_HOUR:-00}:00:00|g" \
    "$ROOT/config/namelist.wps" > "$CASE/namelist.wps"
ln -sf "$CASE/namelist.wps" "$WPS/namelist.wps"
VTABLE="$WPS/ungrib/Variable_Tables/Vtable.GFS"
[ -f "$RAW/Vtable.GFS" ] && VTABLE="$RAW/Vtable.GFS"   # updated table includes soil levels
cp -f "$VTABLE" "$WPS/Vtable"
if [ ! -f "$CASE/geo_em.d02.nc" ]; then
  (cd "$WPS" && ./geogrid.exe > "$CASE/geogrid.log" 2>&1)
  cp "$WPS"/geo_em.d0*.nc "$CASE/"
else
  echo "  skip geogrid (already generated)"
fi

echo "[2/6] inject LCZ urban parameters with w2w"
mkdir -p "$CASE/w2w"
cp "$CASE"/geo_em.d0*.nc "$CASE/w2w/"
LCZ_TIF="$RAW/lcz_milan_oa96.tif"
LCZ_BAND=1   # LCZ Generator band 2 = filtered map (0-indexed 1)
if [ -f "$RAW/lcz_europe_4326.tif" ]; then
  LCZ_TIF="$RAW/lcz_europe_4326.tif"
  LCZ_BAND=0   # European single-band map, reprojected to EPSG:4326
elif [ -f "$RAW/lcz_europe.tif" ]; then
  LCZ_TIF="$RAW/lcz_europe.tif"
  LCZ_BAND=0
fi
cp "$LCZ_TIF" "$CASE/w2w/lcz.tif"
if [ ! -f "$CASE/w2w/geo_em.d02_LCZ_params.nc" ]; then
  (cd "$CASE/w2w" && w2w . lcz.tif geo_em.d02.nc -l "$LCZ_BAND" \
      --lcz-ucp "$RAW/LCZ_UCP_lookup.csv" > "$CASE/w2w.log" 2>&1)
else
  echo "  skip w2w (already generated)"
fi
# Use the w2w-adjusted files for metgrid (rename as documented by w2w).
for f in "$CASE/w2w/geo_em.d01_41.nc" "$CASE/w2w/geo_em.d02_LCZ_params.nc"; do
  [ -f "$f" ] || { echo "missing $f"; cat "$CASE/w2w.log"; exit 1; }
done
cp "$CASE/geo_em.d01.nc" "$WPS/geo_em.d01.nc"
cp "$CASE/w2w/geo_em.d02_LCZ_extent.nc" "$WPS/geo_em.d02.nc"

echo "[3/6] ungrib + metgrid"
i=0
d="$CASE_START"
while :; do
  dnum="${d//-/}"
  for h in 00 06 12 18; do
    letter=$(printf "\\$(printf '%03o' $((65+i)))")
    ln -sf "$RAW/gfs.t${h}z.pgrb2.0p25.f000.$dnum" "$WPS/GRIBFILE.AA${letter}"
    i=$((i+1))
  done
  [ "$d" = "$CASE_END" ] && break
  d=$(date -d "$d + 1 day" +%F)
done
rm -f "$WPS"/FILE:*  # stale intermediate files from earlier attempts
S1_Y=$((10#${CASE_START:0:4})); S1_M=$((10#${CASE_START:5:2})); S1_D=$((10#${CASE_START:8:2}))
E1_Y=$((10#${CASE_END:0:4}));   E1_M=$((10#${CASE_END:5:2}));   E1_D=$((10#${CASE_END:8:2}))
if [ ! -f "$WPS/met_em.d01.${CASE_START}_00:00:00.nc" ]; then
  (cd "$WPS" && ./ungrib.exe > "$CASE/ungrib.log" 2>&1)
  (cd "$WPS" && ./metgrid.exe > "$CASE/metgrid.log" 2>&1)
else
  echo "  skip ungrib/metgrid (already generated)"
fi
cp "$WPS"/met_em.d0*.nc "$CASE/"

echo "[4/6] real.exe"
LEVELS=$(python - <<PY
import glob, netCDF4
f = sorted(glob.glob('$WPS/met_em.d01.*.nc'))[0]
with netCDF4.Dataset(f) as ds:
    print(ds.dimensions['num_metgrid_levels'].size)
PY
)
E1_H=$((10#${CASE_END_HOUR:-0}))
sed -E \
    -e "s/num_metgrid_levels = 34/num_metgrid_levels = $LEVELS/" \
    -e "s/start_year = [0-9]+, [0-9]+/start_year = $S1_Y, $S1_Y/" \
    -e "s/start_month = [0-9]+, [0-9]+/start_month = $S1_M, $S1_M/" \
    -e "s/start_day = [0-9]+, [0-9]+/start_day = $S1_D, $S1_D/" \
    -e "s/end_year = [0-9]+, [0-9]+/end_year = $E1_Y, $E1_Y/" \
    -e "s/end_month = [0-9]+, [0-9]+/end_month = $E1_M, $E1_M/" \
    -e "s/end_day = [0-9]+, [0-9]+/end_day = $E1_D, $E1_D/" \
    -e "s/end_hour = [0-9]+, [0-9]+/end_hour = $E1_H, $E1_H/" \
    "$ROOT/config/namelist.input" > "$CASE/namelist.input"
ln -sf "$CASE/namelist.input" "$WRF/run/namelist.input"
ln -sf "$WPS"/met_em.d0*.nc "$WRF/run/"
(cd "$WRF/run" && ./real.exe > "$CASE/real.log" 2>&1)
cp "$WRF/run"/wrfinput_d0* "$WRF/run"/wrfbdy_d01 "$CASE/"

echo "[5/6] wrf.exe"
(cd "$WRF/run" && ./wrf.exe > "$CASE/wrf.log" 2>&1)
cp "$WRF/run"/wrfout_d0* "$CASE/"

echo "[6/6] done -> $CASE"
