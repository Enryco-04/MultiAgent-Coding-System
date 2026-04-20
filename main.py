"""
main.py
-------
CLI mode selector for the project.

Modes:
  python main.py normal [problem_id ...]
  python main.py future [args ...]

Backward-compatible usage:
  python main.py
  python main.py sliding_window_max
"""

import sys

from orchestrator.loop import run_future_mode, run_normal_mode


DEFAULT_MODE = "normal"
FUTURE_MODE = "future"
VALID_MODES = {DEFAULT_MODE, FUTURE_MODE}


def _split_mode_and_args(argv: list[str]) -> tuple[str, list[str]]:
    if not argv:
        return DEFAULT_MODE, []

    first_arg = argv[0].lower()
    if first_arg in VALID_MODES:
        return first_arg, argv[1:]

    # Preserve the old CLI: `python main.py <problem_id ...>`
    return DEFAULT_MODE, argv


def main(argv: list[str] | None = None):
    mode, mode_args = _split_mode_and_args(argv or sys.argv[1:])

    if mode == DEFAULT_MODE:
        return run_normal_mode(mode_args)

    if mode == FUTURE_MODE:
        return run_future_mode(mode_args)

    raise ValueError(f"Unsupported mode: {mode}")


if __name__ == "__main__":
    main()
