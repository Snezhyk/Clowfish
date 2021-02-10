import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "./images/"

nemos_friends = []
for i in range(3):
    friend = cv2.cvtColor(cv2.imread(path + str(i) + ".jpg"), cv2.COLOR_BGR2RGB)
    nemos_friends.append(friend)


def segment_fish(image):
    ''' Cегментация рыбы-клоуна из предоставленного изображения '''

    # Конвертация изображения в HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Установка оранжевого диапазона
    light_orange = (1, 190, 160)
    dark_orange = (25, 255, 255)

    # Применение оранжевой маски
    mask = cv2.inRange(hsv_image, light_orange, dark_orange)

    # Установка белого диапазона
    light_white = (0, 0, 200)
    dark_white = (145, 110, 255)

    # Применение белой маски
    mask_white = cv2.inRange(hsv_image, light_white, dark_white)

    # Объединение двух масок
    final_mask = mask + mask_white
    result = cv2.bitwise_and(image, image, mask=final_mask)

    # Сглаживание сегментации с помощью размытия
    blur = cv2.GaussianBlur(result, (7, 7), 0)
    return blur


results = [segment_fish(friend) for friend in nemos_friends]

for i in range(0, 3):
    plt.subplot(1, 2, 1)
    plt.imshow(nemos_friends[i])
    plt.subplot(1, 2, 2)
    plt.imshow(results[i])
    plt.show()