import sys
from macroblocks import Macroblocks

def show_motion_vectors(input_file):
    macroblocks = Macroblocks()
    macroblocks.showMacroblocks(input_file)

def create_container(input_file):
    macroblocks = Macroblocks()
    macroblocks.createContainer(input_file)


if __name__ == "__main__":

    function_name = sys.argv[1]
    input_file = sys.argv[2]

    if function_name == "show_motion_vectors":
        show_motion_vectors(input_file)
    elif function_name == "create_container":
        create_container(input_file)

    
