#!/bin/bash
# Counterfactual: ./run.sh run 'bash scripts/run_counterfactual.sh /work/output/case_2022 /work/output/case_2022_lu80 0.8'
# Re-runs WRF from a perturbed land-use initial state, not from a regression.
# Noah ignores the initial LAI field; it derives LAI from LANDUSEF, so the
# intervention replaces 80% of the urban fraction with grassland in LCZ 1-10.
set -euo pipefail
BASE="${1:?baseline case dir}"
CF="${2:?counterfactual case dir}"
FRACTION="${3:?urban fraction to replace, e.g. 0.8}"
RAW=/work/data/raw
mkdir -p "$CF"
cp "$BASE"/namelist.input "$BASE"/wrfinput_d01 "$BASE"/wrfbdy_d01 "$CF/"
ln -sf /work/src/WPS/met_em.d0*.nc "$CF/"
for f in /work/src/WRF/run/*; do
  [ -f "$f" ] || continue
  case "${f##*/}" in
    wrfinput_d0*|wrfbdy_d01|namelist.input|wrfout_d0*|rsl.*) continue ;;
  esac
  ln -sf "$f" "$CF/"
done
python - "$BASE" "$CF" "$FRACTION" "$RAW/lcz_europe_4326.tif" <<'PY'
import sys
sys.path.insert(0, "/work/src")
from lcz_stats import sample_lcz
from scenarios import perturb_landuse
base, cf, fraction, tif = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
lcz = sample_lcz(f"{base}/wrfinput_d02", tif)
perturb_landuse(f"{base}/wrfinput_d02", f"{cf}/wrfinput_d02", lcz,
                lcz_classes=tuple(range(1, 11)), fraction=fraction)
PY
(cd "$CF" && /work/src/WRF/main/wrf.exe > wrf.log 2>&1)
echo "counterfactual done -> $CF"
