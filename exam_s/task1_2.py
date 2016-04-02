import argparse
import shutil
import os
import subprocess

parser = argparse.ArgumentParser(description="Litlle size")

parser.add_argument('path', type=str,
                    help='file_name')
parser.add_argument('command', type=str,
                    help="size")
parser.add_argument('path_out', type=str, nargs="?", help="out_name")


args = parser.parse_args()
command = args.command
path = args.path
path_out = args.path_out
size = '-resize ' + command + '%'
# if os.path.isfile(path):
if path_out is None:
    run = "convert " + path + size
    subprocess.run(run.join(" "), shell=True)
else:
    run = "convert " + path + size + path_out
    subprocess.run(run.join(" "), shell=True)
# elif os.path.isdir(path):
#    for i in path:
#       if os.path.isfile(path):
#         if path_out==None:
#             run = "convert " + path + size
#             subprocess.run(run.join(" "), shell=True)
#             print("done")
#         else:
#             run = "convert " + path + size + path_out
#             subprocess.run(run.join(" "), shell = True)
