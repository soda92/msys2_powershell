import sys
from pathlib import Path


def print_help():
    print(
        (
            """Usage:
    %~1 [options] [login shell parameters]

Options:
    -mingw32 ^| -mingw64 ^| -ucrt64 ^| -clang64 ^|
    -msys[2] ^| -clangarm64           Set shell type
    -defterm ^| -mintty ^| -conemu     Set terminal type
    -here                            Use current directory as working
                                     directory
    -where DIRECTORY                 Use specified DIRECTORY as working
                                     directory
    -[use-]full-path                 Use full current PATH variable
                                     instead of trimming to minimal
    -no-start                        Do not use "start" command and
                                     return login shell resulting 
                                     errorcode as this batch file 
                                     resulting errorcode
    -shell SHELL                     Set login shell
    -help ^| --help ^| -? ^| /?         Display this help and exit

Any parameter that cannot be treated as valid option and all
following parameters are passed as login shell command parameters."""
        ).replace("%~1", Path(sys.argv[0]).name)
    )


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
