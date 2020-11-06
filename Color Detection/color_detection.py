import pandas as pd
import numpy as np
import cv2
import argparse
"""
    argparse will make easy to user if he give invalid agrs
    add_argument = it will give help to this agr at the time of taking input
"""
ap =argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help='Image Path')
args = vars(ap.parse_args())
img_path = args['image']

# now we will read image with opn cv lib
img = cv2.imread(img_path)

# declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

# reading csv file with pandas and giving index names to all columns
index=["color","color_name","hex","R","G","B"]
color = pd.read_csv('colors.csv',names=index,header=None)

# now we have rgb values we will make function to give color name
def get_color_name(R,G,B):
    minimum = 10000
    for i in range(len(color)):
        # color.loc[i,'R'] here i will be row value and R will the name of column this will return value at (i,r) position
        d = abs(R-int(color.loc[i,'R'])) + abs(G-int(color.loc[i,'G'])) + abs(B-int(color.loc[i,'B']))
        if(d<=minimum):
            minimum = d
            cname = color.loc[i,'color']
    return cname

# draw_function will calculate r,g,b values where mouse is clicked
def draw_function(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        # img[x,y] will return b,g,r values at position x,y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# now we will create image named window and in that window we will make fun n will call that fun whenever someone click on window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

# draw img on the window
while(1):
    cv2.imshow('image',img)
    if (clicked):
        # cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)

        #Creating text string to display ( Color name and RGB values )
        text = get_color_name(r,g,b) + '  R =' +str(r) + '  G =' + str(g) + '  B =' + str(b)

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if (r+g+b)>600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

            clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break 

cv2.destroyWindow()

