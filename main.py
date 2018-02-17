import struct
from discriminator import *
from node import *

def readFiles(labelsFilePath, imagesFilePath):
    flImg = open(imagesFilePath, 'rb')
    flLbl = open(labelsFilePath, 'rb')
    (mNumberImg, sizeImg, height, width) = struct.unpack('>IIII', flImg.read(16))
    (mNumberLbl, sizeLbl) = struct.unpack('>II', flLbl.read(8))
    imgs = []
    labels = map(ord, flLbl.readlines()[0])
    for i in range(sizeImg):
        imgs.append({'img': map(ord, list(flImg.read(width*height))), 'label': labels[i]})
    flImg.close()
    flLbl.close()
    return imgs


if __name__ == "__main__":
    ##Using the MNIST Handwrite dataset http://yann.lecun.com/exdb/mnist/
    imagesTrainingFile = 'train-images-idx3-ubyte'
    labelsTrainingFile = 'train-labels-idx1-ubyte'
    imagesTestFile = 't10k-images-idx3-ubyte'
    labelsTestFile = 't10k-labels-idx1-ubyte'

    # imgHeight, imgWidth = (28, 28) ##784 posições.
    # Training Images Array with labels
    training = readFiles(labelsTrainingFile, imagesTrainingFile)

    # Instantiation of discriminators
    discriminators = []
    for i in range(9):
        discriminators.append(Discriminator(98, 784, str(i)))

    # Training of Discriminators
    for i in training[0:1000]:
        d = [k for k in discriminators if k.label == str(i['label'])]
        if len(d) > 0 and d[0].label != '':
            d[0].train(i['img'])

    # Tests Images array with labels 
    testing = readFiles(labelsTestFile, imagesTestFile)
    rightCount, wrongCount = (0, 0)
    for i in testing[0:100]:
        discriminatorValue, discriminatorLabel = max([[d.getNodesResponse(i['img']), d.label] for d in discriminators])
        if discriminatorLabel == str(i['label']): rightCount += 1
        else:  wrongCount += 1

    #Print Results
    print("Acertou {0} e Errou {1}".format(rightCount, wrongCount))
