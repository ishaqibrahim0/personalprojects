import cv2
import numpy as np
import pandas as pd
import argparse

# takes image from user
#'C:\Users\big shaq\Downloads\inbox.jpeg'
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
# Reading image with opencv
img = cv2.imread(img_path)

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_cv('colors.cv', names=index, header=None)


# set the draw_function
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# mouse callback event
cv2.namesWindow('image')
cv2.setMouseCallback('image', draw_function)


# distance calculation
# equations d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loci[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
        return cname


# display image on window for user to interact with
while True:
    cv2.imgshow("image", img)
    if (clicked):
        # cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        # creates text string to display (color name and RGB values
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + 'B=' + str(b)
        # cvs.putText(img,text,start,font(0-7),frontScale, color, thickness, lineType
        cv2.putText((img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA))
        # for very light colors txt will show in black
        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText((img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA))
        clicked = False
        # break loop if user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27:
            break
cv2.destroyAllWindows()
