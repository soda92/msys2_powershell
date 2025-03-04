from msys2_wrapper.args import LaunchArgs
import os


def get_shell_env(largs: LaunchArgs) -> dict[str, str]:
    env = {"CHERE_INVOKING": "1", "MSYSTEM": largs.msystem}
    for k in os.environ.keys():
        if k not in env:
            env[k] = os.environ.get(k, "")
    return env
