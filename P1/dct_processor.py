import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image

class DCTProcessor:
    def __init__(self):
        pass

    def dct_encode(self, image_path):
        try:
            # Open and read the image using Pillow (PIL)
            image = Image.open(image_path)
            image_data = np.array(image)

            # Ensure that image_data is a 2D NumPy array
            if len(image_data.shape) == 3:
                # Convert image_data to grayscale by averaging the color channels
                image_data = np.mean(image_data, axis=2)

            # Apply 2D DCT to the image data
            encoded_data = dct(dct(image_data, axis=0, norm='ortho'), axis=1, norm='ortho')

            return encoded_data
        except Exception as e:
            print(f"An error occurred during DCT encoding: {e}")
            return None

    def dct_decode(self, encoded_data):
        try:
            # Apply inverse 2D DCT to the encoded data
            decoded_data = idct(idct(encoded_data, axis=0, norm='ortho'), axis=1, norm='ortho')

            return decoded_data
        except Exception as e:
            print(f"An error occurred during DCT decoding: {e}")
            return None
