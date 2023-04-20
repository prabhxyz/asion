import cv2
from PIL import Image, ImageFilter
import os

def process(threshold, min_area, blur):
    # Use any file type for input image, and then convert it to a .png
    if os.path.isfile("ml/input/input.png"):
        resize_img = cv2.imread("ml/input/input.png")
        resize_img = cv2.resize(resize_img, (400, 400))
        cv2.imwrite('ml/input/image.png', resize_img)
        os.remove("ml/input/input.png")  # delete the file
    else:
        resize_img = cv2.imread("ml/input/image.png")
        resize_img = cv2.resize(resize_img, (400, 400))
        cv2.imwrite('ml/input/image.png', resize_img)

    # Process image
    image = Image.open("ml/input/image.png")
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