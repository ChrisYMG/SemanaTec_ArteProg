# SemanaTec_ArteProg

# Miembros del equipo

Jorge Ramón González Ozorno A0137845

Christian Yael Mejía Galindo A01770081

Omar Alejandro Rodríguez Valencia A01769948

María Fernanda Zavala Ramírez A01769162

Ricardo Adolfo González Terán A01769410

# Objetivo

Generar un código de python mediante el cual se aplicarán diferentes kernel a una imagen en específico, obteniendo así una imagen distorsionada por los filtros utilizados. Mediante la aplicación de los conceptos vistos en clase se obtendrá como salida las funciones de Mexican Hat, Gaussian Blur, Top Sobel, Laplacian of Gaussian y Laplace.

# Resumen del repositorio

Nuestro main utiliza y enlaza las funciones Mexican Hat, Gaussian Blur, Top Sobel, Laplacian of Gaussian y Laplace. Se realiza la importación y ejecución de las diferentes funciones pasándoles los parámetros necesarios. Cada uno de los integrantes programó un método diferente, para cada función se pide al usuario el tamaño del sigma y el tamaño del Kernel. El programa obtiene la imagen deseada del ordenador de la persona que lo está corriendo. Se utilizó la siguiente imagen:
SemanaTec_ArteProg/mr_increible.jpg at master · ChrisYMG/SemanaTec_ArteProg (github.com)

En el programa se ocupan diferentes módulos de Python para poder facilitar la visualización y el manejo de datos en el cálculo de los kernels y de la visualización de las imágenes a las que se les aplicarán los diferentes kernels, los módulos que se utilizan son: 

**Numpy** (Librería para manejo de números y operaciones, la cual también posee herramientas para las matrices)
**Pillow**  (Librería para poder editar parámetros de las imágenes, por ejemplo, convertirlas a escala de grises)
**MatPlotLib** (Librería para poder generar y mostrar gráficas con distintos elementos en diferentes ventanas y así poder mostrar el resultado de los kernels)
**Scipy** (Librería para poder aplicar las covaleciones a las imágenes aplicando los kernels a estas) 

Después de los módulos se importan las funciones del programa kernels.py, que se muestran a continuación en la fase de desarrollo.

# Desarrollo

## Funciones

**Laplacian of Gaussian:**

Los filtros laplacianos son filtros derivados utilizados para encontrar áreas de cambio rápido (bordes) en las imágenes. Dado que los filtros derivados son muy sensibles al ruido, es común suavizar la imagen (por ejemplo, usando un filtro gaussiano) antes de aplicar el laplaciano. Este proceso de dos pasos se denomina operación laplaciana de gaussiana o Laplacian of Gaussian (LoG). Para conseguir este filtro, combinamos las funciones laplaciana y gaussiana, obteniendo una sola ecuación:

![ecuacion_log](https://user-images.githubusercontent.com/102307137/160051584-6cbd1eef-cad9-41d2-b233-cf7be56f41b6.jpg)

Un kernel discreto para el caso de σ = 1.4 viene dado por:

![kernel_log](https://user-images.githubusercontent.com/102307137/160051689-9a5c01cf-639e-438d-8aa2-426e10868267.jpg)

El operador LoG toma la segunda derivada de la imagen. Donde la imagen es uniforme, el LoG dará cero. Dondequiera que ocurra un cambio, el LoG dará una respuesta positiva en el lado más oscuro y una respuesta negativa en el lado más claro.

**Top Sobel:**

Los filtros conocidos como “Sobel” tienen el objetivo de hacer énfasis en las diferencias en píxeles adyacentes en una dirección en específico. Funciona como una derivada, calculando la intensidad de la diferencia entre dos píxeles. Se suele utilizar para poder encontrar más fácilmente los bordes dentro de la imagen. Este kernel utiliza una de las siguientes matrices dependiendo de la dirección que se quiera enfatizar:

![top_sobel](https://user-images.githubusercontent.com/102307137/160052363-cacccba0-bd54-45fd-a2cf-0170e5cfb77b.jpg)

**Laplace:**

El filtro laplace es un detector de bordes que se utiliza para calcular las segundas derivadas de una imagen, midiendo la velocidad a la que cambian las primeras derivadas. Esto determina si un cambio en los valores de píxeles adyacentes se debe a un borde o a una progresión continua.

Los núcleos de filtro laplaciano generalmente contienen valores negativos en un patrón cruzado, centrado dentro de la matriz. Las esquinas son valores cero o positivos. El valor central puede ser negativo o positivo. Este kernel está dado por la siguiente fórmula:

![laplace](https://user-images.githubusercontent.com/102307137/160052477-e8a5d5fe-6b0f-4d9f-992f-3ed5db0fc5ea.jpg)

**Gaussian Blur:**

El desenfoque gaussiano es un tipo de filtro de desenfoque de imagen que utiliza una función gaussiana (que también expresa la distribución normal en estadística) para calcular la transformación que se aplicará a cada píxel de la imagen. La fórmula de una función gaussiana en una dimensión es:

![gauss](https://user-images.githubusercontent.com/102307137/160052932-71d45833-f276-4f2a-9f00-705c047e47e2.jpg)

