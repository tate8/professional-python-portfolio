from essential_generators import DocumentGenerator
from tkinter import *
import time

gen = DocumentGenerator()

random_text = ''
char_typed = 0
errors = 0
start_time = None
end_time = None
GREEN = 'green'


def check_text(event):
  text = text_label.cget('text')
  input = T.get('1.0', 'end-1c')
  input = input[:-1]
  if input == text:
    # right
    global char_typed, end_time
    end_time = time.time()
    time_taken = int(end_time - start_time)
    cps = char_typed / time_taken
    label.config(text=f'Typing speed: {int(cps*(60/5))} WPM \nAccuracy: {int(((char_typed - errors) / char_typed)*100)}%')
    T.delete('1.0', END)
  else:
    # wrong
    label.config(text='Oops!')


def generate_text():
    T.delete('1.0', END)
    global random_text, char_typed
    char_typed = 0
    random_text = gen.sentence()
    text_label.config(text=random_text)
    label.config(text='Start typing')


def key_pressed(event):
    t = text_label.cget('text')
    i = T.get('1.0', 'end-1c')
    text = t[0:len(i)]
    # get start time when first character is there
    if len(i) == 1 :
      global start_time
      start_time = time.time()
    # check if its wrong
    if i != text:
      if event.keysym == 'BackSpace':
        pass
      else:
        global errors
        T.config(fg='red')
        
        errors += 1
        print('error')
    else:
      T.config(fg='white')
    if event.char == ' ':
        pass
    else:
        global char_typed
        char_typed += 1


root = Tk()
root.config(bg=GREEN, padx=10)
# if key pressed, excecute key_pressed()
root.bind('<Return>', check_text)
root.bind('<Key>', key_pressed)

label = Label(text='Start typing', bg=GREEN, fg='white', font=('Arial', 24))
label.pack()
# make random text @ start
random_text = gen.sentence()
text_label = Label(text=random_text, bg=GREEN, fg='white', font=('Consolas', 12))
text_label.pack()


again = Button(text='again?', bg=GREEN, command=generate_text)
again.pack(side=BOTTOM)

# scrollbar and text
S = Scrollbar(root)
T = Text(root, height=4, width=60, bg=GREEN, fg='white')
T.focus_set()
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)



mainloop()






