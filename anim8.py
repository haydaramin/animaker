import cv2 as cv
import sys

# REQUIRES: how to open and close an image
# EFFECTS: opens the image, and closes it
def open_close_image(img_path_in):
    img = cv.imread(cv.samples.findFile(img_path_in))

    if img is None:
        sys.exit("could not read image in")

    cv.imshow("Display window", img)
    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite(img_path_in, img)

def main():
    file_path = input("enter path to image you want to open: ")
    open_close_image(file_path)

if __name__ == '__main__':
    main()
