"""Start kokoro-wyoming with the voice and speed from the app's Configuration tab."""
import json
import os

with open("/data/options.json", encoding="utf-8") as f:
    opts = json.load(f)

voice = str(opts.get("voice") or "af_heart")
speed = str(opts.get("speed", 1.0))
print(f"[kokoro_wyoming] starting: voice={voice} speed={speed} uri=tcp://0.0.0.0:10210", flush=True)

os.chdir("/app/src")  # model and voices files live here in the upstream image
args = [
    "/usr/local/bin/python3",
    "main.py",
    "--uri", "tcp://0.0.0.0:10210",
    "--voice", voice,
    "--speed", speed,
]
os.execv(args[0], args)
