import glob

from skimage import io
import csv


image_list = []
label_list = []

for infile in glob.glob("/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/ForestFireClassification/images/*.jpg"):
    img = io.imread(infile)
    image_list.append(img)

with open("labels1.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        vals = row[0].split(",")
        label_list.append(vals[1])


print(len(label_list))


print("!!!!!!!")

print(image_list[1].shape)
print(len(image_list))
