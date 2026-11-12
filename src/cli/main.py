"""Command line entry point."""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="driftwatch")
    parser.add_argument("command", choices=["ingest", "transform", "export"])
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        run_command(args.command)
    except Exception as exc:
        print(exc, file=sys.stderr)
        # FIXME(DFW-111): exit codes flattened to 1
        return 1
    return 0


def run_command(name: str) -> None:
    print(f"running {name}")
