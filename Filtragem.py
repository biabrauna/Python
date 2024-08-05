import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot
from scipy.signal import convolve2d 

def splot(img,lin,col,ind):
    pyplot.subplot(lin,col,ind) # para colocar mais de uma imagem em uma mesma janela
    pyplot.gray()
    pyplot.imshow(img.astype('uint8'))
    pyplot.axis('off')

def rgb2gray(img):
    return 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
im = mpimg.imread('paisagem.jpg')

filtro = (1.0/16)*np.array([[1,2,1],[2,4,2],[1,2,1]]) # matriz 3x3, filtro passa baixa filtra a alta frequencia e só deixa passar baixa
imGray = rgb2gray(im[400:900,200:625]) # a terceira dimensão vai mostrar tudo

ruido = np.random.normal(0,0.3,imGray.shape) #media 0 e desvio padrao = 0.1
imRuidosa = imGray + ruido
imRuidosa[imRuidosa > 255] = 255 # condição dentro dos colchetes
imFiltrada = convolve2d(imRuidosa,filtro,boundary='symm',mode='same')
splot(imRuidosa,1,2,1); splot(imFiltrada,1,2,2)

pyplot.show()
pyplot.close()
