"""Compatibility shim: canonical engine lives in `wrf_digital_twin.engine`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wrf_digital_twin.engine import *  # noqa: F401,F403
