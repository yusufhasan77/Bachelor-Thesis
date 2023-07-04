### Python file that contains the class to load the data.

# Import the necessary libraries
# Import the os for working with directories and paths
import os
# Import randint as this will be used to make sure images are not paired
from random import randint
# Import Image from PIL to load images
from PIL import Image
# Import the torch Dataset class to create a Dataset class
from torch.utils.data import Dataset
# Import the transform in case any transformation is to be done
import torchvision.transforms as transforms


# Define a class to load the horse and zebra dataset
class horse2zebraDataset(Dataset):
    
    # Define the constructor
    def __init__(self, img_dir = "horse2zebra", mode = "train", transform=None):
        # Define the transform attribute
        self.transform = transform
        # Create an attribute to store the name of image directory
        self.img_dir = img_dir
        # Create an atrribute to store the mode
        self.mode = mode
        # Define the address of horse files
        self.path_img_horse = sorted(os.listdir( os.path.join(self.img_dir, self.mode + "A") ) )
        # Define the address of zebra files
        self.path_img_zebra = sorted(os.listdir( os.path.join(self.img_dir, self.mode + "B") ) )

    # Define the method that returns the length of the dataset
    def __len__(self):
        # Return the length of the dataset
        return min( len(self.path_img_horse), len(self.path_img_zebra) )

    def __getitem__(self, index_image):
        
        # Check if there is any transformation to be done
        if self.transform != None:
            # Get an image of a horse
            real_image_horse = self.transform( Image.open(
                os.path.join(self.img_dir, self.mode + "A/") +
                self.path_img_horse[index_image % len(self.path_img_horse)] ).convert("RGB") )
            # Get an image of a zebra, make sure it is random so there are no paired images
            real_image_zebra = self.transform( Image.open(
                os.path.join(self.img_dir, self.mode + "B/") +
                self.path_img_zebra[randint(0, len(self.path_img_zebra) - 1)] ).convert("RGB") )
            # Return the images
            return real_image_horse, real_image_zebra
        # If the there is no transform just return the images
        else:
            # Get an image of a horse
            real_image_horse = Image.open( os.path.join(self.img_dir, self.mode + "A/")
                                          + self.path_img_horse[index_image % len(self.path_img_horse)] ).convert("RGB")
            # Get an image of a zebra, make sure it is random so there are no paired images
            real_image_zebra = Image.open( os.path.join(self.img_dir, self.mode + "B/") 
                                          + self.path_img_zebra[randint(0, len(self.path_img_zebra) - 1)] ).convert("RGB")
            # Return the images
            return real_image_horse, real_image_zebra
###