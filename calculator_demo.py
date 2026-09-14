from tkinter import *

def press(num):
    global eqn_txt
    eqn_txt = eqn_txt + str(num)
    eqn_label.set(eqn_txt)

def calc():
    global eqn_txt
    try:
        total = str(eval(eqn_txt))
        eqn_label.set(total)
        eqn_txt = total
    except SyntaxError:
        eqn_label.set('!!!SYNTAX ERROR!!!')
        eqn_txt = ''
    except ZeroDivisionError:
        eqn_label.set('!!!ARITHMETIC ERROR!!!')
        eqn_txt = ''

def clear():
    global eqn_txt
    eqn_label.set('')
    eqn_txt = ''

def delete():
    global eqn_txt
    eqn_txt = eqn_txt[:-1]
    eqn_label.set(eqn_txt)

window = Tk()
window.title('CALCULATOR')

# Note: Ensure 'apple-calculator.png' is in the same directory, 
# or comment out iconphoto if you don't have the asset handy.
try:
    pic = PhotoImage(file='apple-calculator.png')
    window.iconphoto(True, pic)
except Exception:
    pass

window.config(background='#262626')
window.geometry('400x500')
window.minsize(400, 500)
window.maxsize(400, 500)

eqn_txt = ''
eqn_label = StringVar()

label = Label(window, textvariable=eqn_label, relief=RAISED, font=('Sans Serif', 20, 'bold'), fg='#FFFFFF', bg='#858585', height=2, width=20)
label.grid(row=0, column=0, columnspan=4, pady=20, padx=25)

frame = Frame(window, bg='#262626')
frame.grid(row=1, column=0, columnspan=4, padx=25)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('DEL', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('+', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('*', 3, 3),
    ('CLR', 4, 0), ('(', 4, 1), (')', 4, 2), ('/', 4, 3)
]

for text, row, column in buttons:
    action = calc if text == '=' else delete if text == 'DEL' else clear if text == 'CLR' else lambda t=text: press(t)
    
    # Give the equals button a distinct highlight color
    bg_color = '#FF5733' if text == '=' else '#424242'
    active_bg = '#FF8F66' if text == '=' else '#7a7979'
    
    Button(frame, text=text, height=2, width=6, font=('Sans Serif', 15, 'bold'), 
           fg='#FFFFFF', bg=bg_color, activebackground=active_bg, command=action
          ).grid(row=row, column=column, padx=2, pady=2)

window.mainloop()