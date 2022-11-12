import climage
import imgHandler

'''
    Author: Brayden Hill
    Description: Grabs Calvin and hobbes art to display on the terminal on open
'''

# Grab the image
outfile = imgHandler.GrabImage()

# Convert and print the image
terminalImage = climage.convert(outfile, is_unicode=True)
print(terminalImage)