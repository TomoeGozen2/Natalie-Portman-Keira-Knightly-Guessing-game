import tkinter as tk
from PIL import Image, ImageTk
import glob
import random

window = tk.Tk()
window.title("Simple window")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("1280x720")

images = glob.glob('images/*.jpg')
random_photo_index = random.randint(0, len(images) - 1)
random_photo = images[random_photo_index]
image = Image.open(random_photo)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(window, image=photo, width="800", height="800")
image_label.pack()

def button_clicked(button_text):
    global random_photo

    if button_text in random_photo:
        random_photo = random.choice(images)
        image = Image.open(random_photo)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    else:
        button3 = tk.Button(window, text="You lose!")
        button3.place(x=500, y=800)

button1 = tk.Button(window, text="keira", command=lambda: button_clicked('keira'))
button1.place(x=400, y=500)

button2 = tk.Button(window, text="natalie", command=lambda: button_clicked('natalie'))
button2.place(x=600, y=500)

window.mainloop()
