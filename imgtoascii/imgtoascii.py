from PIL import Image

class ImageProcessor:

    def __init__(self):
        self.image = None
        self.asciFile = None
    
    def setImage(self, image):
        self.image = image
    
    def setAsciFile(self, file):
        self.asciFile = file

    def resizeImage(self, scale): #method to resize image
        w, h = self.image.size
        if scale <= 0:
            scale = 1

        self.image = self.image.resize((w//scale, h//scale))

    def convertGrayScale(self):
        self.image = self.image.convert("L")
        pxls = self.image.load()
        grey_scale = []
        for y in range(self.image.size[1]):  # Iterate over height first
            for x in range(self.image.size[0]):  # Then iterate over width
                grey_scale.append(pxls[x, y])  # add grayscale integer values
            grey_scale.append("\n")  # to show that a new line has started
        return grey_scale

    def decideAsciiChar(self, number): #decides which character should replace a pixel based on its intensity
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
        elif number == "\n":
            char = "\n"
        else:
            char = " "
        
        return char

    def processImage(self, image, scale):
        self.image = Image.open(image)
        self.resizeImage(10)
        self.setAsciFile(open("asciiimage.txt", "a"))
        grey_scale = self.convertGrayScale()
        for x in range(len(grey_scale)):
            char = self.decideAsciiChar(grey_scale[x])
            self.asciFile.write(char)


if __name__ == "__main__":
    imageProcessor = ImageProcessor()
    imageName = input("Give the path to the image you'd like to convert:")
    scaleFactor = int(input("Give the scale factor you'd like to use to downsize the image"))
    imageProcessor.processImage(imageName, scaleFactor)