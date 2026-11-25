#!/bin/bash
# Counterfactual: +20% initial soil moisture; 1-hour WRF re-run.
set -euo pipefail
BASE=/work/output/case_2022
CF=/work/output/case_2022_soil20
rm -rf "$CF"; mkdir -p "$CF"
cp "$BASE"/namelist.input "$BASE"/wrfinput_d01 "$BASE"/wrfinput_d02 "$BASE"/wrfbdy_d01 "$CF/"
sed -i -E 's/end_hour = [0-9]+, [0-9]+/end_hour = 1, 1/' "$CF/namelist.input"
python - <<'PY'
import sys
sys.path.insert(0, "/work/src")
from scenarios import perturb_soil
perturb_soil("/work/output/case_2022/wrfinput_d02", "/work/output/case_2022_soil20/wrfinput_d02", 1.2)
PY
for f in /work/src/WRF/run/*; do
  b=$(basename "$f")
  case "$b" in wrfout_d0*|wrfinput_d0*|wrfbdy_d0*|namelist.input) continue;; esac
  [ -e "$CF/$b" ] || ln -sf "$f" "$CF/$b"
done
(cd "$CF" && /work/src/WRF/main/wrf.exe > wrf.log 2>&1)
echo "soil counterfactual complete -> $CF"
