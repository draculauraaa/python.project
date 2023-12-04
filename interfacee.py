import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter  import messagebox
from tkinter import ttk
from tkinter import StringVar


window =tk.Tk()
window.geometry('500x600')
window.title('Unit Converter')
window.configure(bg = 'pink')


font1 = font.Font(family = 'verdana',size = '30', weight = 'bold')
font2 = font.Font(family = 'verdana',size = '15')
font3 = font.Font(family = 'verdana',size = '20')

number_from=StringVar()

def selected(event):
    unit=event.widget.get()
    if unit == 'Volume':
        fromdd['values']= ('cubic metere',
                           'cubic centimetere',
                           'cubic millimetre',
                           'cubic kilometere',
                           'cubic decimetre',
                           'millilitre',
                           'litre',
                           'cubic foot',
                           'gallon'
                           )
        todd['values'] = ('cubic metere',
                            'cubic centimetere',
                            'cubic millimetre',
                            'cubic kilometere',
                            'cubic decimetre',
                          'millilitre',
                            'litre',
                            'cubic foot',
                            'gallon'
                            )
    elif unit == 'Lenght':
        fromdd['values'] = ( 'metere',
                            'centimetere',
                            'millimetre',
                            'kilometere',
                            'decimetre',
                             'micrometer',
                            'inch',
                            'foot',
                            'mile',
                             'yard'
                            )
        todd['values'] = ('metere',
                            'centimetere',
                            'millimetre',
                            'kilometere',
                            'decimetre',
                            'micrometer',
                            'inch',
                            'foot',
                            'mile',
                            'yard'
                            )
    elif unit == 'Area':
        fromdd['values'] = ('square metere',
                            'square centimetere',
                            'square millimetre',
                            'square kilometere',
                            'square decimetre',
                            'square micrometer',
                            'square inch',
                            'square foot',
                            'square mile',
                            'square yard',
                            'hectare',
                            'are'
                            )
        todd['values'] = ('square metere',
                            'square centimetere',
                            'square millimetre',
                            'square kilometere',
                            'square decimetre',
                            'square micrometer',
                            'square inch',
                            'square foot',
                            'square mile',
                            'square yard',
                            'hectare',
                            'are'
                            )
    elif unit == 'Mass':
        fromdd['values'] = ('tonne',
                            'kilogram',
                            'gram',
                            'milligram',
                            'microgram',
                            'kilotonne',
                            'pound'
                            )
        todd['values'] = ('tonne',
                            'kilogram',
                            'gram',
                            'milligram',
                            'microgram',
                            'kilotonne',
                            'pound'
                            )
def fromfunc(event):
    global result_from
    result_from=event.widget.get()


def tofunc(event):
    global result_to
    result_to=event.widget.get()


def answer():
    pass



main = tk.Label(window,text = 'Unit Converter',bg='pink')
main['font'] = font1
main.place(relx = '0.5',rely = '0.1',anchor = 'center')

unit = tk.Label(window, text = 'Unit:',bg = 'pink')
unit ['font']=font2
unit.place(relx='0.2',rely='0.305',anchor='center')

n = StringVar()
unitdd=ttk.Combobox(window,width='35',textvariable=n)

unitdd['values']=('Lenght','Area','Volume','Mass')
unitdd.place(relx='0.5',rely='0.31',anchor='center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

label_from=tk.Label(window,text='From:',bg='pink')
label_from['font']=font2
label_from.place(relx='0.2',rely='0.395',anchor='center')

f=StringVar()
fromdd=ttk.Combobox(window,width='35', textvariable=f)
fromdd.place(relx='0.5',rely='0.4',anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

num_from=tk.Entry(window,width=10,textvariable=number_from)
num_from.place(relx='0.5',rely='0.55',anchor='center')

answer = partial(answer,num_from)

to = tk.Label(window,text='To:',bg='pink')
to['font']=font2
to.place(relx='0.2',rely='0.475',anchor='center')
t=StringVar()
todd=ttk.Combobox(window,width='35',textvariable=t)
todd.place(relx='0.5',rely='0.48', anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

result = tk.Label(window,text='',bg='white',width=20)
result['font']=font3
result.place (relx='0.5',rely='0.65',anchor='center')

get_answer = tk.Button(window,text='generate answer',bg='red',fg='white',command=answer)
get_answer['font']=font2
get_answer.place(relx='0.5',rely='0.8',anchor='center')


window.mainloop()


