import sys
import subprocess
import os
import numpy as np
from collections import OrderedDict
from dct_processor import DCTProcessor


def rgb_to_yuv(r, g, b):
    Y = 0.299 * r + 0.587 * g + 0.114 * b
    U = -0.147 * r - 0.289 * g + 0.436 * b
    V = 0.615 * r - 0.515 * g - 0.100 * b
    return [Y, U, V]


def yuv_to_rgb(y, u, v):
    R = y + 1.140 * v
    G = y - 0.395 * u - 0.581 * v
    B = y + 2.032 * u
    return [R, G, B]


def ffmpeg_resize(path_to_im):
    base_name, ext = os.path.splitext(os.path.basename(path_to_im))

    output_path = f"{base_name}_filtered{ext}"

    cmd = f'ffmpeg -i "{path_to_im}" -vf "scale=360:-1" "./output_images/{output_path}"'
    subprocess.run(cmd, shell=True)

def serpentine(image_path):
    zigzag_order = [
        (0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), (0, 3), (1, 2),
        (2, 1), (3, 0), (4, 0), (3, 1), (2, 2), (1, 3), (0, 4), (0, 5),
    ]

    zigzag_data = []

    try:
        with open(image_path, "rb") as image_file:
            byte = image_file.read(1)
            while byte:
                zigzag_data.append(byte)
                # Read the next byte using the zigzag pattern
                for x, y in zigzag_order:
                    byte = image_file.read(1)
                    if not byte:
                        break
                    zigzag_data.append(byte)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return zigzag_data

def color_to_bw(image_path):
    base_name, ext = os.path.splitext(os.path.basename(image_path))

    output_path = f"{base_name}_bw{ext}"

    cmd = f'ffmpeg -i "{image_path}" -vf "format=gray" "./output_images/{output_path}"'
    subprocess.run(cmd, shell=True)

def run_length_encoding(input):

    """
    Parameters:
    
    input: string to encode
    """
    dict=OrderedDict.fromkeys(input, 0)

    for ch in input:
        dict[ch] += 1
    
    output = ''
    for key,value in dict.items():
        output = output + key + str(value)
    return output

def dct_encode(image_path):
    dct_processor = DCTProcessor()
    return dct_processor.dct_encode(image_path)

def dct_decode(encoded_data):
    dct_processor = DCTProcessor()
    return dct_processor.dct_decode(encoded_data)


if __name__ == "__main__":
    function_name = sys.argv[1]

    if ((function_name == "rgb_to_yuv" or function_name == "yuv_to_rgb") and len(sys.argv) != 5):
        print("Usage: python rgb_yuv.py function_name R|Y G|U B|V")
        sys.exit(1)
    elif function_name == "ffmpeg_resize" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py ffmpeg_resize 'path_to_im'")

    if function_name == "rgb_to_yuv" or function_name == "yuv_to_rgb":
        r = float(sys.argv[2])
        g = float(sys.argv[3])
        b = float(sys.argv[4])
    elif function_name == "ffmpeg_resize" or function_name == "serpentine" or function_name == "color_to_bw" or function_name == "run_length_encoding" or "dct_encode" or "dct_decode":
        im_path = sys.argv[2]
        array_of_bytes = sys.argv[2]

    if function_name == "rgb_to_yuv":
        result = rgb_to_yuv(r, g, b)
    elif function_name == "yuv_to_rgb":
        result = yuv_to_rgb(r, g, b)
    elif function_name == "ffmpeg_resize":
        result = ffmpeg_resize(im_path)
    elif function_name == "serpentine":
        result = serpentine(im_path)
    elif function_name == "color_to_bw":
        result = color_to_bw(im_path)
    elif function_name == "run_length_encoding":
        result = run_length_encoding(array_of_bytes)
    elif function_name == "dct_encode":
        result = dct_encode(im_path)
    elif function_name == "dct_decode":
        result = dct_decode(array_of_bytes)
    else:
        print("Invalid function name. Use 'rgb_to_yuv', 'yuv_to_rgb','ffmpeg_resize','serpentine','color_to_bw',run_length_encoding.")
        sys.exit(1)

    print("Result:", result)
