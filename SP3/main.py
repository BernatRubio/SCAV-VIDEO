import sys
from rescompress import ResCompressor

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [function] [parameters]\n"
              "Available functions are: resize and "
              "change_codec.")
        sys.exit(1)

    function_name = sys.argv[1]
    input_file = sys.argv[2]
    
    if function_name == "resize":
        obj = ResCompressor()
        resx = sys.argv[3]
        resy = sys.argv[4]
        ResCompressor.resize(obj,input_file, resx, resy)
    elif function_name == "change_codec":
        obj = ResCompressor()
        codec = sys.argv[3]
        obj.changeCodec(input_file,codec)
    