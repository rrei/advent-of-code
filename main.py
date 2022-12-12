import argparse
import importlib
import sys

parser = argparse.ArgumentParser(description="Run advent of code programs")
parser.add_argument(
    "-y",
    "--years",
    dest="years",
    default="2022",
    metavar="YEARS",
    help="Specify one or more (comma-separated) years to run.",
)
parser.add_argument(
    "-d",
    "--days",
    dest="days",
    default=",".join(str(d) for d in range(1, 26)),
    metavar="DAYS",
    help="Specify one or more (comma-separated) days to run.",
)
parser.add_argument(
    "-p",
    "--parts",
    dest="parts",
    default="1,2",
    metavar="PARTS",
    help="Specify one or more (comma-separated) parts to run.",
)

args = parser.parse_args()
for y in args.years.split(","):
    for d in args.days.split(","):
        modname = f"aoc{y.strip()}.day{d.strip()}"
        try:
            mod = importlib.import_module(modname)
        except ImportError:
            print(f"ERROR: unable to import {modname}")
            continue
        print(f"Running {modname}...")
        for p in args.parts.split(","):
            funcname = f"part{p.strip()}"
            print(f"\t{funcname}...", end=" ")
            try:
                print(getattr(mod, funcname)())
            except BaseException as error:
                print(f"{type(error).__name__}: {error}")
            sys.stdout.flush()
