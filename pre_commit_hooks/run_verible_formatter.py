import argparse
import subprocess
import shlex
import os
import pathlib

def cmd(cmd, stdout=None, stderr=None, setenv={}):
        env = dict(os.environ)
        for key, value in setenv.items():
            env[key] = value 
        output = subprocess.run(shlex.split(cmd), stdout=stdout, text=True, env=env)

        if stdout == subprocess.PIPE:
            return f"{output.stdout.strip()}"
        else:
            return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    files = args.filenames
    for file in files:
        # print(f"{pathlib.Path().cwd()/file}")
        cmd(f"verible-verilog-format --inplace {file}")

if __name__ == "__main__":
    main()