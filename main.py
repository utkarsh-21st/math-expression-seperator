from function import *
from pathlib import Path
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Symbol extracter')
    parser.add_argument('-i', '--input_path', required=True, help='path of image to be processed')
    parser.add_argument('-o', '--output_path', required=True, help='path to save the processed files')
    parser.add_argument('--show_boxes', action='store_true', help='Display the image overlayed with boxes')

    global args
    args = parser.parse_args()


if __name__ == '__main__':
    parse_args()
    img_path = args.input_path
    img = read(img_path)
    # show(img, 'original')
    resize_img = resize(img, 600)  # resizing with a width of 600 while maintaining aspect ratio
    # show(resize_img, 'after resize')
    temp = apply_thresh(resize_img)
    # show(temp, 'after threshold')
    # each mask contains a single component of the abstract in the image
    path = Path.cwd() / 'saved'
    save_all_masks(temp, show_boxes=args.show_boxes, path=Path(args.output_path))
