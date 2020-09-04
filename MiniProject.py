######################################################################################
# MiniProject   : Image binarization / Sauvola method
# Author        : Madji Abderrahmane G02 (IAM)
# Email         : a.madji[Q]esi-sba.dz
# Tested on     : Pycharm CE 2019 / Python 3.8
# References    : Formulas ==> Adaptive document image binarization (Paper)
#                 Test Picture ==> Wikipedia (Birmingham Quran manuscript 645 AD)
######################################################################################

import numpy as np
from PIL import Image
from math import sqrt  # I used it to to calculate 'Standard deviation'
import pylab as plt

def Sauvola(imageIn, windowSize, k):

    imageOut = np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1]))) # new Blank Image
    sizeF = windowSize
    sizeF2 = windowSize//2 # This Value will be used to neglect the edges

    for i in range(sizeF2,imageIn.shape[0]-sizeF2): # Two loops to move the window
        for j in range(sizeF2,imageIn.shape[1]-sizeF2): # Starts from 'sizeF2' to neglect the edges
            mean = 0.0
            total = 0
            for m in range(sizeF): # Two loops to loop through the window
                for n in range(sizeF):
                    mean += imageIn[i+m-sizeF2, j+n-sizeF2] # add all the pixel's values of the window
                    total += 1 #Increment total
            mean = mean / total

            stand = 0.0
            total = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    stand += (mean - imageIn[i+m-sizeF2, j+n-sizeF2]) ** 2 #Calculating standard deviation
                    total += 1
            stand = sqrt(stand / total)

            #Formula from "Adaptive document image binarization, Jaako Sauvola"
            thres = mean * (1.0 + k * ((stand/128.0) - 1.0)) #Now that's our threshold value for that pixel

            if imageIn[i, j] > thres:   #if the pixel's value is > Our threshold then our new pixel = 255
                imageOut[i, j] = 255.0  #Affecting the binary values to our new image
            if imageIn[i, j] <= thres:  #if the pixel's value is =< Our threshold then our new pixel = 0
                imageOut[i, j] = 0.0    #Affecting the binary values to our new image

    return imageOut


#########SettingUp##########
imgOri = Image.open('quran.jpg') # Note: Image can be changed to 'peppers.bmp' to try non-text binarization
imgGreyScale = Image.open('quran.jpg').convert('L') #Charging Image, Converting to grayscale image
imgMat = np.array(imgGreyScale)  #Image to Matrix conversion
windowsize = int(input('Enter WindowSize : '))  #Getting windowsize from user
sauvolaImage = Sauvola(imgMat, windowsize, 0.25)  #Note : k is always 0.25
#############End###########

#############Results#############
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(imgOri)
plt.subplot(1, 2, 2)
plt.title('Sauvola')
plt.imshow(Image.fromarray(sauvolaImage), cmap='gray')
plt.show()
###########End-Results###########
