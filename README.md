# ForestFireClassification
CNN to detect forest fires from images. 

 This project made use of transference learning. 
 The convolutional portion of the neural net was VGG16 pre-trained on the image net dataset. 
 We then experimented with freezing the updating of weights on certain layers of VGG16. 
 Finally, we tried different architectures for the final fully connected layer, and using the Keras image augmentation library.

Accuracy on test data set: 94%
