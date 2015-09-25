from os import listdir
from os.path import isfile, join, splitext
import json

import gambar
import objek

def main():
    features = []
    path = 'train'
    for name in [f for f in listdir(path) if isfile(join(path, f))]:
        img = gambar.read(join(path, name))
        img = gambar.asgray(img)
        img = gambar.tobw(img)
        img = gambar.koponging(img)
        
        pixels = objek.getpixels(img)
        center = objek.getcenter(pixels)
        feature = objek.getfeature(img, pixels, center)
        
        features.append({'label': splitext(name)[0], 'data': feature.tolist()})
    
    with open('features.json', 'w') as outfile:
        json.dump(features, outfile)

if __name__ == ('__main__'):
    main()