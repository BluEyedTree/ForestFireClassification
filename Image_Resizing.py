import glob



from PIL import Image
import os

'''
allImageFilePath = glob.glob("/Users/thomasbekman/Documents/ForChase/test/*.jpg")

file = "/Users/thomasbekman/Documents/Homework/Deep_Learning/Final Project/Processed"
size = 480,270
counter = 0
for i in allImageFilePath:
    im = Image.open(i)
    im.thumbnail(i)
    width, height = im.size
    print(type(im.size[0]))
    if(int(width) > 480 and int(height) > 270):
        im.thumbnail(i)
        im.save(file +str(counter), "JPEG")
        counter +=1

'''

from PIL import Image
import glob, os
import imghdr


size = 600,500

counter = 0
for infile in glob.glob("/Users/thomasbekman/Documents/ForChase/test/*.jpg"):


    im = Image.open(infile)
    #im.save("/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/Processed/" + "1.JPEG", "JPEG")
    width, height = im.size
    if (int(width) > 480 and int(height) > 270 and imghdr.what(infile)=="jpeg"):

        print()
        im.thumbnail(size)

        if(im.size[0] == 600 and im.size[1] >= 300):
            counter += 1
            size1 = 600, 300
            im_resized = im.resize(size1, Image.ANTIALIAS)
            #box – The crop rectangle, as a (left, upper, right, lower)-tuple.
            im_resized.save("/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/Processed/Forest_No_Fire/" + str(counter)+ ".JPEG", "JPEG")
    print(counter)