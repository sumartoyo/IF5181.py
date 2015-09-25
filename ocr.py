import sys
import numpy as np

import gambar
import objek

def main(argv):
    img = gambar.read(argv[1])
    img = gambar.asgray(img)
    img = gambar.tobw(img)
    img = gambar.koponging(img)
    
    pixels = objek.getpixels(img)
    center = objek.getcenter(pixels)
    
    feature = objek.getfeature(img, pixels, center)
    print(objek.recognize(feature))
    # gambar.showlining(img, center, None)

if __name__ == ('__main__'):
    main(sys.argv)