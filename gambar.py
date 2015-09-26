import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def read(path):
    return mpimg.imread(path)

def show(img):
    plt.imshow(img)
    plt.show()

def asimg(matrix):
    matrixr = (matrix-1)*-255 if matrix.dtype == 'bool' else np.copy(matrix)
    return (matrixr.reshape(matrixr.shape + (1,))
                   .repeat(3, -1)
                   .astype(np.uint8))

def asgray(img):
    imgr = img*255 if img.dtype == 'float32' else np.copy(img)
    return (imgr.mean(-1)
                .round()
                .astype(np.uint8))

def tobw(gray):
    return gray < 128

def koponging(bw):
    # this `probably` takes a lot of memory
    target = np.copy(bw) # target is index of removal
    target[:] *= np.roll(bw, 1, 0)  # roll down
    target[:] *= np.roll(bw, -1, 0) # roll up
    target[:] *= np.roll(bw, 1, 1)  # roll right
    target[:] *= np.roll(bw, -1, 1) # roll left
    return bw - target # change to False for target

# def koponging(bw):
    # kopong = np.copy(bw)
    # ''' The hell is this loop '''
    # for y in range(1, bw.shape[0]-1):
        # for x in range(1, bw.shape[1]-1):
            # if bw[y, x]:
                # kopong[y, x] = not (bw[y-1, x] and bw[y+1, x] and bw[y, x-1] and bw[y, x+1])
    # return kopong

def showlining(kopong, center, name):
    bergaris = ((kopong-1)*-255).astype(np.uint8)
    centerr = center.round().astype(np.uint32)
    bergaris[:, centerr[0]] = 128
    bergaris[centerr[1], :] = 128
    show(asimg(bergaris))
    # mpimg.imsave('{}.png'.format(name), asimg(bergaris))