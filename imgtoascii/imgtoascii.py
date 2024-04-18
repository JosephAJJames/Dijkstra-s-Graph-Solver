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

    def decideAsciiChar(number):
        if number in range(0, 28):
            char = "#"
        elif number in range(28, 56):
            char = "X"
        elif number in range(56, 84):
            char = "%"
        elif number in range(84, 112):
            char = "&"
        elif number in range(112, 141):
            char = "*"
        elif number in range(141, 168):
            char = "+"
        elif number in range(168, 196):
            char = "/"
        elif number in range(196, 224):
            char = "("
        elif number in range(224, 226):
            char = "."
        else:
            char = " "

        return char


    def processImage(self, image):
        self.image = Image.open(image)
        self.setAsciFile(open("asciiimage.txt", "w"))
        grey_scale = self.convertGrayScale()
        char = self.decideAsciiChar()
        
        


if __name__ == "__main__":
    imageProcessor = ImageProcessor()
    imageName = "former-ukip-leader-nigel-farage-and-hard-right-tory-mp-jacob-rees-mogg2.jpg"
    imageProcessor.processImage(imageName)
    print("working")