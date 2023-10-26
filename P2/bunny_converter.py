import sys
import subprocess
import os

def mp4_to_mpg(input_file):
    output_path = f"BBB.mpg"
    cmd = f'ffmpeg -i {input_file} ./output_videos/{output_path}'
    subprocess.run(cmd, shell=True, check=True)

def ffmpeg_resize(input_file,resx,resy):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    output_path = f"{base_name}_{resx}_{resy}{ext}"

    cmd = f'ffmpeg -i {input_file} -vf scale={resx}:{resy} ./output_videos/{output_path}'
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Resize successful. Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bunny_converter.py function_name [parameters]")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "mp4_to_mpg":
        input_file = sys.argv[2]
        result = mp4_to_mpg(input_file)
    if function_name == "ffmpeg_resize":
        input_file = sys.argv[2]
        resx = sys.argv[3]
        resy = sys.argv[4]
        result = ffmpeg_resize(input_file,resx,resy)

    print("Result:",result)