import glob, cv2,os


# for img in glob.glob(os.path.join('inference/output', '*.*')):
#     print(img)
#     a = cv2.imread(img)
#     cv2.imshow('',a)
#     cv2.waitKey()


colors = [(0, 0, 255), (255, 0, 255), (0, 255, 0)]


def drawBBs(BBs, img):
    # img = cv2.resize(img, (1263, 947))
    for BB in BBs:
        BB = BB.split(" ")
        print(img.shape[1],img.shape[0])
        x = int(float(BB[1]) * img.shape[1])
        y = int(float(BB[2]) * img.shape[0])
        w = int(float(BB[3]) * img.shape[1])
        h = int(float(BB[4]) * img.shape[0])
        print(BB[0], x, y, w, h)
        # c = BB[4]

        # sc = BB[5]
        # x = BB[6]
        # y = BB[7]
        # z = BB[8]
        ### TODO: MI A TETVES FASZOM???
        # s = (x  , y )
        # e = (x + w, y + h)
        s = (x - w // 2, y - h // 2)
        e = (x + w // 2, y + h // 2)
        cv2.rectangle(img, s, e, colors[0], 1)
        # tl = (s[0], s[1]+15)
        # bl = (s[0], e[1]-5)
        # #cv2.putText(img,subclassNames[c][sc],tl,cv2.FONT_HERSHEY_COMPLEX_SMALL,0.75,colors[c])
        # coords = "(%.2f, %.2f, %.2f)" % (x,y,z)
        # cv2.putText(img,coords,bl,cv2.FONT_HERSHEY_COMPLEX_SMALL,0.65,colors[c])

    return img


import pickle
import cv2
import matplotlib.pyplot as plt
# This way it doesn't try to open a window un the GUI - works in python notebook
# matplotlib
# inline

# Read images
img = cv2.imread("./rgb_41.png")
# depth = cv2.imread("HW/g1/depth/1.png", -1)

# Read annotations
file = open('./rgb_41.txt', 'r')
annotations = file.readlines()
print(annotations)

# Visualization
# depth = depth / 5000.0
img = drawBBs(annotations, img)
img_rgb = img #cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Figure with subplots
# plt.figure(figsize=(30, 30))
# plt.subplot(1, 1, 1)
# plt.imshow(img_rgb)
cv2.imshow("",img_rgb)
cv2.waitKey()
# plt.subplot(1,2,2)
# plt.imshow(depth,cmap='gray')