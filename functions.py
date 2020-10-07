# --------------------Image--------------
#
# |-------------> x-axis
# | $ $ $ $ $--------------------------------------------------------> (x, y)
# | $ $ $ $ $
# | $ $ $ $ $
# |
# y-axis


# --------------------numpy array--------------
#
# |-------------> x-axis
# | $ $ $ $ $--------------------------------------------------------> (y, x)
# | $ $ $ $ $
# | $ $ $ $ $
# |
# y-axis

import sys
import cv2 as cv
import numpy as np
from pathlib import Path


def read(path):
    img = cv.imread(path, 0)
    if type(img) == type(None):
        sys.exit("Error!, Invalid path")
    else:
        return img


def resize(img, width=600):
    b = width
    a = b / img.shape[1]
    return cv.resize(img, (b, int(img.shape[0] * a)), interpolation=cv.INTER_AREA)


def show(img, name='image'):
    cv.imshow(name, img)
    k = cv.waitKey(0) & 0xFF
    cv.destroyAllWindows()


def apply_thresh(img):
    return cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 155, 20)  # 155, 15


def get_box_coords(cnts):
    boxes = np.zeros((len(cnts), 4), dtype='uint8')
    for i, cnt in enumerate(cnts):
        x, y, w, h = cv.boundingRect(cnt)
        boxes[i] = x, y, w, h
    return boxes


def get_area_wise_order(cnts):
    def f(box):
        return box[2] * box[3]

    vfunc = np.vectorize(lambda cnt: f(cv.boundingRect(cnt)))
    areas = vfunc(cnts)
    order = np.argsort(areas)
    return order


def squarify(img):
    axis_0, axis_1 = img.shape
    diff = np.abs(axis_0 - axis_1)
    pad_1 = diff // 2
    pad_2 = pad_1 + (diff % 2)
    if axis_0 > axis_1:
        return np.pad(img, ((0, 0), (pad_1, pad_2)), mode='constant', constant_values=255)
    else:
        return np.pad(img, ((pad_1, pad_2), (0, 0)), mode='constant', constant_values=255)


def save_all_masks(img, show_boxes, path):
    cnts, _ = cv.findContours(255 - img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 1st stage contour
    pad_x = 2
    pad_y = 2

    mask = np.ones(img.shape, np.uint8) * 255

    for cnt in cnts:
        cv.drawContours(mask, [cnt], 0, (0, 0, 0), -1)

    cnts, _ = cv.findContours(255 - mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 2nd stage contour
    cnts = np.asarray(cnts)
    sizes = np.zeros(len(cnts))
    max_size = 0

    for i, cnt in enumerate(cnts):
        size = cv.contourArea(cnt)
        max_size = np.maximum(size, max_size)
        sizes[i] = size

    order = get_area_wise_order(cnts)
    cnts = cnts[order]
    sizes = sizes[order]

    temp = img.copy()
    for i, cnt in enumerate(cnts):
        size = sizes[i]
        if size > max_size / 20:
            x, y, w, h = cv.boundingRect(cnt)
            target = temp[y: y + h, x: x + w]
            target = np.pad(target, (2, 2), mode='constant', constant_values=255)
            target = squarify(target)
            temp[y: y + h, x: x + w] = 255
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv.imwrite(str(path / f'{i}.png'), target)
        else:
            x, y, w, h = cv.boundingRect(cnt)  # box enclosing given contour
            temp[y: y + h, x: x + w] = 255
    cv.imwrite(str(path / 'image_with_boxes.png'), img)
    if show_boxes == True:
        show(img)
