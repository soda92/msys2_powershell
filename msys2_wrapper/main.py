from msys2_wrapper.find_msys2 import find_msys2
from msys2_wrapper.args import parse_args
from msys2_wrapper.start_shell import start_shell
from msys2_wrapper.shell_env import get_shell_env
import sys


def main():
    largs = parse_args()
    base = find_msys2()

    shell_exe = base / f"usr/bin/{largs.shell}.exe"
    if not shell_exe.exists():
        print(f"shell `{largs.shell}` not exist", file=sys.stderr)
        exit(-1)

    args2 = [str(shell_exe).replace("\\", "/"), *largs.shell_args]
    # print(" ".join(args2))

    env = get_shell_env()

    start_shell(args2, largs, env)


if __name__ == "__main__":
    main()
