"""Fast, WRF-free checks for the installable engine."""
import tempfile
import unittest
from pathlib import Path

from wrf_digital_twin.engine import CaseRequest, build_namelists


class TestRequest(unittest.TestCase):
    def test_grid_centred_and_sized(self):
        self.assertEqual(CaseRequest(45.5, 9.1, 25, "2022-07-25T00:00:00Z", 6).grid_n, 31)
        self.assertEqual(CaseRequest(45.5, 9.1, 100, "2022-07-25T00:00:00Z", 6).grid_n, 73)

    def test_gfs_window_must_be_6_hourly(self):
        for hours in (1, 5, 7):
            with self.assertRaises(ValueError):
                CaseRequest(45.5, 9.1, 25, "2022-07-25T00:00:00Z", hours)

    def test_namelists_follow_request(self):
        req = CaseRequest(45.4937, 9.16646, 25, "2022-07-25T00:00:00Z", 6)
        with tempfile.TemporaryDirectory() as tmp:
            case = Path(tmp)
            build_namelists(req, case)
            wps = (case / "namelist.wps").read_text()
            wrf = (case / "namelist.input").read_text()
            self.assertIn("ref_lat = 45.493700", wps)
            self.assertIn("ref_lon = 9.166460", wps)
            self.assertIn("e_we = 31, 31,", wps)
            self.assertIn("end_date   = '2022-07-25_06:00:00'", wps)
            self.assertIn("start_day = 25, 25,", wrf)
            self.assertIn("end_hour = 6, 6,", wrf)
            self.assertIn("i_parent_start = 1, 11,", wrf)


if __name__ == "__main__":
    unittest.main()
