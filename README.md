# copy-specific-images-from-one-folder-to-other
Used to refine my dataset for research project

# This was used to separate an image dataset in which i was having 2,00,000 + images in one folder and csv files having their sentiment Positive, Neg, Neutral.

# Dataset research paper: 
Image sentiment analysis using latent correlations among visual, textual, and sentiment views
Conference Proceedings: 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)
Author: Marie Katsurai
Publisher: IEEE
Date: March 2016
Copyright © 2016, IEEE

This paper was having all the images in one folder but we were needing images in separate folders Pos, Neg and Neutral so this code just copies data from one main folder to other 3 sub folders using shutil.
</br>
</br>
All images was categorised and sentiment stored in csv file.
</br>
In this code we are choosing only those images which are having sentiment majority atleast 2 out of 3. 
</br>
<h4>If any image is having equal sentiment score for all categories we are not choosing it.</h4> 
