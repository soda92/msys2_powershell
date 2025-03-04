from msys2_wrapper.args import parse_args
from msys2_wrapper.start_shell import start_shell
from msys2_wrapper.shell_env import get_shell_env


def main():
    largs = parse_args()
    env = get_shell_env(largs)
    start_shell(largs, env)


if __name__ == "__main__":
    main()
