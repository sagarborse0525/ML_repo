# -*- coding: utf-8 -*-
"""tensors-demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e2qKvawQfaVZLi5r9qITG3Epz5_1hSAH

** What is Tensors?**

** In machine learning. A tensor is a multi-dimensional array of numerical values used to represent data. It is fundamental data structure in machine learning and deep learning frameworks like TensorFlow and PyTorch.
We can think of a tensor-like container that can hold a scaler (0-D), a vector (1-D), matrices (2-D), and a high-dimensional array (3-D, 4-D).
Tensors are used to represent various types of data, for example: images, audio signals, text data, and graphs. Following are the tensor examples. **

**1.Scaler(0D tensor)**
"""

import numpy as np
a = np.array(10)
print(a)
print("Dimentional : ",a.ndim)

"""**2.Vector(1-D Tensor):Vector is array of numbers.It has 1 Axis and 1-dimensional Tensor**"""

b = np.array([10,20,30])
print(b)
print("Dimentional : ",b.ndim)

"""**3.Matrices(2D tensor):
Matrices is nothing but collection of vectors. It has 2 Axis and 2-dimensional Tensor**
"""

c = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(c)
print("Dimentional : ",c.ndim)

"""**N-Dimensional tensor: **

"""

d = np.array([[[10,20,30],[40,50,60],[70,80,90]],[[10,20,30],[40,50,60],[70,80,90]]])
print(d)
print("Dimentional : ",d.ndim)