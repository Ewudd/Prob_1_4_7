'''
frame.py
Frames an image for Rolex Corporation.

Program by Connor Toth and Reese Pugh
'''

import PIL
#import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  

RED = (255,0,0,0)
BLACK = (0,0,0,0)
LOGO = PIL.Image.open("rolex.png")
def alter_logo():
    #resizes logo
    LOGO.resize((100, 25))
alter_logo()


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
    mask = PIL.Image.new("RGBA", (width+100, height+100), (0,0,0, 255))
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
    logo_side1 = width/2 - LOGO.size[0]/2
    logo_side2 = width/2 + LOGO.size[0]/2
    
    
    


    #draw secondary rectangle border
    draw.rectangle([(10,height-10),(40,10)], fill = BLACK)
    draw.rectangle([(width-40,height-10),(width-10,10)], fill=BLACK)
    draw.rectangle([(10,height-10),(logo_side1,height-40)], fill = BLACK)
    draw.rectangle([(logo_side2,height-10),(width-10,height-40)], fill = BLACK)
    draw.rectangle([(10,40),(width-10,10)],fill=BLACK)
    
    
    del draw
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', mask.size, (0,0,0,0))
    result.paste(image, (50,height-50), mask=mask)
    return result
    #add actual image
    
    ###############
    
def frame_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.

    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified2')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with radius = 30% of short side
        new_image = frame_image(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    





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
