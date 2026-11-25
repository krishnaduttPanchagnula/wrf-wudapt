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
    r.add_argument("--root", default=str(Path(os.environ.get(
        "WRF_TWIN_ROOT", Path(__file__).resolve().parents[1])) / "output"))
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
        name = f"twin_{req.lat:.4f}_{req.lon:.4f}_{req.start_dt:%Y%m%dT%H}"
        root = Path(args.root) / name
        base = engine.prepare_case(req, root / "baseline")
        engine.run_baseline(base)
        cf = engine.apply_scenario(base, load(args.proposal), root / "scenario")
        engine.compare_cases(base, cf, root / "results")
        print(f"digital-twin run complete -> {root}")


if __name__ == "__main__":
    main()
