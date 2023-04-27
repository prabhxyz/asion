import numpy as np
import cv2
from PIL import Image, ImageFilter
from data.parameters import blur
import sys

# Duplicate of process() from process.py
def process(threshold, min_area):
    # Process image
    image = Image.open(f"ml/input/image.png")
    image = image.filter(ImageFilter.BoxBlur(blur))
    def process_image (threshold, image):
        gray_image = image.convert("L")
        for x in range(gray_image.width):
            for y in range(gray_image.height):
                if gray_image.getpixel((x, y)) > threshold:
                    gray_image.putpixel((x, y), 255)
                else:
                    gray_image.putpixel((x, y), 0)
        return gray_image

    # Save processed image.
    processed_image = process_image(threshold, image)
    processed_image.save("ml/input/temp/processed.jpg")
    img = cv2.imread("ml/input/temp/processed.jpg", 0)

    # Find contours in the binary image
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # x value lists
    x_lst = []
    y_lst = []
    # Loop through all contours
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)
        if area > min_area:
            # Calculate the center of the contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                x_lst.append(cX)
                y_lst.append(cY)
    return x_lst, y_lst

def find_parameters():
    good_pairs = []
    good_thresholds = []
    i = 0
    b_num = 520
    for threshold in range(0, 255, 10):
        for min_area in range(0, 100, 5):
            list1, list2 = process(threshold, min_area)
            if 3 < len(list1) < 30:
                good_pairs.append((threshold, min_area))
                good_thresholds.append(threshold)
            i+=1
            sys.stdout.write('\r' + f"Loading... {(i / b_num) * 100}%")
    print()

    thld = np.median([t[0] for t in good_pairs]) # calculate the median of the first elements
    if thld % 10 != 0:
        thld+=5

    indices = np.where(thld == good_pairs)[0] # get the indices of the tuples with the median first element
    new_pairs = []
    for index in range(len(good_pairs)):
        if index in indices:
            new_pairs.append(good_pairs[index])

    mn_ar = np.median([t[1] for t in new_pairs]) # calculate the median of the second elements
    if mn_ar % 5 != 0:
        mn_ar+=2.5

    # Threshold, Min Area
    return thld, mn_ar

if __name__ == '__main__':
    print(find_parameters())