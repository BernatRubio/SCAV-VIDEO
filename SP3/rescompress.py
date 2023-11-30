import os
import subprocess

class ResCompressor:
    
    def __init__(self) -> None:
        pass
    
    def resize(self,input_file,resx,resy):
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        output_path = f"{base_name}_{resx}_{resy}{ext}"

        cmd = f'ffmpeg -hide_banner -i "{input_file}" -vf scale={resx}:{resy} "./{output_path}"'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"Resize successful. Image saved as {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    
    def changeCodec(self,input_file, codec):
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        if codec.lower() == "vp8":
            cmd = f'ffmpeg -i "{input_file}" -c:v libvpx -b:v 0 ./{base_name}_{codec}.webm'
        elif codec.lower() == "vp9":
            cmd = f'ffmpeg -i "{input_file}" -c:v libvpx-vp9 -b:v 0 ./{base_name}_{codec}.webm'
        elif codec.lower() == "h265":
            cmd = f'ffmpeg -i "{input_file}" -c:v libx265 -b:v 0 ./{base_name}_{codec}.mp4'
        elif codec.lower() == "av1":
            cmd = f'ffmpeg -i "{input_file}" -c:v libaom-av1 -b:v 0 {base_name}_{codec}.mkv'
            
        subprocess.run(cmd, shell=True, check=True)
        
    def compareCodecs(self,input_file,codec1, codec2):
        self.changeCodec(input_file,codec1)
        self.changeCodec(input_file,codec2)
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        if codec1 == "vp8" or codec1 == "vp9":
            codec1new = "webm"
        if codec2 == "vp8" or codec2 == "vp9":
            codec2new = "webm"
        if codec1 == "h265":
            codec1new = "mp4"
        if codec2 == "h265":
            codec2new = "mp4"
        if codec1 == "av1":
            codec1new = "mkv"
        if codec2 == "av1":
            codec2new = "mkv"
        cmd = (
            
            f'ffmpeg -i "{base_name}_{codec1.lower()}.{codec1new}" -i "{base_name}_{codec2.lower()}.{codec2new}"' 
            ' -filter_complex [0:v][1:v]hstack -c:v libx264 -crf 23 -c:a aac -b:a 192k ./comparison_output.mp4'
        
        )
        
        cmd2 = "ffplay ./comparison_output.mp4"
        
        subprocess.run(cmd, shell=True, check=True)
        subprocess.run(cmd2, shell=True, check=True)