import sys
import subprocess
import os
sys.path.append('../P1')
from rgb_yuv import *

def mp4_to_mpg(input_file):
    output_path = f"BBB.mpg"
    cmd = f'ffmpeg -hide_banner -i {input_file} ./{output_path}'
    subprocess.run(cmd, shell=True, check=True)

def ffmpeg_resize(input_file,resx,resy):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    output_path = f"BBB_{resx}_{resy}{ext}"

    cmd = f'ffmpeg -hide_banner -i {input_file} -vf scale={resx}:{resy} ./{output_path}'
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Resize successful. Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def chroma_subsampling(input_file,subsampling_format):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    output_path = f"BBB_{subsampling_format}{ext}"
    cmd = f'ffmpeg -hide_banner -i {input_file} -vf format={subsampling_format} ./{output_path}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def video_info(input_file):
    cmd = f'ffprobe -hide_banner {input_file}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bunny_converter.py function_name [parameters]")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name in {"rgb_to_yuv", "yuv_to_rgb"} and len(sys.argv) != 5:
        if(function_name=="rgb_to_yuv"):
            print(f"Usage: python rgb_yuv.py {function_name} R G B")
        elif(function_name=="yuv_to_rgb"):
            print(f"Usage: python rgb_yuv.py {function_name} Y U V")
    elif function_name == "serpentine" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py serpentine 'image_path'")
    elif function_name == "color_to_bw" and len(sys.argv) != 4:
        print("Usage: python rgb_yuv.py color_to_bw 'image_path' 'crf'")
    elif function_name == "run_length_encoding" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py run_length_encoding 'input_string'")
    elif function_name in {"dct_encode", "dct_decode"} and len(sys.argv) != 3:
        print(f"Usage: python rgb_yuv.py {function_name} 'image_path'")
    elif function_name == "mp4_to_mpg" and len(sys.argv) != 3:
        print(f"Usage: python {function_name} 'input_file'")
    elif function_name == "ffmpeg_resize" and len(sys.argv) != 5:
        print(f"Usage: python {function_name} 'input_file' 'resx' 'resy'")
    elif function_name == "chroma_subsampling" and len(sys.argv) != 4:
        print(f"Usage: python {function_name} 'input_file' 'subsampling_format'")
    elif function_name == "video_info" and len(sys.argv) != 3:
        print(f"Usage: python {function_name} 'input_file'")
    else:
        try:
            if function_name == "rgb_to_yuv":
                r, g, b = map(float, sys.argv[2:5])
                result = rgb_to_yuv(r, g, b)
            elif function_name == "yuv_to_rgb":
                y, u, v = map(float, sys.argv[2:5])
                result = yuv_to_rgb(y, u, v)
            elif function_name == "serpentine":
                im_path = sys.argv[2]
                result = serpentine(im_path)
            elif function_name == "color_to_bw":
                im_path = sys.argv[2]
                crf = float(sys.argv[3])
                color_to_bw(im_path, crf)
            elif function_name == "run_length_encoding":
                input_string = sys.argv[2]
                result = run_length_encoding(input_string)
            elif function_name == "dct_encode":
                im_path = sys.argv[2]
                result = dct_encode(im_path)
            elif function_name == "dct_decode":
                encoded_data = sys.argv[2]
                result = dct_decode(encoded_data)
            elif function_name == "mp4_to_mpg":
                input_file = sys.argv[2]
                result = mp4_to_mpg(input_file)
            elif function_name == "ffmpeg_resize":
                input_file = sys.argv[2]
                resx = sys.argv[3]
                resy = sys.argv[4]
                result = ffmpeg_resize(input_file,resx,resy)
            elif function_name == "chroma_subsampling":
                input_file = sys.argv[2]
                subsampling_format = sys.argv[3]
                result = chroma_subsampling(input_file,subsampling_format)
            elif function_name == "video_info":
                input_file = sys.argv[2]
                result = video_info(input_file)
            else:
                print("Invalid function name. Use 'rgb_to_yuv', 'yuv_to_rgb', 'ffmpeg_resize', 'serpentine', 'color_to_bw', 'run_length_encoding', 'dct_encode', 'dct_decode', 'mp4_to_mpg', 'chroma_subsampling', 'video_info'.")
        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Result:", result)