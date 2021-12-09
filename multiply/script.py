import numpy as np
import matplotlib.pyplot as plt


X = np.matrix('1 1; 1 2; 1 3')

y = np.matrix('1 2 3; 2 3 1')

# dot product 
z = np.dot(X, y)
print(z)


# Colormap plot
figure = plt.figure()
axes = figure.add_subplot(111)

caxes = axes.matshow(z, interpolation ='nearest')
figure.colorbar(caxes)
plt.show()