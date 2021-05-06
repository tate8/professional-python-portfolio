from tkinter import *
from tkinter import messagebox
from PIL import Image
import urllib.request

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

type_local = False
type_url = False

def set_type_local():
    global type_local, type_url
    type_local = True
    type_url = False


def set_type_url():
    global type_local, type_url
    type_url = True
    type_local = False


def watermark():
    img_url = input.get()
    # if type_local == True and type_url == True:
    #     messagebox.showinfo(title='Oops', message='Don\'t check both boxes!')
    if type_local == True:
        try:
            base_image = Image.open(img_url).convert('RGB')
        except:
            messagebox.showinfo(title='Oops', message='Make sure you enter a valid filepath.')
    elif type_url == True:
        try:
            new_local = urllib.request.urlretrieve(img_url, 'pic.png')
            base_image = Image.open('pic.png')    
        except ValueError:
            messagebox.showinfo(title='Oops', message='Make sure you enter a valid url.')
    watermark = Image.open('images/wm.png').convert('RGBA')
    watermark = watermark.resize(base_image.size)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, (0,0), mask=watermark)
    transparent.show()
    transparent.save('wm_images/bg_watermarked.png')


window = Tk()
window.title('Watermarker')
window.minsize(width=300, height=300)
window.config(bg=PINK, pady=80, padx=100)
# local
label = Label(text='Enter path for image', bg=PINK, fg='white')
label.grid(row=0, column=0)

c1 = Checkbutton(text='local', bg=PINK, fg='white', onvalue=2, command=set_type_local)
c1.grid(row=1, column=0)

c2 = Checkbutton(text='url', bg=PINK, fg='white', onvalue=1, command=set_type_url)
c2.grid(row=2, column=0)

input = Entry(width=20, bg=PINK, fg='white')
input.grid(row=3, column=0, pady=5)

button = Button(text="Watermark", highlightthickness=0, bg=PINK, fg=PINK, borderwidth=0, command=watermark)
button.grid(column=0, row=4)


window.mainloop()
