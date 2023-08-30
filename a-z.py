from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry('600x300')
tk.title('Alphabet')

count= 0
caps = False
word = ''

# функция за del
def del_btn():
    global word
    if word != '':
        word = word[:-1]
        btn_res['text']=word
        
#функция за капс
def caps_btn():
    global count
    global caps
    
    if count == 0:
        count = 1
        caps = True
    elif count == 1:
        caps = False
        count = 0

# функции за буквы
def lit_1_btn():
    global word
    global caps

    if caps == False:
        word += 'а'
        btn_res['text']=word
    elif caps == True:
        word += 'А'
        btn_res['text']=word

def lit_2_btn():
    global word
    global caps

    if caps == False:
        word += 'б'
        btn_res['text']=word
    elif caps == True:
        word += 'Б'
        btn_res['text']=word

def lit_3_btn():
    global word
    global caps

    if caps == False:
        word += 'в'
        btn_res['text']=word
    elif caps == True:
        word += 'В'
        btn_res['text']=word

def lit_4_btn():
    global word
    global caps

    if caps == False:
        word += 'г'
        btn_res['text']=word
    elif caps == True:
        word += 'Г'
        btn_res['text']=word

def lit_5_btn():
    global word
    global caps

    if caps == False:
        word += 'д'
        btn_res['text']=word
    elif caps == True:
        word += 'Д'
        btn_res['text']=word

def lit_6_btn():
    global word
    global caps

    if caps == False:
        word += 'е'
        btn_res['text']=word
    elif caps == True:
        word += 'Е'
        btn_res['text']=word

def lit_7_btn():
    global word
    global caps

    if caps == False:
        word += 'ё'
        btn_res['text']=word
    elif caps == True:
        word += 'Ё'
        btn_res['text']=word

def lit_8_btn():
    global word
    global caps

    if caps == False:
        word += 'ж'
        btn_res['text']=word
    elif caps == True:
        word += 'Ж'
        btn_res['text']=word

def lit_9_btn():
    global word
    global caps

    if caps == False:
        word += 'з'
        btn_res['text']=word
    elif caps == True:
        word += 'З'
        btn_res['text']=word

def lit_10_btn():
    global word
    global caps

    if caps == False:
        word += 'и'
        btn_res['text']=word
    elif caps == True:
        word += 'И'
        btn_res['text']=word

def lit_11_btn():
    global word
    global caps

    if caps == False:
        word += 'й'
        btn_res['text']=word
    elif caps == True:
        word += 'Й'
        btn_res['text']=word

def lit_12_btn():
    global word
    global caps

    if caps == False:
        word += 'к'
        btn_res['text']=word
    elif caps == True:
        word += 'К'
        btn_res['text']=word

def lit_13_btn():
    global word
    global caps

    if caps == False:
        word += 'л'
        btn_res['text']=word
    elif caps == True:
        word += 'Л'
        btn_res['text']=word

def lit_14_btn():
    global word
    global caps

    if caps == False:
        word += 'м'
        btn_res['text']=word
    elif caps == True:
        word += 'М'
        btn_res['text']=word

def lit_15_btn():
    global word
    global caps

    if caps == False:
        word += 'н'
        btn_res['text']=word
    elif caps == True:
        word += 'Н'
        btn_res['text']=word

def lit_16_btn():
    global word
    global caps

    if caps == False:
        word += 'о'
        btn_res['text']=word
    elif caps == True:
        word += 'О'
        btn_res['text']=word

def lit_17_btn():
    global word
    global caps

    if caps == False:
        word += 'п'
        btn_res['text']=word
    elif caps == True:
        word += 'П'
        btn_res['text']=word

def lit_18_btn():
    global word
    global caps

    if caps == False:
        word += 'р'
        btn_res['text']=word
    elif caps == True:
        word += 'Р'
        btn_res['text']=word

def lit_19_btn():
    global word
    global caps

    if caps == False:
        word += 'с'
        btn_res['text']=word
    elif caps == True:
        word += 'С'
        btn_res['text']=word

def lit_20_btn():
    global word
    global caps

    if caps == False:
        word += 'у'
        btn_res['text']=word
    elif caps == True:
        word += 'У'
        btn_res['text']=word

def lit_21_btn():
    global word
    global caps

    if caps == False:
        word += 'у'
        btn_res['text']=word
    elif caps == True:
        word += 'У'
        btn_res['text']=word

def lit_22_btn():
    global word
    global caps

    if caps == False:
        word += 'ф'
        btn_res['text']=word
    elif caps == True:
        word += 'Ф'
        btn_res['text']=word

def lit_23_btn():
    global word
    global caps

    if caps == False:
        word += 'х'
        btn_res['text']=word
    elif caps == True:
        word += 'Х'
        btn_res['text']=word

def lit_24_btn():
    global word
    global caps

    if caps == False:
        word += 'ц'
        btn_res['text']=word
    elif caps == True:
        word += 'Ц'
        btn_res['text']=word

def lit_25_btn():
    global word
    global caps

    if caps == False:
        word += 'ч'
        btn_res['text']=word
    elif caps == True:
        word += 'Ч'
        btn_res['text']=word

def lit_26_btn():
    global word
    global caps

    if caps == False:
        word += 'ш'
        btn_res['text']=word
    elif caps == True:
        word += 'Ш'
        btn_res['text']=word

def lit_27_btn():
    global word
    global caps

    if caps == False:
        word += 'щ'
        btn_res['text']=word
    elif caps == True:
        word += 'Щ'
        btn_res['text']=word

def lit_28_btn():
    global word
    global caps

    if caps == False:
        word += 'ъ'
        btn_res['text']=word
    elif caps == True:
        word += 'Ъ'
        btn_res['text']=word

def lit_29_btn():
    global word
    global caps

    if caps == False:
        word += 'ы'
        btn_res['text']=word
    elif caps == True:
        word += 'Ы'
        btn_res['text']=word

def lit_30_btn():
    global word
    global caps

    if caps == False:
        word += 'ь'
        btn_res['text']=word
    elif caps == True:
        word += 'Ь'
        btn_res['text']=word

def lit_31_btn():
    global word
    global caps

    if caps == False:
        word += 'э'
        btn_res['text']=word
    elif caps == True:
        word += 'Э'
        btn_res['text']=word

def lit_32_btn():
    global word
    global caps

    if caps == False:
        word += 'ю'
        btn_res['text']=word
    elif caps == True:
        word += 'Ю'
        btn_res['text']=word

def lit_33_btn():
    global word
    global caps

    if caps == False:
        word += 'я'
        btn_res['text']=word
    elif caps == True:
        word += 'Я'
        btn_res['text']=word

# функция за пробел
def space_btn():
    global word
    word += ' '

# выводится экран
btn_res = ttk.Button(text='', )
btn_res.pack(fill=X)

# delete 
btn_del = ttk.Button(text='Delete', command=del_btn)
btn_del.place(relx=0.87,rely=0.08)

#caps lock
btn_caps = ttk.Button(text='Caps Lock', command=caps_btn)
btn_caps.place(relx=0,rely=0.08)

# алфавит
btn_1_lit = ttk.Button(text='A', command=lit_1_btn)
btn_1_lit.place(relx=0, rely=0.5)

btn_2_lit = ttk.Button(text='Б', command=lit_2_btn)
btn_2_lit.place(relx =0.12, rely=0.5)

btn_3_lit = ttk.Button(text='В', command=lit_3_btn)
btn_3_lit.place(relx =0.24, rely=0.5)

btn_4_lit = ttk.Button(text='Г', command=lit_4_btn)
btn_4_lit.place(relx =0.35, rely=0.5)

btn_5_lit = ttk.Button(text='Д', command=lit_5_btn)
btn_5_lit.place(relx =0.46, rely=0.5)

btn_6_lit = ttk.Button(text='Е', command=lit_6_btn)
btn_6_lit.place(relx =0.57, rely=0.5)

btn_7_lit = ttk.Button(text='Ё', command=lit_7_btn)
btn_7_lit.place(relx =0.68, rely=0.5)

btn_8_lit = ttk.Button(text='Ж', command=lit_8_btn)
btn_8_lit.place(relx =0.79, rely=0.5)

btn_9_lit = ttk.Button(text='З', command=lit_9_btn)
btn_9_lit.place(relx =0.90, rely=0.5) 

# верхния стоока 0,5
btn_10_lit = ttk.Button(text='И', command=lit_10_btn)
btn_10_lit.place(relx =0, rely=0.6)

btn_11_lit = ttk.Button(text='Й', command=lit_11_btn)
btn_11_lit.place(relx =0.12, rely=0.6)

btn_12_lit = ttk.Button(text='К', command=lit_12_btn)
btn_12_lit.place(relx =0.24, rely=0.6)

btn_13_lit = ttk.Button(text='Л', command=lit_13_btn)
btn_13_lit.place(relx =0.35, rely=0.6)

btn_14_lit = ttk.Button(text='М', command=lit_14_btn)
btn_14_lit.place(relx =0.46, rely=0.6)

btn_15_lit = ttk.Button(text='Н', command=lit_15_btn)
btn_15_lit.place(relx =0.57, rely=0.6)

btn_16_lit = ttk.Button(text='О', command=lit_16_btn)
btn_16_lit.place(relx =0.68, rely=0.6)

btn_17_lit = ttk.Button(text='П', command=lit_17_btn)
btn_17_lit.place(relx =0.79, rely=0.6)

btn_18_lit = ttk.Button(text='Р', command=lit_18_btn)
btn_18_lit.place(relx =0.9, rely=0.6)

# cтрока 0,6
btn_19_lit = ttk.Button(text='С', command=lit_19_btn)
btn_19_lit.place(relx =0, rely=0.7)

btn_20_lit = ttk.Button(text='Т', command=lit_20_btn)
btn_20_lit.place(relx =0.12, rely=0.7)

btn_21_lit = ttk.Button(text='У', command=lit_21_btn)
btn_21_lit.place(relx =0.24, rely=0.7)

btn_22_lit = ttk.Button(text='Ф', command=lit_22_btn)
btn_22_lit.place(relx =0.35, rely=0.7)

btn_23_lit = ttk.Button(text='Х', command=lit_23_btn)
btn_23_lit.place(relx =0.46, rely=0.7)

btn_24_lit = ttk.Button(text='Ц', command=lit_24_btn)
btn_24_lit.place(relx =0.57, rely=0.7)

btn_25_lit = ttk.Button(text='Ч', command=lit_25_btn)
btn_25_lit.place(relx =0.68, rely=0.7)

btn_26_lit = ttk.Button(text='Ш', command=lit_26_btn)
btn_26_lit.place(relx =0.79, rely=0.7)

btn_27_lit = ttk.Button(text='Щ', command=lit_27_btn)
btn_27_lit.place(relx =0.9, rely=0.7)

# строка 0,7
btn_28_lit = ttk.Button(text='Ъ', command=lit_28_btn)
btn_28_lit.place(relx =0, rely=0.8)

btn_29_lit = ttk.Button(text='Ы', command=lit_29_btn)
btn_29_lit.place(relx =0.12, rely=0.8)

btn_30_lit = ttk.Button(text='Ь', command=lit_30_btn)
btn_30_lit.place(relx =0.24, rely=0.8)

btn_31_lit = ttk.Button(text='Э', command=lit_31_btn)
btn_31_lit.place(relx =0.68, rely=0.8)

btn_32_lit = ttk.Button(text='Ю', command=lit_32_btn)
btn_32_lit.place(relx =0.79, rely=0.8)

btn_33_lit = ttk.Button(text='Я', command=lit_33_btn)
btn_33_lit.place(relx =0.9, rely=0.8)

btn_space = ttk.Button(text='                        Space                                  ', command=space_btn)
btn_space.place(relx=0.35,rely=0.8)

tk.mainloop()