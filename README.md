# Bachelor-Thesis
Repository for code used for doing bachelor thesis at Tilburg University

######## CODE FOR BACHELOR THESIS ########

### Dataset ###
To train the model first horse2zebra dataset has to be download and put in the data folder.

### Training the models ###

The .py files for training the models as well as the jupyter notebooks.
The models can be trained using either one of them.

### Different generator and discriminator architectures ###

The Models folder contains .py files on containing generator and discriminator architectures.
These models are created as functions and can be called in main training scripts.

e.g If I want to create a discriminator from the two available choices I can do

# If vanilla CycleGAN Discriminator is required
disc_X = CycleGAN_Discrminator(input_channels, initial_channels)

# If depthwise separable discriminator is required
disc_X = CycleGAN_Discrminator_DWS(input_channels, initial_channels)
