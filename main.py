from PIL import Image, ImageDraw
from random import randint, choice
from numpy import imag
import xml.etree.ElementTree as ET
from colourlovers import clapi
from PIL import ImageColor

def circle(resolution,ic,colours):
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    diameter = randint(200, 1200)

    temp = list(choice(colours))
    temp.append(randint(25, 255))

    #ic.ellipse([x, y, x+diameter, y+diameter], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)))
    ic.ellipse([x, y, x+diameter, y+diameter], fill = tuple(temp))

def rectangle(resolution,ic,colours):
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    length = randint(200, 1200)
    width = randint(200, 1200)
    
    temp = list(choice(colours))
    temp.append(randint(25, 255))
    
    #ic.rectangle([x, y, x+length, y+width], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)))
    ic.rectangle([x, y, x+length, y+width], fill = tuple(temp))


def line(resolution,ic,colours):
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    length = randint(100, 1200)
    width = randint(100, 1200)
    
    temp = list(choice(colours))
    temp.append(randint(25, 255))
    
    #ic.line([x, y, x+length, y+width], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)), width=randint(3, 10))
    ic.line([x, y, x+length, y+width], fill = tuple(temp), width=randint(2, 20))

def getPalette(colours):
    cl = clapi.ColourLovers()
    response = cl.search_palettes(True,request='random')
    responseFile = open('responseFile.xml', 'w')
    responseFile.write(response)
    responseFile.close()
    tree = ET.parse('responseFile.xml')
    root = tree.getroot()
    for hex in root.iter('hex'):
        hex= '#'+hex.text
        rgbVal = ImageColor.getcolor(hex, "RGB")
        colours.append(rgbVal)
    # print (colours)


def generate(cnt):
    colours = []
    getPalette(colours)
    resolution = (1920, 1200)
    image = Image.new("RGB", resolution, choice(colours))
    ic = ImageDraw.Draw(image, "RGBA")
    shapes = ["circle", "rectangle", "line"]
    for i in range(randint(5, 30)):
        shapename = choice(shapes)
        if shapename == "circle":
            circle(resolution,ic,colours)
        elif shapename == "rectangle":
            rectangle(resolution,ic,colours)
        # elif shapename == "line":
        #     line(resolution,ic,colours)
    # image.show()
    imgName="'"+str(cnt)+".png'"
    print(imgName)
    image.save(imgName,'png')

for i in range(100):
    generate(i)
