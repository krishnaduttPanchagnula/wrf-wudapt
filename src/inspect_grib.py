"""List variables in one GRIB2 file (diagnostic)."""
import sys

from eccodes import codes_get, codes_grib_new_from_file, codes_release

path = sys.argv[1]
seen = set()
with open(path, "rb") as f:
    while True:
        gid = codes_grib_new_from_file(f)
        if gid is None:
            break
        key = (codes_get(gid, "discipline"), codes_get(gid, "parameterCategory"),
               codes_get(gid, "parameterNumber"), codes_get(gid, "shortName"))
        seen.add(key)
        codes_release(gid)
for k in sorted(seen):
    if any(s in k[3].lower() for s in ("soil", "sm", "st", "tmp", "shtfl", "lhtfl")):
        print(k)
print(f"total distinct messages: {len(seen)}")
