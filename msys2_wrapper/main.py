from msys2_wrapper.find_msys2 import find_msys2
import subprocess
from msys2_wrapper.args import parse_args
import sys
import os
import contextlib


@contextlib.contextmanager
def CD(d):
    cwd = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(cwd)


def main():
    largs = parse_args()
    base = find_msys2()
    shell_exe = base / f"usr/bin/{largs.shell}.exe"
    if not shell_exe.exists():
        print(f"shell `{largs.shell}` not exist", file=sys.stderr)
        exit(-1)
    env = {"CHERE_INVOKING": "1", "MSYSTEM": largs.msystem}
    for k in os.environ.keys():
        if k not in env:
            env[k] = os.environ.get(k, "")

    args2 = [str(shell_exe).replace("\\", "/"), *largs.shell_args]
    # print(" ".join(args2))
    try:
        with CD(largs.working_directory):
            subprocess.call(args2, env=env)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
