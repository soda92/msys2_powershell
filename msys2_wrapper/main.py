from msys2_wrapper.args import parse_args
from msys2_wrapper.start_shell import start_shell
from msys2_wrapper.shell_env import get_shell_env


def main():
    largs = parse_args()
    shell_exe = largs.get_shell_exe()
    args2 = [shell_exe, *largs.shell_args]
    # print(" ".join(args2))

    env = get_shell_env(largs)
    start_shell(args2, largs, env)


if __name__ == "__main__":
    main()
