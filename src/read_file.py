import struct

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