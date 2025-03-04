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


def start_shell(shell_args, largs: LaunchArgs, env: dict[str, str]):
    try:
        with CD(largs.working_directory):
            subprocess.call(shell_args, env=env)
    except KeyboardInterrupt:
        exit()
