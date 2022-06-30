import cv2 as cv
import sys
import argparse
import pathlib as path

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

def border_test():


def main():
    parser = argparse.ArgumentParser(description='2d animation maker')
    parser.add_argument('photo', metavar='jpg', help='tagged picture to be animated')
    args = parser.parse_args()
    photo_path = args.photo
    print(photo_path)
    # file_path = input("enter path to image you want to open: ")
    # it gives an error if you do a relative file path but not an absolute why?
    # fix, use abouslute paths for now
    open_close_image(photo_path)

if __name__ == '__main__':
    main()
