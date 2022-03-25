# Librerías a utilizar.

import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
from kernels import *

# Lectura de la imágen a utilizar
imgInput = Image.open('mr_increible.jpg')
I  = imgInput.convert('L')
I  = numpy.asarray(I)
I  = I / 255.0

# Padding

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 20)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
# Procesado de imágenes a través de los distintos kernels

I = numpy.pad(I, 10, pad_with, padder=0)

kernelMH = MexicanHat(3,9) 
kernelTS = TopSobel(3) 
kernelGB = GaussBlur(9,9) 
kernelLG = LaplacianGauss(9,9)
kernelLA = laplace(9) 

# Se realiza el convolve para cada kernel
imgTS = ndimage.convolve(I, kernelTS, mode='constant', cval=0.0)
imgGB = ndimage.convolve(I, kernelGB, mode='constant', cval=0.0) 
imgMH = ndimage.convolve(I, kernelMH, mode='constant', cval=0.0)
imgLA = ndimage.convolve(I, kernelLA, mode='constant', cval=0.0)
imgLG = ndimage.convolve(I, kernelLG, mode='constant', cval=0.0)

# Plot de los resultados obtenidos en cada kernel

plt.imshow(imgInput)
plt.xlabel('Input Image')
plt.show()


plt.imshow(imgTS)
plt.xlabel('Image Top Sobel')
plt.show()

plt.imshow(imgGB)
plt.xlabel('Image Gaussian Blur')
plt.show()

plt.imshow(imgMH)
plt.xlabel('Image Ricker Wavelet - Mexican Hat')
plt.show()

plt.imshow(imgLA)
plt.xlabel('Image Laplacian')
plt.show()

plt.imshow(imgLG)
plt.xlabel('Image Laplacian Gauss')
plt.show()

