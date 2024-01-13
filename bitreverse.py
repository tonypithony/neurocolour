# conda activate iWM

# pip install opencv-python

import cv2
import numpy as np

# очень медленный код и не оптимальный
def order_in_reversed_bits(data: np.ndarray) -> np.ndarray:
    tobinary = lambda t: np.binary_repr(t, width=len(np.binary_repr(data.shape[0]-1)))[::-1]
    func = np.vectorize(tobinary)
    a = func(np.arange(0,data.shape[0]))
    t = np.zeros(data.shape,dtype='float64')

    for i,k in enumerate(a):
        t[int(k,2)] = data[i]

    return t

def order_in_reversed_bits_python(lst):
    return order_in_reversed_bits(lst)
    # довольно быстрый, но работает ТОЛЬКО с черно-белыми изображениями
    return [v for _, v in sorted(enumerate(lst), key=lambda k: bin(k[0])[:1:-1])]

def rever(img:cv2.Mat,size:int=0)->cv2.Mat:
    if(size==0):
        size = img.shape[0]
    print(img.shape)
    print(size)
    print(img.shape[0]//size)
    # применим бит-реверсивную перестановку для каждой строки изображения
    for i in range(img.shape[0]):
        #меняем фрагментированно, для голографических свойств
        for j in range(0,img.shape[0]//size): 
            img[i][j*size:j*size+size] = order_in_reversed_bits_python(img[i][j*size:j*size+size])
    return img

def example2(img:cv2.Mat,size:int=0)->cv2.Mat:
    # приминяем бит реверсную перестановку для картинки горизонтально
    img = rever(img,size)
    # транспонируем матрицу(мменяем местами координаты x,y)
    img = cv2.transpose(img)
    # приминяем бит реверсную перестановку для картинки вертикально
    img = rever(img,size)
    # возвращаем матрицу на свое место
    img = cv2.transpose(img)
    return img

if __name__ == "__main__":
    
    # читаем картинку new.png и выводим на экран, ждем действий от пользователя
    img = cv2.imread('colored_text_for_vangogh.jpg', cv2.IMREAD_COLOR)
    

    h = 1024
    img = cv2.resize(img, (h, h))
    cv2.imwrite("before_vangogh.png",img)

    # применяем бит-реверсивную перестановку к изображению, 
    # получаем закодированное изображение, сохраняем в файл corupt.png выводим его на экран и ждем, 
    # если пользователь хочет его попробывать повредить, ждем действий от пользователя
    img = example2(img)
    cv2.imwrite("corupt_vangogh.png",img)
    
    # resize-attack
    img = cv2.imread('corupt_vangogh.png', cv2.IMREAD_COLOR)
    h = 512
    img = cv2.resize(img, (h, h))

    
    # # Читаем по новой из файла, который пользователь мог изменить, 
    # # выводим изменения на экран, чтобы пользователь убедился, что закодированное изображение повреждено, 
    # # ждем действий от пользователя
    
    img = cv2.imread('corupt_vangogh.png', cv2.IMREAD_COLOR)
    

    # # применяем бит-реверсивную перестановку для востановления изображения
    # # раскомментировать, для голографических свойств, а другую строку закомментировать
    
    # resize-attack
    H = 1024
    img = cv2.resize(img, (H, H))

    img = example2(img)

    # # выводим результат и ждем действий от пользователя
    cv2.imwrite(f"result_vangogh-{h}.jpg",img)