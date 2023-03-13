import sys
import PIL.Image

inputFile = sys.argv[1]

openedImage = PIL.Image.open(inputFile)
openedImage = openedImage.convert("L")
minimum = 255
maximum = 0
print("Indexing image...")
for x in range(openedImage.width):
    for y in range(openedImage.height):
        currentColor = openedImage.getpixel((x,y))

        if (currentColor < minimum):
            minimum = currentColor
        if (currentColor > maximum):
            maximum = currentColor

newImage = PIL.Image.new("L",(openedImage.width,openedImage.height))
print("Processing image...")
for x in range(newImage.width):
    for y in range(newImage.height):
        currentColor = openedImage.getpixel((x,y))

        colorRange = maximum - minimum

        newImage.putpixel((x,y),round((currentColor - minimum) / colorRange * 255))

print("Saving image...")
newImage.save(inputFile.rsplit(".",1)[0] + "-clamped.jpeg")
print("Done.")