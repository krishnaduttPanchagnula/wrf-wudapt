"""CLI for the digital-twin engine. Run inside the container, e.g.

./run.sh run 'python scripts/twin.py prepare request.json --case /work/output/twin_case'
./run.sh run 'python scripts/twin.py run request.json proposal.json'
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from digital_twin import CaseRequest, apply_scenario, compare_cases, prepare_case, run_baseline  # noqa: E402


def load(path: str):
    return json.loads(Path(path).read_text())


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("prepare")
    q.add_argument("request")
    q.add_argument("--case", required=True)
    b = sub.add_parser("baseline")
    b.add_argument("case")
    s = sub.add_parser("scenario")
    s.add_argument("case")
    s.add_argument("proposal")
    s.add_argument("--out", required=True)
    c = sub.add_parser("compare")
    c.add_argument("baseline")
    c.add_argument("scenario")
    c.add_argument("--out", required=True)
    r = sub.add_parser("run")
    r.add_argument("request")
    r.add_argument("proposal")
    r.add_argument("--root", default=str(ROOT / "output"))

    args = p.parse_args()
    if args.cmd == "prepare":
        prepare_case(CaseRequest(**load(args.request)), Path(args.case))
    elif args.cmd == "baseline":
        run_baseline(Path(args.case))
    elif args.cmd == "scenario":
        apply_scenario(Path(args.case), load(args.proposal), Path(args.out))
    elif args.cmd == "compare":
        compare_cases(Path(args.baseline), Path(args.scenario), Path(args.out))
    elif args.cmd == "run":
        req = CaseRequest(**load(args.request))
        name = f"twin_{req.lat:.4f}_{req.lon:.4f}_{req.start_dt:%Y%m%dT%H}"
        root = Path(args.root) / name
        base = prepare_case(req, root / "baseline")
        run_baseline(base)
        cf = apply_scenario(base, load(args.proposal), root / "scenario")
        compare_cases(base, cf, root / "results")
        print(f"digital-twin run complete -> {root}")


if __name__ == "__main__":
    main()
