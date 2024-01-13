# conda activate iWM

# https://stackru.com/questions/28475624/obnaruzhenie-simvolov-na-neodnorodnom-fonovom-izobrazhenii
# Идея состоит в том, чтобы размыть изображение двумя разными ядрами и вычесть соответствующие результаты:

# https://python-lab.ru/razmytie-po-gaussu-s-python-cv2

import cv2

img = "result_vangogh-512.jpg"

im = cv2.imread(img, 0)

#--- it is better to take bigger kernel sizes to remove smaller edges ---
kernel1 = 13
kernel2 = 41

blur1 = cv2.GaussianBlur(im,(kernel1, kernel1), 0) 
blur2 = cv2.GaussianBlur(im,(kernel2, kernel2), 0) 

cv2.imwrite("Difference_of_Gaussians_vangogh-512.png", blur2 - blur1)