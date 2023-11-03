import subprocess
import os

class Macroblocks:
    
    def __init__(self) -> None:
        pass
    
    def showMacroblocks(self,input_file):
        
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        cmd = f'ffmpeg -hide_banner -flags2 +export_mvs -i {input_file} -vf codecview=mv=pf+bf+bb ./{base_name}_macroblocks{ext}'
        subprocess.run(cmd, shell=True, check=True)

    def createContainer(self,input_file):
        base_name, ext = os.path.splitext(os.path.basename(input_file))
        output1 = f'{base_name}_trimmed{ext}'
        cmd = f'ffmpeg -hide_banner -i {input_file} -ss 00:00:00 -t 00:00:50 -c:v copy -c:a copy {output1}'
        subprocess.run(cmd, shell=True, check=True)

        cmd2 = f'ffmpeg -hide_banner -i {output1} -vn -c:a libmp3lame -ac 1 {base_name}_mono.mp3'
        cmd3 = f'ffmpeg -hide_banner -i {output1} -vn -ac 2 -c:a libmp3lame -b:a 128k {base_name}_stereo.mp3'
        cmd4 = f'ffmpeg -hide_banner -i {output1} -vn -ac 2 -c:a aac {base_name}_stereo.aac'
        cmd5 = f'ffmpeg -i {output1} -i {base_name}_mono.mp3 -i {base_name}_stereo.mp3 -i {base_name}_stereo.aac -map 0:v:0 -map 1:a:0 -map 2:a:0 -map 3:a:0 -metadata:s:a:0 title="MP3 Mono" -metadata:s:a:1 title="MP3 Stereo" -metadata:s:a:2 title="AAC Stereo" -c:v copy -c:a copy output_with_3_audios{ext}'
        subprocess.run(cmd2, shell=True, check=True)
        subprocess.run(cmd3, shell=True, check=True)
        subprocess.run(cmd4, shell=True, check=True)
        subprocess.run(cmd5, shell=True, check=True)

    def showStreams(self,input_file):
        cmd = f'ffprobe {input_file} -hide_banner -show_entries format=nb_streams -v 0 -of compact=p=0:nk=1'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"The number of tracks of video {input_file} is {result.stdout}")
