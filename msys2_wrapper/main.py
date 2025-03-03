from msys2_wrapper.find_msys2 import find_msys2
import subprocess
from msys2_wrapper.args import parse_args
import sys


def main():
    msystem, shell, args = parse_args()
    base = find_msys2()
    shell_exe = base / f"usr/bin/{shell}.exe"
    if not shell_exe.exists():
        print(f"shell `{shell}` not exist", file=sys.stderr)
        exit(-1)
    env = {"CHERE_INVOKING": "1", "MSYSTEM": msystem}

    args2 = [shell_exe, *args]
    subprocess.call(args2, env=env)


if __name__ == "__main__":
    main()
