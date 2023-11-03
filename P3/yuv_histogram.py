import subprocess
import os

def yuv_histogram(input_file):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    cmd = f'ffmpeg -hide_banner -i {input_file} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" {base_name}_histogram{ext}'
    subprocess.run(cmd, shell=True, check=True)