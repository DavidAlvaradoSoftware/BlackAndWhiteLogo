# Water Mark Black/White/Gray images

![Project Image](project-image-url)

> This program allows you to add a watermark (logo) to your black/gray and/or
> black/white images.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This program will allow you to place a watermark
on a single image or multiple images.
This is a great way to prevent other individuals from claiming your work
as their own. 

The difference between a watermark and just 
placing a logo on your image is that you are able to
customize the intensity of the watermark. This is handy when 
you don't want to draw attention away from your original intent.

#### Technologies

- Python
    1. tkinter
    2. opencv


[Back To The Top](#read-me-template)

---

## How To Use
-NOTE (If more than one image is being watermarked): 
For best results, all images should be THE SAME SIZE. Images
of differing size may cause part of the watermark to be cut off.
The watermark image (your logo) is usually of different size than the images
you are trying to watermark so its size is not of concern.

-NOTE (Colored images): All colored images will automatically be 
converted to black and gray images.

#### Installation
- The Easiest way to download would be to click the 
top right corner where it says "code"
and download the ZIP folder.

- Extract the contents into your desired location.

#### Initialization
To start the program:
- Windows: Open Command Prompt and change to the directory where you extracted
the downloaded files. Once inside, copy and paste the following command into
  CMD:
  ```html
    Python BlackAndWhiteLogoMain.py
  ```
  1. TIP: If you have the folder where the program resides open
    with File Explorer, in the address bar type in "CMD" and 
     command prompt will open in the directory you are currently in.

-Linux/IOS: Open command line/Terminal and 
change to the directory where you extracted
the downloaded files. Once inside, copy and 
paste the following command into
the command line:
    
```html
    ./BlackAndWhiteLogoMain.py
```
- Once the program's main window shows up, you can start watermarking your images!
#### Steps To Watermark
1. Choose your logo:
   ```
       - Click browse which is on the top right and 
         find your logo using the file explorer window that pops up.
       
       - Once you find your logo, select it and 
         click open on the bottom of the file explorer window.
    ```

2. Choose Single or Multiple images depending on your application.
    ```
       - If you only want to watermark a single image, 
         check the "Single image" option then and
         click submit.
       
       - If you want to watermark multiple images, 
         check the "multiple images" option and
         then click submit.
    ```

3. Choosing your image/folder location:
   
    NOTE: If you have multiple images, they must all be in one folder.
   ```
       - Single Image: 
            1. Click browse (bottom one not the top) to 
               find your image using the file explorer.
       
            2. Once you find your image, select it and 
               click open on the bottom of the file explorer window.
        
       - Multiple Images:
            1. Click browse (bottom one not the top) to  
               find your folder using the file explorer.
       
            2. Once you find your folder, select it and 
               click open on the bottom of the file explorer window.
       
       - Click "Preview Image" 
   ```
4. Watermark setup:
    ```
       - Intensity:
            1. In this text box, you can enter a DECIMAL 
               between 0 and 1. The closer the value is to 1
               the more visible the logo will be. The closer 
               the value is to 0, the logo will be less visible.
       
       - Logo placement: 
            1. This program uses a coordinate system to place
               the logo in your desired location. The "x" value corresponds 
               to the horizontal placement of your logo. The y corresponds 
               to the vertical placement. If you input 0 for x and y, the logo
               will be placed in the top left corner. 
               
               If you enter a number which lies outside of the resolution (shape) 
               of your image, your logo may be cropt or it may 
               not show up at all.
            
            TIP: To figure out the shape of your image/s (not logo),
                 right click on the image and select properties. For the logo
                 to be visible, your x and y coordinates should lie within the image
                 dimensions (shape).
   ```
   
5. Preview:
   ```
            - To preview your logo's location with respect to the image, 
              click on "preview". This will open a new window with the
              watermark added to your image. If you are watermarking multiple
              images, the program will retrieve the first image in your folder
              for you to adjust your watermark.
               
            - If you are not satisfied with the placement of your watermark, you
              can always adjust the values in the previous window and re-click 
              "preview". 
  
              NOTE: Everytime you click "preview" a new window will pop up
                    displaying a preview of your image with the current values in
                    the text boxes. It does not close any previous "preview" 
                    windows automatically. You will have to close those manually. 
   ```
6. Confirm and start watermarking:
    ```
           - Once you're satisfied with the placement of your watermark, click
             "Confirm and Start Blending". All images watermarked will be saved 
             in the "output" folder.

    ```


#### API Reference

```html
    <p>dummy code</p>
```
[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Twitter - [@jamesqquick](https://twitter.com/jamesqquick)
- Website - [James Q Quick](https://jamesqquick.com)

[Back To The Top](#read-me-template)