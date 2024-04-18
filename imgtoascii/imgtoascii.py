from PIL import Image

class ImageProcessor:

    def __init__(self):
        self.image = None
        self.asciFile = None
    
    def setImage(self, image):
        self.image = image
    
    def setAsciFile(self, file):
        self.asciFile = file

    def convertGrayScale(self):
        self.image = self.image.convert("L")
        pxls = self.image.load()
        grey_scale = []
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                grey_scale.append(pxls[x, y]) #add grayscale integter values
            grey_scale.append("\n") #to show that a new line has started
        return grey_scale

    def processImage(self, image):
        self.image = Image.open(image)
        file = open("asciiimage.txt", "w")
        self.setAsciFile(file)
        grey_scale = self.convertGrayScale()
        print(grey_scale)



if __name__ == "__main__":
    imageProcessor = ImageProcessor()
    imageName = "former-ukip-leader-nigel-farage-and-hard-right-tory-mp-jacob-rees-mogg2.jpg"
    imageProcessor.processImage(imageName)
    print("working")