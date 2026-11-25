#!/bin/bash
# GFS f000 (forecast hour 0) includes soil fields; .anl files do not.
set -euo pipefail
RAW=/work/data/raw
for d in 20220724 20220725 20220726 20220727; do
  for h in 00 06 12 18; do
    echo "$d $h"
  done
done | xargs -P 4 -n 2 bash -c '
  d="$0"; h="$1"; f="/work/data/raw/gfs.t${h}z.pgrb2.0p25.f000.${d}"
  if [ -s "$f" ]; then exit 0; fi
  url="https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.${d}/${h}/atmos/gfs.t${h}z.pgrb2.0p25.f000"
  curl -sL --retry 3 --max-time 900 "$url" -o "$f"
  echo "$f $(stat -c%s "$f")"
'
