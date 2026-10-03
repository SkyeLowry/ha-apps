# Changelog

## 1.1.0-3 (2026-10-03)

- Fix: build failed on Home Assistant OS (`failed to fetch remote ...kokoro-wyoming.git`). Docker's git-URL `ADD` needs git on the host, which HA OS doesn't ship. The source is now downloaded as GitHub's archive of the pinned commit, and the build fails if the archive's commit ID doesn't match.

## 1.1.0-2 (2026-10-03)

- Fix: the app failed to start (`exec: /usr/local/bin/python3: no such file or directory`). Every image upstream publishes on Docker Hub, including `1.1.0` and `latest`, is the 2.4 GB CUDA build, whose Python lives at `/usr/bin/python3`.
- Now built on the host from upstream source (tag v1.1.0) on `python:3.13-slim` with CPU `onnxruntime`; model and voices are downloaded with checksums. Much smaller image, no CUDA libraries.
- Dependencies pinned in `requirements.txt` to the versions tested (describe, synthesize, streaming).

## 1.1.0-1 (2026-10-02)

- First release. Wraps nordwestt/kokoro-wyoming 1.1.0 (2026-09-12, Wyoming streaming synthesis).
- Options: default voice, speed.
