import sys


def print_help():
    pass


def parse_args() -> (str, str):
    # default
    shell = "bash"
    msystem = "ucrt64"

    args = sys.argv

    def shift_args():
        nonlocal args
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

        shift_args()

    return msystem.upper(), shell
