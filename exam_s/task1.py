import argparse
import shutil
import os
import subprocess

parser = argparse.ArgumentParser(description="Litlle size")

parser.add_argument('path', type=str,
                    help='file_name')
parser.add_argument('command', type=str,
                    help="size")
parser.add_argument('path_out', type=str, help="out_name")


args = parser.parse_args()
command = args.command
path = args.path
path_out = args.path_out
size = '-resize ' + command + '%'
run = "convert " + path + size + path_out
# subprocess.run(["convert",path, size.join(" "), path_out], shell=True)
subprocess.run(run.join(" "), shell=True)
