#!/bin/bash
# Compile WPS (GNU serial, GRIB2 enabled) inside the container.
set -euo pipefail
cd /work/src/WPS
printf '1\n' | env NETCDF=/usr JASPERLIB=/usr/lib JASPERINC=/usr/include ./configure \
  > /work/output/wps_configure.log 2>&1
# Ubuntu puts libnetcdff in the multiarch dir; WPS's generated config misses it.
sed -i 's|-L$(NETCDF)/lib  -lnetcdf|-L$(NETCDF)/lib -L/usr/lib/x86_64-linux-gnu -lnetcdff -lnetcdf -lcurl -lz|' configure.wps
env NETCDF=/usr JASPERLIB=/usr/lib JASPERINC=/usr/include ./compile \
  > /work/output/wps_compile.log 2>&1
tail -5 /work/output/wps_compile.log
