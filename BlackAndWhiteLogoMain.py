# Next steps: Need to add function to blend in logo to image at a specific location and at a certain transparency.
# I should show the user a preview prior to saving the new image.
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import os
import subprocess

logo_location = None
image_location_label = None
image_or_images_folder_location = None
single_image_checkbox = None
multiple_image_checkbox = None
image_directory = None


def main():
    root = Tk(className="Black and White Logo adder")
    root.geometry("800x400")

    # Logo
    logo = Label(root, text="Please choose the location of your logo:  ", anchor="w")
    logo.grid(row=0, column=0, padx=(10,0), pady=(10,50), sticky="w")

    browse_button_one = Button(root, text="Browse", command=lambda: file_explorer_logo(root), anchor="w")
    browse_button_one.grid(row=0, column=2, padx=0, pady=(10,50), sticky="w")

    # File/Folder
    single_image_label = Label(root, text="Would you like to add a logo to a single image or multiple?")
    single_image_label.grid(row=2, column=0, padx=10)

    single_image_answer, multiple_images_answer = IntVar(), IntVar()

    global single_image_checkbox
    single_image_checkbox = Checkbutton(root, text="Single image", variable=single_image_answer, anchor="w")
    single_image_checkbox.grid(row=3, column=0, pady=(10,10), padx=10, sticky="w")

    global multiple_image_checkbox
    multiple_image_checkbox = Checkbutton(root, text="Multiple images", variable=multiple_images_answer, anchor="w")
    multiple_image_checkbox.grid(row=3, column=1, pady=(10,10), sticky="w")

    submit_button = Button(root, text="Submit",
                           command=lambda: submit(single_image_answer, multiple_images_answer, root), anchor="w")
    submit_button.grid(row=4, column=0, columnspan=2, padx=(10,0), pady=(10,50), sticky="W")

    root.mainloop()


def submit(single_image_answer, multiple_images_answer, root):
    global image_directory

    if image_directory is not None:
        image_directory.destroy()

    if single_image_answer.get() == 1 and multiple_images_answer.get() == 0:
        image_directory = Label(root, text="Please choose your image location:")
        image_directory.grid(row=5, column=0, padx=(10,5), sticky="w")
        browse = Button(root, text="Browse", command=lambda: file_explorer_single_image(root))
        browse.grid(row=5, column=2)
    elif single_image_answer.get() == 0 and multiple_images_answer.get() == 1:
        image_directory = Label(root, text="Please choose your image folder:")
        image_directory.grid(row=5, column=0, padx=(10,5), sticky="w")
        browse = Button(root, text="Browse", command=lambda: file_explorer_folder(root))
        browse.grid(row=5, column=2)
    else:
        error = showerror(title="Error with selection", message="Please select one and only one.")


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
        image_location_label.grid(row=5, column=1, padx=(5,10),sticky="w")


def file_explorer_logo(root):
    global logo_location
    logo_image_location = filedialog.askopenfilename(initialdir="c:/", title="Select the image",
                                                     filetypes=[
                                                         ("Image Files", ".bmp .dib .jpeg .jpg .jpe .jp2 .png .pbm "
                                                                         ".pgm .ppm .pxm .pnm .pfm .sr .ras .tiff "
                                                                         ".tif .exr .hdr .pic")])

    logo_location = logo_image_location
    logo_location_label = Label(root, text=logo_location, anchor="w")
    logo_location_label.grid(row=0, column=1, padx=(0,10), pady=(10,50), sticky="w")


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


if __name__ == "__main__":
    main()
