from skimage import io
import json
import urllib
from urllib.request import urlretrieve  # Python 3
import csv



#This

img = io.imread("/Users/thomasbekman/Documents/ForChase/test.jpg")




#First step pull down all the files from the .json

josn_path = "/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/Final/Forest_FIre.json"



#print(type(img))


image = []
for line in open('/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/Final/Forest_FIre.json', 'r'):
    image.append(json.loads(line))


with open('labels1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    labels = []
    count = 0
    for i in image:
        label = i["annotation"]["labels"]
        link = i["content"]
        print(label)
        try:
            if(label[0] != 'garbage'):
                count += 1
                urlretrieve(link, "images/"+str(count)+".jpg")
                rowToWrite = []
                rowToWrite.append(str(count))
                rowToWrite.append(label[0])
                print(rowToWrite)
                spamwriter.writerow(rowToWrite)
            #print(label[0])
        except:
            print("Failed")


