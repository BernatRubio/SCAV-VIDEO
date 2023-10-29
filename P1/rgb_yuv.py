import sys
import subprocess
import os
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

    cmd = f'ffmpeg -i "{path_to_im}" -vf "scale=360:-1" "./{output_path}"'
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Resize successful. Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

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
                for x, y in zigzag_order:
                    byte = image_file.read(1)
                    if not byte:
                        break
                    zigzag_data.append(byte)
        print("Serpentine encoding successful.")
        return zigzag_data
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def color_to_bw(image_path, crf):
    base_name, ext = os.path.splitext(os.path.basename(image_path))
    output_path = f"./{base_name}_bw_crf{crf}{ext}"

    cmd = f'ffmpeg -i "{image_path}" -vf "format=gray" -q:v {crf} "{output_path}"'

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Conversion successful. Image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_length_encoding(input):
    data = list(input)
    encoded_data = OrderedDict.fromkeys(data, 0)

    for char in data:
        encoded_data[char] += 1

    encoded_str = ''.join([f'{key}{value}' for key, value in encoded_data.items()])
    print("Run-length encoding successful.")
    return encoded_str

def dct_encode(image_path):
    dct_processor = DCTProcessor()
    return dct_processor.dct_encode(image_path)

def dct_decode(encoded_data):
    dct_processor = DCTProcessor()
    return dct_processor.dct_decode(encoded_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rgb_yuv.py function_name [parameters]")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name in {"rgb_to_yuv", "yuv_to_rgb"} and len(sys.argv) != 5:
        if(function_name=="rgb_to_yuv"):
            print(f"Usage: python rgb_yuv.py {function_name} R G B")
        elif(function_name=="yuv_to_rgb"):
            print(f"Usage: python rgb_yuv.py {function_name} Y U V")
    elif function_name == "ffmpeg_resize" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py ffmpeg_resize 'path_to_im'")
    elif function_name == "serpentine" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py serpentine 'image_path'")
    elif function_name == "color_to_bw" and len(sys.argv) != 4:
        print("Usage: python rgb_yuv.py color_to_bw 'image_path' 'crf'")
    elif function_name == "run_length_encoding" and len(sys.argv) != 3:
        print("Usage: python rgb_yuv.py run_length_encoding 'input_string'")
    elif function_name in {"dct_encode", "dct_decode"} and len(sys.argv) != 3:
        print(f"Usage: python rgb_yuv.py {function_name} 'image_path'")
    else:
        try:
            if function_name == "rgb_to_yuv":
                r, g, b = map(float, sys.argv[2:5])
                result = rgb_to_yuv(r, g, b)
            elif function_name == "yuv_to_rgb":
                y, u, v = map(float, sys.argv[2:5])
                result = yuv_to_rgb(y, u, v)
            elif function_name == "ffmpeg_resize":
                im_path = sys.argv[2]
                result = ffmpeg_resize(im_path)
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
            else:
                print("Invalid function name. Use 'rgb_to_yuv', 'yuv_to_rgb', 'ffmpeg_resize', 'serpentine', 'color_to_bw', 'run_length_encoding', 'dct_encode', 'dct_decode'.")
        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Result:", result)
