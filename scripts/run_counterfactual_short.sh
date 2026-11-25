#!/bin/bash
# Short counterfactual from the baseline initial state; 1-hour run for a quick
# end-to-end demonstration of the causal (perturb-WRF) approach.
set -euo pipefail
BASE=/work/output/case_2022
CF=/work/output/case_2022_lai20
mkdir -p "$CF"
cp "$BASE"/namelist.input "$BASE"/wrfinput_d01 "$BASE"/wrfinput_d02 "$BASE"/wrfbdy_d01 "$CF/"
sed -i -E 's/end_hour = [0-9]+, [0-9]+/end_hour = 1, 1/' "$CF/namelist.input"
python - "$BASE" "$CF" <<'PY'
import sys
sys.path.insert(0, "/work/src")
from scenarios import perturb_lai
base, cf = sys.argv[1:3]
# LCZ field is absent in this build's wrfinput; perturb all cells uniformly.
# Upgrade to per-LCZ perturbation when the 41-category WRF build is available.
perturb_lai(f"{base}/wrfinput_d02", f"{cf}/wrfinput_d02", 1.2)
PY
# WRF reads radiation/land-surface tables from the working directory.
for f in /work/src/WRF/run/*; do
  b=$(basename "$f")
  case "$b" in wrfout_d0*|wrfinput_d0*|wrfbdy_d0*|namelist.input) continue;; esac
  [ -e "$CF/$b" ] || ln -sf "$f" "$CF/$b"
done
(cd "$CF" && /work/src/WRF/main/wrf.exe > wrf.log 2>&1)
echo "counterfactual complete -> $CF"
