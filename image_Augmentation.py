import pickle
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import csv




from keras.preprocessing.image import ImageDataGenerator

import scipy.misc



file = open('/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/ForestFireClassification/data.pkl','rb')


data = pickle.load(file)


xTrain = data["image"]
yTrain = data["label"]

new_y =[]
# tokenize the labels
for i in yTrain:
    if(i == '-Fire-Smoke'):
        new_y.append(0)
    elif (i == '-Fire+Smoke'):
        new_y.append(1)
    elif (i == '+Fire+Smoke'):
        new_y.append(2)


y_train_f = np_utils.to_categorical(new_y, 3)





datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    fill_mode='wrap')


with open('aug_labels.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('labels1.csv', newline='') as f:
        reader = csv.reader(f)

        for j in range(1,688):
            img = load_img(
                '/Users/thomasbekman/Documents/Homework/Deep_Learning/Final_Project/ForestFireClassification/images/' +str(j) + '.jpg')
            x = img_to_array(img)  # creating a Numpy array with shape (3, 150, 150)
            x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)
            row1 = next(reader)
            label = row1[1]

            print("We are on image: "+str(j))
            print("The associated label in the original CSV is: "+str(row1[0]))
            print("The label is:  "+ label)
            i = 0
            for batch in datagen.flow(x,save_to_dir='preview', save_prefix=str(j)+"___", save_format='jpeg'):
                rowToWrite = []
                rowToWrite.append(str(j))
                rowToWrite.append(label)
                spamwriter.writerow(rowToWrite)
                i += 1
                if i > 19:
                    break



