"""Fetch the upstream kokoro-wyoming source at a pinned commit (build time).

Docker's git-URL ADD needs git on the host's Docker daemon, which Home Assistant
OS doesn't have, so download GitHub's archive of the commit over HTTPS instead.
GitHub writes the commit ID into the archive's pax header; it's checked against
the pin so the build fails rather than running other code.
"""
import io
import sys
import tarfile
import urllib.request

REPO = "nordwestt/kokoro-wyoming"
COMMIT = "cc3ec38609e611abf5d21fbf48917db4d69d7217"  # tag v1.1.0
DEST = "/opt/kokoro-wyoming"

url = f"https://github.com/{REPO}/archive/{COMMIT}.tar.gz"
print(f"fetching {url}", flush=True)
with urllib.request.urlopen(url, timeout=120) as resp:
    data = resp.read()

with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
    found = tar.pax_headers.get("comment", "")
    if found != COMMIT:
        sys.exit(f"archive commit mismatch: expected {COMMIT}, got {found!r}")
    prefix = tar.getnames()[0].split("/")[0] + "/"
    members = []
    for m in tar.getmembers():
        if not m.name.startswith(prefix) or m.name == prefix.rstrip("/"):
            continue
        m.name = m.name[len(prefix):]
        members.append(m)
    tar.extractall(DEST, members=members, filter="data")

print(f"extracted {len(members)} entries at commit {COMMIT} to {DEST}", flush=True)
