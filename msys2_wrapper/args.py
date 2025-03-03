import sys
from msys2_wrapper.help import print_help
from msys2_wrapper.helper import remove_quote


def parse_args() -> (str, str):
    # default
    shell = "bash"
    msystem = "ucrt64"

    args = sys.argv

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
            shell = remove_quote(args[1])
            shift_args(2)  # two times
            continue

        shift_args()

    return msystem.upper(), shell
