from tkinter import *
from tkinter import filedialog
from PIL import Image ,ImageDraw,ImageFont ,ImageTk
from tkinter import messagebox

image = None
preview_image = None

def choose_img():
    global image
    file_path = filedialog.askopenfilename()
    print(file_path)
    image = Image.open(file_path)

    preview_copy = image.copy()
    preview_copy.thumbnail((200, 200))
    preview_image = ImageTk.PhotoImage(preview_copy)

    image_preview.config(text="", image=preview_image)
    image_preview.image = preview_image


def save_image():
    global image
    if not image:
        messagebox.showerror(title="No image",message="Please select an Image before clicking save")
    else:
        watermark = watermark_txt_entry.get()
        drawer = ImageDraw.Draw(image)
        font = ImageFont.truetype("LHANDW.TTF",size=40)
        drawer.text(xy=(10,10),text=watermark,font=font,fill="black")
        save_path = filedialog.asksaveasfilename(initialdir="C:/Users/D E L L/Pictures/Watermarked photos",
                                                 initialfile="water_marked_img.png",
                                                 defaultextension=".png")
        image.save(save_path)


def preview_watermark():
    if not image:
        messagebox.showerror(title="No image",message="Please select an Image before clicking preview")

    else:
        watermark = watermark_txt_entry.get()
        preview_copy = image.copy()
        preview_copy.thumbnail((200, 200))
        drawer = ImageDraw.Draw(preview_copy)


        font = ImageFont.truetype("LHANDW.TTF", size=5)
        drawer.text(xy=(10, 10), text=watermark, font=font, fill="black")
        preview_image = ImageTk.PhotoImage(preview_copy)

        image_preview.config(text="", image=preview_image)
        image_preview.image = preview_image




window = Tk()
window.title("Watermark marker")
window.config(height=400,width=400)


title_label = Label(text="Watermarker")
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

choose_img_button = Button(text="Choose Img",command=choose_img)
choose_img_button.grid(row=1, column=0, columnspan=2, pady=10)


watermark_txt = Label(text="Watermark Text :")
watermark_txt.grid(row=3, column=0, padx=10, pady=10)


watermark_txt_entry = Entry(width=30,)
watermark_txt_entry.grid(row=3, column=1, padx=10, pady=10)

save_buttons = Button(text="Save",command=save_image)
save_buttons.grid(row=4, column=0, columnspan=2, pady=20)

preview_button = Button(text="Preview",command=preview_watermark)
preview_button.grid(row=3,column=2,pady=10,padx=10)

image_preview = Label(text="Image Preview here :")
image_preview.grid(row=2, column=0, columnspan=2, pady=10)


window.grid_propagate(False)
window.mainloop()