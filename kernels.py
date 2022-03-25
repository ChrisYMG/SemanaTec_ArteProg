import numpy

# MexicanHat Ferza
def MexicanHat(sigma, K):
    A=numpy.zeros((K,K)) #Devulve matriz formada por ceros
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(numpy.pi*sigma**4) * (1-(1/2)*((x**2+y**2)/(sigma**2))) * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# TopSobel #Omar
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

# GaussBLur #Christian
def GaussBlur(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = 1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))

    return A


# LaplacianGauss #Jorge
def LaplacianGauss(sigma, K):
    A=numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            A[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2)))* numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return A

# Laplace #Ricardo
def laplace(K):
    A=numpy.zeros((K,K))
    A[K//2][K//2] = 4
    A[K//2 + 1][K//2] = -1
    A[K//2 - 1][K//2] = -1
    A[K//2][K//2 + 1] = -1
    A[K//2][K//2 - 1] = -1
    return A



