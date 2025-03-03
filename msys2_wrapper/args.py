import sys
from msys2_wrapper.help import print_help
from msys2_wrapper.helper import remove_quote
import os


class LaunchArgs:
    def __init__(self):
        self.shell = "bash"
        self.msystem = "ucrt64"
        self.shell_args = ["-l"]
        self.working_directory = os.getcwd()


def parse_args() -> LaunchArgs:
    largs = LaunchArgs()

    args = sys.argv[1:]

    def shift_args(times=1):
        nonlocal args
        for _ in range(times):
            args = args[1:]

    while len(args) > 0:
        arg = args[0]
        if arg in ("-help", "--help", "-?", "/?"):
            print_help()
            exit()

        if arg in ("-msys", "-msys2"):
            msystem = "msys"
            shift_args()
            continue
        if arg in ("-mingw32", "-mingw64", "-clang64", "-ucrt64", "-clangarm64"):
            msystem = arg[1:]
            shift_args()
            continue
        if arg == "-mingw":
            msystem = "mingw64"
            shift_args()
            continue
        if arg == "-shell":
            if len(args) == 1:
                print("Shell not specified for -shell parameter.", file=sys.stderr)
                exit(2)
            largs.shell = remove_quote(args[1])
            shift_args(2)  # two times
            continue

        if arg == "-where":
            if len(args) == 1:
                print(
                    "Working directory is not specified for -where parameter.",
                    file=sys.stderr,
                )
                exit(2)
            largs.working_directory = remove_quote(args[1])
            shift_args(2)
            continue

        break

    largs.msystem = msystem.upper()
    largs.shell_args.extend(args)
    return largs
