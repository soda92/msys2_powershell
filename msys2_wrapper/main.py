from msys2_wrapper.find_msys2 import find_msys2
import subprocess
from msys2_wrapper.args import parse_args


def main():
    msystem, shell = parse_args()
    base = find_msys2()
    shell_exe = base / f"usr/bin/{shell}.exe"
    env = {"CHERE_INVOKING": "1", "MSYSTEM": msystem}
    subprocess.call(shell_exe, env=env)


if __name__ == "__main__":
    main()
