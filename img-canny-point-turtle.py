import turtle
import xml.etree.ElementTree as ET

tree = ET.parse("idx.xml")
root = tree.getroot()
print(root)  # <Element 'opencv_storage' at 0x7f9d6c222040>
print(root.tag)  # opencv_storage
print(root.attrib)  # {}

for child in root:
    print(child.tag, child.attrib)  # cannyresult {'type_id': 'opencv-matrix'}

print(
    [elem.tag for elem in root.iter()]
)  # ['opencv_storage', 'cannyresult', 'rows', 'cols', 'dt', 'data']


for movie in root.iter("data"):
    # print(movie.text) # <Element 'data' at 0x7f057b0013b0>
    print("for loop")

allPointText = [i.text for i in root.iter("data")]
# print(type(allPointText)) # <class 'list'>
allPointTextZero = allPointText[0].split(" ")
print(allPointTextZero)
# print(type(allPointTextZero)) # <class 'list'>
# print(len(allPointTextZero))  # 4384
allPointTextR = [i.strip("\n") for i in allPointTextZero]
# print(allPointTextR)


evenOdd = 0
xPoint = []
yPoint = []

for i in allPointTextR:

    if len(i) != 0:
        if evenOdd % 2 == 0:
            xPoint.append(int(i))
        else:
            yPoint.append(int(i))
        evenOdd += 1


# print(xPoint)
# print(yPoint)
print(max(xPoint))
print(max(yPoint))



zipPoint = zip(xPoint, yPoint)
listZipPoint = list(zipPoint)


# turtle.setworldcoordinates(600,600,600,600)
# set world coordinates
# llx lly urx ury
turtle.setworldcoordinates(100, 100, -40, -40)

turtle.setup(768, 768)

wn = turtle.Screen()
spiral = turtle.Turtle()
spiral.color("blue")
spiral.penup()


for point in listZipPoint:
    # spiral.down()
    spiral.goto(point)
    spiral.dot()
    spiral.penup()

turtle.done()
