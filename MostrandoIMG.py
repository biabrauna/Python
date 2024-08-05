import numpy as np 
import matplotlib.image as mpimg 
from matplotlib import pyplot 

im = mpimg.imread('paisagem.jpg')
# variavel array do numpy em 3 dimensões (1280,960,3)
# numero de linhas, numero de colunas e numero de canais
# valor maximo 1 e minimo 0 (png)
# valor maximo 255 e minimo 0 (jpg)
# mais claro de 1 ou 255 mais claro


print(type(im))
print(im.shape)
print(np.max(im))
print(np.min(im))

# Criou o obj pra mostrar
pyplot.imshow(im)
pyplot.axis('off')
# desligando os eixos

# cria a janela e mostra
pyplot.show()
pyplot.close()
# garantir que vai fechar o obj quando clicar para fechar