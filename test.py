import numpy as np

img = np.array([[[1 ,1 ,1],  [0,0, 0],[1,1,1]],[[1 ,1 ,1],  [0,0, 0],[1,1,1]]])
print(img)
print(img == 0)
print(img[img == 0])
