import sys
import numpy as np

import gambar
import objek

def main(path):
    img = gambar.read(path)
    img = gambar.asgray(img)
    img = gambar.tobw(img)
    img = gambar.koponging(img)
    
    pixels = objek.getpixels(img)
    center = objek.getcenter(pixels)
    feature = objek.getfeature(img, pixels, center)
    return objek.recognize(feature)

if __name__ == ('__main__'):
    print main(sys.argv[1])
    # gambar.showlining(img, center, None)