import sys
import os
sys.path.append('../P2')
from bunny_converter import ffmpeg_resize
import subprocess

class ResCompressor:
    
    def __init__(self) -> None:
        pass
    
    def resize(self,input_file, resx, resy):
        ffmpeg_resize(input_file, resx, resy)
    
    def changeCodec(self,input_file, codec):
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        if codec.lower() == "vp8":
            cmd = f"ffmpeg -i {input_file} -c:v libvpx -b:v 0 ./{base_name}_{codec}.webm"
        elif codec.lower() == "vp9":
            cmd = f"ffmpeg -i {input_file} -c:v libvpx-vp9 -b:v 0 ./{base_name}_{codec}.webm"
        elif codec.lower() == "h265":
            cmd = f"ffmpeg -i {input_file} -c:v libx265 -b:v 0 ./{base_name}_{codec}.mp4"
        elif codec.lower() == "av1":
            cmd = f"ffmpeg -i {input_file} -c:v libaom-av1 -b:v 0 {base_name}.mkv"
            
        subprocess.run(cmd, shell=True, check=True)