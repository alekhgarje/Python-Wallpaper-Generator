from PIL import Image, ImageDraw
from random import randint, choice
import requests
import xml.etree.ElementTree as ET

colours = [(255,250,221), (223,193,133), (161,69,28), (168,32,0), (255,211,61)]
r = requests.get("https://www.colourlovers.com/api/palettes/random")
tree = ET.fromstring(r.content)
#root = ET.fromstring(r.content)
#for child in root.iter('*'):
#    print(child.tag)

resolution = (1920, 1200)
#image = Image.new("RGB", resolution, (randint(0, 255), randint(0, 255), randint(0, 255)))
image = Image.new("RGB", resolution, choice(colours))
ic = ImageDraw.Draw(image, "RGBA")

def circle():
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    diameter = randint(50, 1200)

    temp = list(choice(colours))
    temp.append(randint(25, 250))

    #ic.ellipse([x, y, x+diameter, y+diameter], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)))
    ic.ellipse([x, y, x+diameter, y+diameter], fill = tuple(temp))

def rectangle():
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    length = randint(50, 1200)
    width = randint(50, 1200)
    
    temp = list(choice(colours))
    temp.append(randint(25, 250))
    
    #ic.rectangle([x, y, x+length, y+width], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)))
    ic.rectangle([x, y, x+length, y+width], fill = tuple(temp))


def line():
    x = randint(0, resolution[0])
    y = randint(0, resolution[1])
    length = randint(50, 1200)
    width = randint(50, 1200)
    
    temp = list(choice(colours))
    temp.append(randint(25, 250))
    
    #ic.line([x, y, x+length, y+width], fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(25, 250)), width=randint(3, 10))
    ic.line([x, y, x+length, y+width], fill = tuple(temp), width=randint(3, 10))

#__________________________________________________________________________

shapes = ["circle", "rectangle", "line"]

for i in range(randint(5, 25)):
    shapename = choice(shapes)
    if shapename == "circle":
        circle()
    elif shapename == "rectangle":
        rectangle()
    elif shapename == "line":
        line()

image.show()