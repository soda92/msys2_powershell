from msys2_wrapper.args import LaunchArgs
import subprocess
import os
import contextlib


@contextlib.contextmanager
def CD(d):
    cwd = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(cwd)


def start_shell(largs: LaunchArgs, env: dict[str, str]):
    shell_exe = largs.get_shell_exe()
    shell_args = [shell_exe, *largs.shell_args]
    # print(" ".join(shell_args))
    try:
        with CD(largs.working_directory):
            subprocess.call(shell_args, env=env)
    except KeyboardInterrupt:
        exit()
