# Preview image done, now need to work on iteration if folder is selected. also need to work on output images to be
# placed in output folder.
import os
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *

import cv2
from PIL import ImageTk, Image

logo_location = None
image_location_label = None
image_or_images_folder_location = None
single_image_checkbox = None
multiple_image_checkbox = None
image_directory = None
cv2_image_for_processing = None
cv2_logo_for_processing = None


def main():
    if not os.path.isdir('output'):
        path = os.path.join(os.getcwd(), "output")
        os.mkdir(path)

    root = Tk(className="Watermark Black and White photos")
    root.geometry("800x400")

    # Logo
    logo = Label(root, text="Please choose the location of your logo:  ", anchor="w")
    logo.grid(row=0, column=0, padx=(10, 0), pady=(10, 50), sticky="w")

    browse_button_one = Button(root, text="Browse", command=lambda: file_explorer_logo(root), anchor="w")
    browse_button_one.grid(row=0, column=2, padx=0, pady=(10, 50), sticky="w")

    # File/Folder
    single_image_label = Label(root, text="Would you like to add a logo to a single image or multiple?")
    single_image_label.grid(row=2, column=0, padx=10)

    single_image_answer, multiple_images_answer = IntVar(), IntVar()

    global single_image_checkbox
    single_image_checkbox = Checkbutton(root, text="Single image", variable=single_image_answer, anchor="w")
    single_image_checkbox.grid(row=3, column=0, pady=(10, 10), padx=10, sticky="w")

    global multiple_image_checkbox
    multiple_image_checkbox = Checkbutton(root, text="Multiple images", variable=multiple_images_answer, anchor="w")
    multiple_image_checkbox.grid(row=3, column=1, pady=(10, 10), sticky="w")

    submit_button = Button(root, text="Submit",
                           command=lambda: submit(single_image_answer, multiple_images_answer, root), anchor="w")
    submit_button.grid(row=4, column=0, columnspan=2, padx=(10, 0), pady=(10, 50), sticky="W")

    preview_image_test = Button(root, text="Preview image", command=lambda: preview_image("Lenna.png"))
    preview_image_test.grid(row=6, column=0)
    root.mainloop()


def preview_image(img_file_name, folder=None):
    # In order for the image to display, we must use the global keyword to prevent it from being collected by
    # the garbage collector.
    global imgtk
    global logo_location
    image_preview_window = Toplevel()
    image_preview_window.title("Adjust logo placement and intensity")

    # Loads an image and converts it to grayscale regardless if its in color or grayscale
    if folder:
        img = cv2.imread(img_file_name + "/" + os.listdir(img_file_name)[0])
    else:
        img = cv2.imread(img_file_name)
    logo = cv2.imread(logo_location)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(gray_img)
    imgtk = ImageTk.PhotoImage(image=im)

    # Put it in the display window
    show_image = Label(image_preview_window, image=imgtk)
    show_image.grid(row=0, column=0, columnspan=5)

    # Intensity and logo location labels and text boxes.
    intensity = Label(image_preview_window, text="Choose Logo Intensity (Decimal between 0 and 1")
    intensity.grid(row=1, column=0, sticky="w")
    intensity_textbox = Entry(image_preview_window, width=10)
    intensity_textbox.grid(row=1, column=1, sticky="w")

    location = Label(image_preview_window, text="Choose logo placement (Whole numbers only)")
    location.grid(row=2, column=0, sticky="w")

    x = Label(image_preview_window, text="x:")
    x.grid(row=2, column=1, sticky="e")
    x_coordinate = Entry(image_preview_window, width=5)
    x_coordinate.grid(row=2, column=2, sticky="w", pady=(5, 10))

    y = Label(image_preview_window, text="y:")
    y.grid(row=2, column=3, sticky="e")
    y_coordinate = Entry(image_preview_window, width=5)
    y_coordinate.grid(row=2, column=4, sticky="w", pady=(5, 10))

    # image preview button
    image_preview_submit_btn = Button(image_preview_window, text="Preview",
                                      command=lambda: preview_window_submit(gray_img,
                                                                            gray_logo,
                                                                            x_coordinate.get(), y_coordinate.get(),
                                                                            intensity_textbox.get()))
    image_preview_submit_btn.grid(row=3, column=0, columnspan=5, sticky="nsew", padx=20, pady=(0, 20))

    # Start button
    start_blending_btn = Button(image_preview_window, text="Confirm and Start Blending",
                                command=lambda: blend_all(gray_logo, img_file_name, folder, y_coordinate.get(),
                                                          x_coordinate.get(),
                                                          intensity_textbox.get()))
    start_blending_btn.grid(row=4, column=0, columnspan=5, sticky="nsew", padx=20, pady=(0, 20))


def blend_all(logo, img_file_name, folder, x, y, intensity):
    if check_values(intensity, x, y):
        x = int(x)
        y = int(y)
        intensity = float(intensity)
        if folder is not None:
            for image in range(len(os.listdir(img_file_name))):
                # retrieve image
                image_name = os.listdir(img_file_name)[image]
                img = cv2.imread(img_file_name + "/" + image_name)
                # convert to grayscale
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # blend with logo
                blended_img = blend(gray_img, logo, x, y, intensity)
                # save to output folder
                save_blended_image(blended_img, image_name)
        else:
            img = cv2.imread(img_file_name)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blended_img = blend(gray_img, logo, x, y, intensity)
            # save to output folder
            last_slash = img_file_name.rfind('/')
            img_name = img_file_name[last_slash + 1:]
            save_blended_image(blended_img, img_name)
    showinfo("Success",
             "All images have been blended with your logo. These new images will be place in the output folder.")


def save_blended_image(blended_img, img_name):
    output_directory = 'output/'
    output_image_name = output_directory + img_name + datetime.now().strftime("%H%M%S%f") + ".jpg"
    cv2.imwrite(output_image_name, blended_img)


def check_values(intensity, x, y):
    result = None
    try:
        intensity = float(intensity)
        x = int(x)
        y = int(y)
    except:
        showerror(title="Invalid values",
                  message="X and Y values must be whole numbers and Intensity value a decimal between 0 and 1. No "
                          "letters or special characters are accepted.")
        return False
    else:
        if intensity > 1 or intensity < 0:
            showerror(title="Invalid intensity value", message="Intensity value must be between 0 and 1")
            result = False
        elif not isinstance(x, int):
            showerror(title="Invalid x-coordinate value", message="Coordinate values should be whole numbers")
            result = False
        elif not isinstance(y, int):
            showerror(title="Invalid intensity value", message="Intensity value must be between 0 and 1")
            result = False

        else:
            result = True

    return result


def preview_window_submit(image, logo, x, y, intensity):
    if check_values(intensity=intensity, x=x, y=y):
        intensity = float(intensity)
        x = int(x)
        y = int(y)
        blended_image = blend(image, logo, y, x, intensity)
        cv2.imshow("Blended_image", blended_image)


def blend(image, logo, x=None, y=None, alpha=None):
    """Function accepts image,
    logo, x-coordinate, y-coordinate,
    and alpha and returns blended image.
    """
    i = y
    blended_image = image.copy()
    for row in range(logo.shape[0]):
        if x == blended_image.shape[1]:
            break
        for col in range(logo.shape[1]):
            if y == blended_image.shape[1]:
                break
            blended_image[x, y] = (alpha * image[x, y]) + ((1 - alpha) * logo[row, col])
            y = y + 1
        y = i
        x = x + 1
    return blended_image


def submit(single_image_answer, multiple_images_answer, root):
    global image_directory

    if image_directory is not None:
        image_directory.destroy()

    if single_image_answer.get() == 1 and multiple_images_answer.get() == 0:
        image_directory = Label(root, text="Please choose your image location:")
        image_directory.grid(row=5, column=0, padx=(10, 5), sticky="w")
        browse = Button(root, text="Browse", command=lambda: file_explorer_single_image(root))
        browse.grid(row=5, column=2)
    elif single_image_answer.get() == 0 and multiple_images_answer.get() == 1:
        image_directory = Label(root, text="Please choose your image folder:")
        image_directory.grid(row=5, column=0, padx=(10, 5), sticky="w")
        browse = Button(root, text="Browse", command=lambda: file_explorer_folder(root))
        browse.grid(row=5, column=2)
    else:
        showerror(title="Error with selection", message="Please select one and only one.")


def file_explorer_logo(root):
    global logo_location
    logo_image_location = filedialog.askopenfilename(initialdir="c:/", title="Select the image",
                                                     filetypes=[
                                                         ("Image Files", ".bmp .dib .jpeg .jpg .jpe .jp2 .png .pbm "
                                                                         ".pgm .ppm .pxm .pnm .pfm .sr .ras .tiff "
                                                                         ".tif .exr .hdr .pic")])

    logo_location = logo_image_location
    logo_location_label = Label(root, text=logo_location, anchor="w")
    logo_location_label.grid(row=0, column=1, padx=(0, 10), pady=(10, 50), sticky="w")


def file_explorer_single_image(root):
    single_image_location = filedialog.askopenfilename(initialdir="c:/", title="Select the image",
                                                       filetypes=[
                                                           ("Image Files", ".bmp .dib .jpeg .jpg .jpe .jp2 .png .pbm "
                                                                           ".pgm .ppm .pxm .pnm .pfm .sr .ras .tiff "
                                                                           ".tif .exr .hdr .pic")])
    if len(single_image_location) > 0:
        global image_location_label
        global image_or_images_folder_location

        if image_location_label is not None:
            image_location_label.destroy()

        image_or_images_folder_location = single_image_location
        image_location_label = Label(root, text=image_or_images_folder_location)
        image_location_label.grid(row=5, column=1, padx=(5, 10), sticky="w")

        preview_image_test = Button(root, text="Preview image",
                                    command=lambda: preview_image(image_or_images_folder_location))
        preview_image_test.grid(row=6, column=0)


def file_explorer_folder(root):
    folder_location = filedialog.askdirectory(parent=root, initialdir="/", title='Please find your image folder')
    if len(folder_location) > 0:
        global image_or_images_folder_location
        global image_location_label
        if image_location_label is not None:
            image_location_label.destroy()

        image_or_images_folder_location = folder_location
        image_location_label = Label(root, text=image_or_images_folder_location)
        image_location_label.grid(row=5, column=1, sticky="w")

        preview_image_test = Button(root, text="Preview image",
                                    command=lambda: preview_image(image_or_images_folder_location, folder=True))
        preview_image_test.grid(row=6, column=0)


if __name__ == "__main__":
    main()
