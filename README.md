# RGIT Recursion 2020: Image Crop Association

**The above code is written in JS & Python**

**Description**:

A web interface to associate cropped images with their original full- sized image. This was built during the RGIT Recursion Hackathon held on 13th and 14th March, 2020. The given dataset consisted of cropped images that were scaled, shrinked, rotated, skewed and noisy. We utlized SIFT+KNN to detect feature points and associate the cropped images to their respective original images. A memory game was also implemented on this interface.

**Video output of web interface (GIF below)**

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/12711480/76875021-fea71500-6895-11ea-9896-8fe1b8377a18.gif)

   **The given task was to**: 

    1. To identify associations between the provided cropped and original images.
    2. To specify the location of the crops from the original image in a json file

  **Required Libraries**: 

    1. NPM 
    2. VueJS
    3. OpenCV built from source
    
  **Important files**: 

    1. ./python/datase*t : Consists of the dataset provided during the competition 
    2. ./python/main.py : Has the SIFT+KNN algorithm. Saves the output in ./python/result.json
    3. ./public/result.json* : Copy the output from ./python/result.json & /public/result.json

    
  **To run the project**: 

    1. npm run serve
    
**Output of SIFT+KNN**</br>
 
![im-2](https://user-images.githubusercontent.com/12711480/76871467-17f99280-6891-11ea-96ad-0b29299fa994.jpg) </br>
    
****Program written by:****
+ Pranav Raut <br>
+ Sameer Pusegoankar <br>
+ Bhushan Patil <br>

