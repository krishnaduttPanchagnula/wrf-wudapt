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
from digital_twin import (CaseRequest, apply_scenario, compare_cases, compare_years,  # noqa: E402
                          prepare_case, run_baseline, run_study,
                          write_comparison_report)


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
    rep = sub.add_parser("report", help="render comparison and validation reports")
    rep.add_argument("results", help="a study's results directory")
    rep.add_argument("--out", help="output directory (default: results)")
    y = sub.add_parser("compare-years")
    y.add_argument("first", help="first study's results directory")
    y.add_argument("second", help="second study's results directory")
    y.add_argument("--out", required=True)
    yr = sub.add_parser("run-years")
    yr.add_argument("first_request")
    yr.add_argument("second_request")
    yr.add_argument("proposal")
    yr.add_argument("--root", default=str(ROOT / "output"))

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
        study = run_study(CaseRequest(**load(args.request)), load(args.proposal),
                          Path(args.root))
        print(f"digital-twin run complete -> {study}")
    elif args.cmd == "report":
        print(write_comparison_report(
            Path(args.results), Path(args.out) if args.out else None))
    elif args.cmd == "compare-years":
        compare_years(Path(args.first), Path(args.second), Path(args.out))
    elif args.cmd == "run-years":
        first = CaseRequest(**load(args.first_request))
        second = CaseRequest(**load(args.second_request))
        proposal = load(args.proposal)
        root = Path(args.root)
        a = run_study(first, proposal, root)
        b = run_study(second, proposal, root)
        compare_years(a / "results", b / "results", root / "years")
        print(f"two-year digital-twin run complete -> {root / 'years'}")


if __name__ == "__main__":
    main()
