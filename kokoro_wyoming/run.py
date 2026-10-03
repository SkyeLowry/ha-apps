"""Start kokoro-wyoming with the voice and speed from the app's Configuration tab."""
import json
import os
import sys

with open("/data/options.json", encoding="utf-8") as f:
    opts = json.load(f)

voice = str(opts.get("voice") or "af_heart")
speed = str(opts.get("speed", 1.0))
print(f"[kokoro_wyoming] starting: voice={voice} speed={speed} uri=tcp://0.0.0.0:10210", flush=True)

os.chdir("/opt/kokoro-wyoming/src")  # model and voices files live here
args = [
    sys.executable,
    "main.py",
    "--uri", "tcp://0.0.0.0:10210",
    "--voice", voice,
    "--speed", speed,
]
os.execv(args[0], args)
