import numpy as np
import json

def getpixels(kopong):
    ''' returns [[x1, x2, ..., xn],
                 [y1, y2, ..., yn]] '''
    return np.asarray(kopong.nonzero())[[1,0]]

def getcenter(pixels):
    return pixels.mean(1)

def getfeature(kopong, pixels, center):
    feature = np.zeros((4, 8))
    for i in range(0, pixels.shape[1]): # for every pixel
        if pixels[0, i] >= center[0]:
            kuadran = 0 if pixels[1, i] >= center[1] else 1
        else:
            kuadran = 2 if pixels[1, i] < center[1] else 3
        for dir in range(0, 8): # for every direction
            nei = move(pixels[0, i], pixels[1, i], dir) # neighbor pixel
            if 0 <= nei[0] < kopong.shape[1] and 0 <= nei[1] < kopong.shape[0]: # if inside image
                if kopong[nei[1]][nei[0]]: # if pixel is black
                    feature[kuadran, dir] += 1
    return feature * (100.0 / pixels.shape[1])

def move(x, y, dir):
    return (x + (1 if dir in [0, 1, 7] else -1 if dir in [3, 4, 5] else 0),
            y + (1 if dir in [1, 2, 3] else -1 if dir in [5, 6, 7] else 0))

def recognize(test):
    with open('features.json') as infile:
        trained = json.load(infile)
    
    result, min = None, 9999
    for character in trained: # for every trained character
        error = ((test - character['data']) ** 2).sum()
        if error < min:
            result, min = character['label'], error
    return result