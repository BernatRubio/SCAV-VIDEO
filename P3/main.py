import sys
from macroblocks import Macroblocks
from print_subtitles import print_subtitles
from yuv_histogram import yuv_histogram

def show_motion_vectors(input_file):
    macroblocks = Macroblocks()
    macroblocks.showMacroblocks(input_file)

def create_container(input_file):
    macroblocks = Macroblocks()
    macroblocks.createContainer(input_file)

def show_streams(input_file):
    macroblocks = Macroblocks()
    macroblocks.showStreams(input_file)


if __name__ == "__main__":

    function_name = sys.argv[1]
    input_file = sys.argv[2]

    if function_name == "show_motion_vectors":
        show_motion_vectors(input_file)
    elif function_name == "create_container":
        create_container(input_file)
    elif function_name == "show_streams":
        show_streams(input_file)
    elif function_name == "print_subtitles":
        subtitles_url = sys.argv[3]
        print_subtitles(input_file,subtitles_url)
    elif function_name == "yuv_histogram":
        yuv_histogram(input_file)
    
