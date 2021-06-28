from pdf2image import convert_from_path
import cv2
import os

pdf_labels = [a for a in os.listdir() if a.endswith(".pdf")]

pdf_labels.sort()

for label_number, label_name in enumerate(pdf_labels):
    pages = convert_from_path(label_name, 500)

    # Saving pages in jpeg format

    for page in pages:
        page.save(f'label_{label_number}.jpg', 'JPEG')

    img = cv2.imread(f'label_{label_number}.jpg')
    crop_img = img[2676:4719, 243:3155]
    rotated_img = cv2.rotate(crop_img, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(f'label_{label_number}.jpg', rotated_img)
    os.system(f'i_view64 {f"label_{label_number}.jpg"} /print')
