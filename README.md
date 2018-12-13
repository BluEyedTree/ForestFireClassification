
# ForestFireClassification
CNN to detect forest fires from images. 

The idea from the project came from the following paper:
https://www.atlantis-press.com/proceedings/ifmeita-16/25850411

The data used was scraped from google images, and labeled manually using data turks.

In lieu of a binary classification (fire, no fire). We choose a quaternaryclassification (+fire+smoke, +fire-smoke, -fire+smoke, -fire-smoke). Where + indicates presence, and - indicates absence. 

 This project made use of transference learning. 
 The convolutional portion of the neural net was VGG16 pre-trained on the image net dataset. 
 We then experimented with freezing the updating of weights on certain layers of VGG16. 
 Finally, we tried different architectures for the final fully connected layers, and using the Keras image augmentation library.

The paper made use of a binary classifier, and achieved a test accuracy of 90%

We achieved a 94% test accuracy with a quaternary classification. 

