import numpy

# MexicanHat María Fernanda Zavala Ramírez
def MexicanHat(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(numpy.pi*sigma**4) * (1-(1/2)*((x**2+y**2)/(sigma**2))) * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# TopSobel Omar Alejandro Rodríguez Valencia
def TopSobel(K):
    A = numpy.zeros((K,K))
    A[K//2][K//2] = 0
    A[K//2 + 1][K//2] = -2
    A[K//2 - 1][K//2] = 2
    A[K//2][K//2 + 1] = 0
    A[K//2][K//2 - 1] = 0
    A[K//2 + 1][K//2 + 1] = -1
    A[K//2 + 1][K//2 - 1] = -1
    A[K//2 - 1][K//2 + 1] = 1
    A[K//2 - 1][K//2 - 1] = 1
    return A

# GaussBLur Christian Yael Mejía Galindo
def GaussBlur(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))

    return A


# LaplacianGauss Jorge Ramón González Ozorno
def LaplacianGauss(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2)))* numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# Laplace Ricardo Adolfo González Terán
def laplace(K):
    A=numpy.zeros((K,K))
    A[K//2][K//2] = 4
    A[K//2 + 1][K//2] = -1
    A[K//2 - 1][K//2] = -1
    A[K//2][K//2 + 1] = -1
    A[K//2][K//2 - 1] = -1
    return A



