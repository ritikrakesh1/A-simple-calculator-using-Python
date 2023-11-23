import tkinter as tk
import tkinter.ttk as tkk

root = tk.Tk()
root.title('Calculator')
root.geometry('280x260')
root.config(bg="#dcdcdc")


calculation_str = ''
error_str = 'Error'

x = 7
y = 5
width = 20
font = ('Arial', 18)

label = tkk.Label(root, text = calculation_str, width = width, font = font)
label.place(x = x, y = y)


def add_a_char(element):
    global calculation_str
    if calculation_str == error_str:
        calculation_str = element
    else:
        calculation_str += element
    label = tkk.Label(root, text = calculation_str, width = width, font = font)
    label.place(x =x, y =y)


button_9 = tkk.Button(root, text = '9', command = lambda: add_a_char('9')).place(x = 5,y= 45)

button_6 = tkk.Button(root, text = '6', command = lambda: add_a_char('6')).place(x = 5,y= 75)

button_3 = tkk.Button(root, text = '3', command = lambda: add_a_char('3')).place(x = 5,y= 105)

button_0 = tkk.Button(root, text = '0', command = lambda: add_a_char('0')).place(x = 5,y= 135)

button_8 = tkk.Button(root, text = '8', command = lambda: add_a_char('8')).place(x = 100,y= 45)

button_5 = tkk.Button(root, text = '5', command = lambda: add_a_char('5')).place(x = 100,y= 75)

button_2 = tkk.Button(root, text = '2', command = lambda: add_a_char('2')).place(x = 100,y= 105)

button_open_bracket = tkk.Button(root, text = '(', command = lambda: add_a_char('(')).place(x = 100,y= 135)

button_7 = tkk.Button(root, text = '7', command = lambda: add_a_char('7')).place(x = 195,y= 45)

button_4 = tkk.Button(root, text = '4', command = lambda: add_a_char('4')).place(x = 195,y= 75)

button_1 = tkk.Button(root, text = '1', command = lambda: add_a_char('1')).place(x = 195,y= 105)

button_close_bracket = tkk.Button(root, text = ')', command = lambda: add_a_char(')')).place(x = 195,y= 135)


def do_cal(operation):
    global calculation_str
    if calculation_str == error_str:
        calculation_str = ''
    elif calculation_str == '':
        calculation_str = ''
    else:
        calculation_str += operation
    label = tkk.Label(root, text = calculation_str, width = width, font = font)
    label.place(x =x, y =y)


button_plus = tkk.Button(root, text = '+', command = lambda: do_cal('+')).place(x = 5,y= 165)

button_minus = tkk.Button(root, text = '-', command = lambda: do_cal('-')).place(x = 5,y= 195)

button_divide = tkk.Button(root, text = '/', command = lambda: do_cal('/')).place(x = 100,y= 165)

button_multiply = tkk.Button(root, text = '*', command = lambda: do_cal('*')).place(x = 100,y= 195)

button_floor_division = tkk.Button(root, text = '//', command = lambda: do_cal('//')).place(x = 5,y= 225)

button_modulo = tkk.Button(root, text = '%', command = lambda: do_cal('%')).place(x = 100,y= 225)



def backspace():
    global calculation_str
    calculation_str = calculation_str[:len(calculation_str)-1]
    label = tkk.Label(root, text = calculation_str, width = width, font = font)
    label.place(x =x, y = y)

button_backspace = tkk.Button(root, text = 'Backspace', command = backspace).place(x = 195,y= 165)


def calculate():
    global calculation_str
    try:
        calculation_str = str(round(eval(calculation_str),2))
    except:
        calculation_str = error_str
    label = tkk.Label(root, text = calculation_str, width = width, font = font)
    label.place(x =x, y = y)

button_calculate = tkk.Button(root, text = 'Calculate', command = calculate).place(x = 195,y= 195)


def clear():
    global calculation_str
    calculation_str = ''
    label = tkk.Label(root, text = calculation_str, width = width, font = font)
    label.place(x =x, y = y)

button_clear = tkk.Button(root, text = 'Clear', command = clear).place(x = 195,y= 225)


root.mainloop()