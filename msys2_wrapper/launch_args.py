import os
import sys

from msys2_wrapper.find_msys2 import find_msys2


class LaunchArgs:
    def __init__(self):
        self.base = find_msys2()
        self.shell = "bash"
        self.msystem = "ucrt64"
        self.shell_args = ["-l"]
        self.working_directory = os.getcwd()
        self.msys2_path_type = ""

    def get_shell_exe(self):
        shell_exe = self.base / f"usr/bin/{self.shell}.exe"
        if not shell_exe.exists():
            print(f"shell `{self.shell}` not exist", file=sys.stderr)
            exit(-1)
        return str(shell_exe).replace("\\", "/")

    def get_shell_env(largs) -> dict[str, str]:
        env = {"CHERE_INVOKING": "1", "MSYSTEM": largs.msystem}
        if largs.msys2_path_type != "":
            env["MSYS2_PATH_TYPE"] = largs.msys2_path_type

        # insert default env
        for k in os.environ.keys():
            if k not in env:
                env[k] = os.environ.get(k, "")

        return env
