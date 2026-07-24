import os
import sys
import subprocess


def build_exe():
    script = os.path.join(os.getcwd(), "app.py")
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--name",
        "ResumeAI_Analyzer",
        "--noconsole",
        "--add-data",
        "assets;assets",
        "--add-data",
        "charts;charts",
        "--add-data",
        "utils;utils",
        script,
    ]
    print("Building desktop executable...")
    subprocess.run(cmd, check=True)
    print("Build completed. Check the dist folder.")


if __name__ == "__main__":
    build_exe()
