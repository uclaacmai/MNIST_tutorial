#!/usr/bin/env python3
from draw import Paint
import numpy as np
from sklearn.externals import joblib
from scipy.misc import imshow

drawing = Paint()
model = joblib.load('model.pkl')
im_arr = drawing.get_digit()
im_vec = im_arr.reshape(1, -1)

print(model.predict(im_vec))

try:
    imshow(im_arr)
except RuntimeError:
    pass

