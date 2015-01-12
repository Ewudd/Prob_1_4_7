'''
frame.py
Frames an image for Rolex Corporation.

Program by Connor Toth and Reese Pugh
'''

import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  

RED = (255,0,0,0)
BLACK = (0,0,0,0)
LOGO = ...  #!~@#$%^

def frame_image(image):
    '''
    Frames an image with a frame that is really strange.
    
    Input:   
    image is a PIL.Image object
    
    Output:
    returns a PIL.Image object that has been framed.
    '''
    
    #sets width and height variables
    width, height= image.size
    #creates a mask and drawing image object
    mask = PIL.Image.new("RGBA", (width+100, height+100), (0,0,0,0))
    draw = PIL.ImageDraw.Draw(mask)
    
    #draw top border
    draw.rectangle([(0,height),(width,height-50)], fill=RED)
    #draw right border
    draw.rectangle([(0,height),(50,0)], fill=RED)
    #draw left border
    draw.rectangle([(width-50, height),(width,0)], fill = RED)
    #draw bottom border
    draw.rectangle([(0,50),(width,0)], fill = RED)
    #draw the logo in the top border
    logo_side1 = width/2 - LOGO.width/2
    logo_side2 = width/2 + LOGO.width/2
    
    
    
    #draw the logo in the bottom border


    #draw squares within borders
            #do some maths
            #loop through and draw each square on top/bottom
            #loop thru and draw each square on left/right
    
    
    
    #add actual image
    
    ###############
    
def frame_all_images()
    '''
    documentation
    '''
    
    
    ###############





def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
