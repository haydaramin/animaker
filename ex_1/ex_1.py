import cv2

def ex_1():
    # imread reads image, takes path
    img = cv2.imread("src/flam.jpg")
    # imshow shows image, first arg is name of window, second arg is image obj
    cv2.imshow("output", img)
    # waitKey, waits for event, arg is delay in miliseconds
    cv2.waitKey(1000)

def ex_2():
    print("example 2: import a video")
    #  opens videocapture object
    cap = cv2.VideoCapture("src/mask.mp4")
    # saves
    while True:
        sucsess, img = cap.read()
        cv2.imshow("Video", img)
        # adds delay and breaks on Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
def ex_3():
    print("use webcam")
    cap = cv2.VideoCapture(0)
    #id 3 is width
    cap.set(3,640)
    #id 4 is height
    cap.set(4,480)
    # id 10 is brightness
    while True:
        sucsess, img = cap.read()
        cv2.imshow("webcam", img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

# usefull functions
def ex_4():
    img = cv2.imread("src/flam.jpg")
    # convert image to different color space
    # in this case grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    imgBlur = cv2.GausianBlur(imgGray)
    cv2.imshow("gray image", imgGray)
    cv2.waitKey(0)



if __name__ == "__main__":
    ex_4()
