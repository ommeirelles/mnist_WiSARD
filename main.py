# from src.discriminator import *
from src.profile import *
from src.read_file import * 
from config import config

if __name__ == "__main__":
    ##Using the MNIST Handwrite dataset http://yann.lecun.com/exdb/mnist/
    imagesTrainingFile = '/Users/otaviomeirelles/Downloads/train-images-idx3-ubyte'
    labelsTrainingFile = '/Users/otaviomeirelles/Downloads/train-labels-idx1-ubyte'
    imagesTestFile = '/Users/otaviomeirelles/Downloads/t10k-images-idx3-ubyte'
    labelsTestFile = '/Users/otaviomeirelles/Downloads/t10k-labels-idx1-ubyte'

    # imgHeight, imgWidth = (28, 28) ##784 posições.
    # Training Images Array with labels
    # training = readFiles(labelsTrainingFile, imagesTrainingFile)

    # Instantiation of discriminators
    # discriminators = []
    # for i in range(9):
    #     discriminators.append(Discriminator(98, 784, str(i)))

    # # Training of Discriminators
    # while (len(training) > 0):
    #     i = training[0]
    #     del training[0]
    #     d = [k for k in discriminators if k.label == str(i['label'])]
    #     if len(d) > 0 and d[0].label != '':
    #         d[0].train(i['img'])
    # del training

    # # Tests Images array with labels 
    # testing = readFiles(labelsTestFile, imagesTestFile)
    # rightCount, wrongCount = (0, 0)
    # for i in testing:
    #     discriminatorValue, discriminatorLabel = max([[d.getNodesResponse(i['img']), d.label] for d in discriminators])
    #     if discriminatorLabel == str(i['label']): rightCount += 1
    #     else:  wrongCount += 1

    # #Print Results
    #     print("Acertou {0} e Errou {1}".format(rightCount, wrongCount))




    connection = pymongo.MongoClient(config["host"], config["port"])[config["database"]]
    '''
        It is 60.000 training images and 10.000 test images of 28x28 pixels of hadwrite numbers from 1-9
        I will train 4 profiles whihc each discriminators will have 196, 98, 56 and 49 nodes respectively.
    '''
    profiles = []
    for i in [{
        "nodes": 196,
        "description": "each node has 4 random positions from image"
    }, {
        "nodes": 98,
        "description": "each node has 8 random positions from image"
    }, {
        "nodes": 56,
        "description": "each node has 14 random positions from image"
    }, {
        "nodes": 49,
        "description": "each node has 16 random positions from image"
    }]:
        profiles.append(Profile(i["nodes"], i["description"], connection))
    for p in profiles:
        p.addDiscriminators([str(i) for i in range(9)])
    print('asfsafas')