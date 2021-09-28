import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser

import cv2
from pdf2image import convert_from_path

parser = ConfigParser()
parser.read('config.ini')

irfan_path = parser.get('path_to_irfan', 'path')
if irfan_path == 'ADD YOUR OWN PATH TO IRFAN VIEWER':
    logging.error('Please add a PATH to the Irfan Viewer executable in your '
                  'config.ini file.')
    sys.exit()


def main(l_number, l_name):
    pages = convert_from_path(l_name, 500)

    # Saving pages in jpeg format

    for page in pages:
        page.save(f'label_{l_number}.jpg', 'JPEG')

    img = cv2.imread(f'label_{l_number}.jpg')
    crop_img = img[2676:4719, 243:3155]
    rotated_img = cv2.rotate(crop_img, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(f'label_{l_number}.jpg', rotated_img)

    # Instantiate Irfan View to print the label
    os.system(
        f'{irfan_path} {f"label_{l_number}.jpg"} /print')


if __name__ == '__main__':
    pdf_labels = [a for a in os.listdir() if a.endswith(".pdf")]
    pdf_labels.sort()
    with ThreadPoolExecutor() as executor:
        for label_number, label_name in enumerate(pdf_labels):
            # Thread(target=main, args=(label_number, label_name)).start()
            # main(label_number, label_name)
            executor.submit(main, label_number, label_name)
