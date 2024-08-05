import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot
from scipy import misc

def show(fig,img):
    pyplot.figure(fig) # permite que mais de uma imagem seja mostrada ao mesmo tempo entrada é um inteiro
    pyplot.imshow(img)
    pyplot.axis('off')

im = mpimg.imread('paisagem.jpg')
imR = np.zeros(im.shape)
imR[:,:,0] = im[:,:,0] # todas as linhas e colunas da dimensão zero, vermelho
imG = np.zeros(im.shape)
imG[:,:,1] = im[:,:,1] # verde
imB = np.zeros(im.shape)
imB[:,:,2] = im[:,:,2] # azul

# show(0,imR) para png
show(0,imR.astype('uint8')) # figura 0, imR
show(1,imG.astype('uint8'))
show(2,imB.astype('uint8'))
# R=G=B=0 temos o preto, =255 temos o branco

# luminancia = imagem em niveis de cinza
# Y = 0.2989*R + 0.5870*G + 0.1140*B (considera a capacidade de absorção do olho humano) resulta numa matriz

def rgb2gray(img):
    return 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
def showGray(f,img):
    pyplot.figure(f)
    pyplot.gray()
    pyplot.imshow(img)
    pyplot.axis('off')

im = mpimg.imread('paisagem.jpg')
imGray = rgb2gray(im)
showGray(1,imGray)

# salvando as imagens
misc.imsave('nome.jpg',imR)

pyplot.show()
pyplot.close()
