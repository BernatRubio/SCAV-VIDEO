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
    if len(sys.argv) < 2:
        print("Usage: python main.py [function] [parameters]\n"
              "Available functions are: show_motion_vectors, "
              "create_container, and show_streams.")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "show_motion_vectors":
        if len(sys.argv) != 3:
            print("Usage: python main.py show_motion_vectors 'input_file'")
            sys.exit(1)
        input_file = sys.argv[2]
        show_motion_vectors(input_file)
    elif function_name == "create_container":
        if len(sys.argv) != 3:
            print("Usage: python main.py create_container 'input_file'")
            sys.exit(1)
        input_file = sys.argv[2]
        create_container(input_file)
    elif function_name == "show_streams":
        if len(sys.argv) != 3:
            print("Usage: python main.py show_streams 'input_file'")
            sys.exit(1)
        input_file = sys.argv[2]
        show_streams(input_file)
    elif function_name == "print_subtitles":
        if len(sys.argv) != 4:
            print("Usage: python main.py print_subtitles 'input_file' "
                  "'subtitles_url'")
            sys.exit(1)
        input_file = sys.argv[2]
        subtitles_url = sys.argv[3]
        print_subtitles(input_file, subtitles_url)
    elif function_name == "yuv_histogram":
        if len(sys.argv) != 3:
            print("Usage: python main.py yuv_histogram 'input_file'")
            sys.exit(1)
        input_file = sys.argv[2]
        yuv_histogram(input_file)
    else:
        print("Wrong usage.\nUsage: python main.py [function] [parameters]\n"
              "Available functions are: show_motion_vectors, create_container, "
              "and show_streams.")