import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot

def splot(img,lin,col,ind):
    pyplot.subplot(lin,col,ind) # permite mostrar mais de uma imagem em uma janela só
    pyplot.imshow(img)
    pyplot.axis('off')

im = mpimg.imread("paisagem.jpg")
splot(im,2,2,1)
im2 = im + 0.3
im2[ im2 > 255 ] = 255
splot(im2,2,2,2)
im3 = im*4
im3[ im3 > 255 ] = 255
splot(im3,2,2,3)
im4 = im*4 + 0.1
im4[ im4 > 255 ] = 255
#splot(im4,2,2,4)
im5 = np.log(im + 3.0/255) # garantir que o log não vá pra menos infinito
im5 = (im5 - np.min(im5))/(np.max(im5)-np.min(im5))
splot(im5,2,2,4)

pyplot.show()
pyplot.close()