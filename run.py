import climage
import imgHandler

'''
    Author: Brayden Hill
    Description: Grabs a daily comic from calvin and hobbes and then displays it to the terminal.
    This will probably need some serious re-imagining to get artwork as text is completely unreadable, even at single block comic size.
'''

# Grab the image
outfile = imgHandler.GrabImage()

# Convert and print the image
terminalImage = climage.convert(outfile, is_unicode=True)
print(terminalImage)