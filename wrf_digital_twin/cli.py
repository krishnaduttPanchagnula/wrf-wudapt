"""Command-line interface for the weather digital twin."""
import argparse
import json
import os
from pathlib import Path

from . import engine


def load(path):
    return json.loads(Path(path).read_text())


def build_parser():
    p = argparse.ArgumentParser(prog="wrf-twin", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("prepare", help="build a case from a request")
    q.add_argument("request")
    q.add_argument("--case", required=True)
    b = sub.add_parser("baseline", help="run WRF for a prepared case")
    b.add_argument("case")
    s = sub.add_parser("scenario", help="run a land-use proposal")
    s.add_argument("case")
    s.add_argument("proposal")
    s.add_argument("--out", required=True)
    c = sub.add_parser("compare", help="export comparison tables")
    c.add_argument("baseline")
    c.add_argument("scenario")
    c.add_argument("--out", required=True)
    r = sub.add_parser("run", help="prepare, baseline, scenario, compare")
    r.add_argument("request")
    r.add_argument("proposal")
    default_root = str(Path(os.environ.get(
        "WRF_TWIN_ROOT", Path(__file__).resolve().parents[1])) / "output")
    r.add_argument("--root", default=default_root)
    p_report = sub.add_parser("report", help="render comparison and validation reports")
    p_report.add_argument("results", help="a study's results directory")
    p_report.add_argument("--out", help="output directory (default: results)")
    y = sub.add_parser("compare-years", help="compare two completed studies' results")
    y.add_argument("first", help="first study's results directory")
    y.add_argument("second", help="second study's results directory")
    y.add_argument("--out", required=True)
    yr = sub.add_parser("run-years", help="run two requests and compare them")
    yr.add_argument("first_request")
    yr.add_argument("second_request")
    yr.add_argument("proposal")
    yr.add_argument("--root", default=default_root)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.cmd == "prepare":
        engine.prepare_case(engine.CaseRequest(**load(args.request)), Path(args.case))
    elif args.cmd == "baseline":
        engine.run_baseline(Path(args.case))
    elif args.cmd == "scenario":
        engine.apply_scenario(Path(args.case), load(args.proposal), Path(args.out))
    elif args.cmd == "compare":
        engine.compare_cases(Path(args.baseline), Path(args.scenario), Path(args.out))
    elif args.cmd == "run":
        req = engine.CaseRequest(**load(args.request))
        study = engine.run_study(req, load(args.proposal), Path(args.root))
        print(f"digital-twin run complete -> {study}")
    elif args.cmd == "report":
        print(engine.write_comparison_report(
            Path(args.results), Path(args.out) if args.out else None))
    elif args.cmd == "compare-years":
        engine.compare_years(Path(args.first), Path(args.second), Path(args.out))
    elif args.cmd == "run-years":
        first = engine.CaseRequest(**load(args.first_request))
        second = engine.CaseRequest(**load(args.second_request))
        proposal = load(args.proposal)
        root = Path(args.root)
        a = engine.run_study(first, proposal, root)
        b = engine.run_study(second, proposal, root)
        engine.compare_years(a / "results", b / "results", root / "years")
        print(f"two-year digital-twin run complete -> {root / 'years'}")


if __name__ == "__main__":
    main()
