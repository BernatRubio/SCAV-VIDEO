import subprocess
import os

def print_subtitles(input_file, subtitles_url):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    cmd_url = f'wget {subtitles_url}'
    subprocess.run(cmd_url, shell=True, check=True)

    cmd_subtitles_name = f'ls | grep -m 1 .srt'
    filename = subprocess.run(cmd_subtitles_name, shell=True, capture_output=True, text=True)
    subtitles = filename.stdout.strip()
    cmd_burn_subtitles = (
        f'ffmpeg -hide_banner -i {input_file} -vf subtitles={subtitles} ./subtitles_burned{ext}'
    )
    subprocess.run(cmd_burn_subtitles, shell=True, check=True)
