from tkinter import *
from buttons import Buttons
import  random
import time
import datetime


root = Tk()
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# 0+0 para ocupar toda a tela
root.geometry("{}x{}+0+0".format(screen_width,screen_height))
root.title("Sitema de Vedas")
root.configure(background="blue")

# Frames primáiros
# Frame widget which may contain other widgets and can have a 3D border.
topo = Frame(root,width=screen_width, height=screen_height/6, bd=4, relief="raise")
topo.pack(side=TOP)

f_left1_height = screen_height
f_left1_right=screen_width*(3/4)
f_left1 = Frame(root, width=f_left1_right, height=f_left1_height, bd=3, relief="raise", bg="grey")
f_left1.pack(side=LEFT)

f_right1_width = screen_width/4
f_right1_height = f_left1_height
f_right1 = Frame(root, width=f_right1_width, height=f_right1_height, bd=3, relief="raise")
f_right1.pack(side=RIGHT)

lbl_topo = Label(topo, font=("arial", 50, "bold"), text="Sistema de Cafeteria", width="40")
lbl_topo.grid(row=0, column=0)

# Frames secundários: Frame Left
f_left1_interno1_height = f_left1_height*(5/6)
f_left1_interno3 = Frame(f_left1, width=f_left1_right, height=f_left1_interno1_height/5, bd=2, relief="raise", bg="grey")
f_left1_interno3.pack(side=BOTTOM)

f_left1_interno1 = Frame(f_left1, width=f_left1_right/2, height=f_left1_interno1_height, bd=2, relief="raise", bg="grey")
f_left1_interno1.pack(side=LEFT)

f_left1_interno2 = Frame(f_left1, width=f_left1_right/2, height=f_left1_interno1_height, bd=2, relief="raise", bg="grey")
f_left1_interno2.pack(side=RIGHT)

# Frames secundários: Frame RIGHT

f_right1_interno_top = Frame(f_right1, width=f_right1_width, height=f_right1_height*(2/3), bd=2, relief="raise", bg="grey")
f_right1_interno_top.pack(side=TOP)

f_right1_interno_bot = Frame(f_right1, width=f_right1_width, height=f_right1_height/3, bd=2, relief="raise", bg="grey")
f_right1_interno_bot.pack(side=BOTTOM)


# Variaveis cafés para raised buttons

var_cafe1 = IntVar().set("0")
var_cafe2 = IntVar().set("0")
var_cafe3 = IntVar().set("0")
var_cafe4 = IntVar().set("0")
var_cafe5 = IntVar().set("0")
var_cafe6 = IntVar().set("0")
var_cafe7 = IntVar().set("0")
var_cafe8 = IntVar().set("0")

# Variaveis bolos para raised buttons

var_bolo1 = IntVar().set("0")
var_bolo2 = IntVar().set("0")
var_bolo3 = IntVar().set("0")
var_bolo4 = IntVar().set("0")
var_bolo5 = IntVar().set("0")
var_bolo6 = IntVar().set("0")
var_bolo7 = IntVar().set("0")
var_bolo8 = IntVar().set("0")


# Criando Radio Buttons Para Cafés

latte = Buttons().raised_button(f_left1_interno1, var_cafe1, "Latte \t\t", 0)
expresso = Buttons().raised_button(f_left1_interno1, var_cafe2,"Expresso \t",1,"gray")
iced_latte = Buttons().raised_button(f_left1_interno1, var_cafe3,"Iced Latte \t",2)
coffe_cropped = Buttons().raised_button(f_left1_interno1, var_cafe4,"Cropped Coffe \t",3,"gray")
milk_coffe = Buttons().raised_button(f_left1_interno1, var_cafe5,"Milk & Coffe \t",4)
black_coffe = Buttons().raised_button(f_left1_interno1, var_cafe6,"Black Coffe \t",5,"gray")
cream_coffe = Buttons().raised_button(f_left1_interno1, var_cafe7,"Cream Coffe \t",6)
cappuccino = Buttons().raised_button(f_left1_interno1, var_cafe8,"Cappuccino \t",7,"gray")



# Criando Radio Buttons Para Bolos

lamon_cake = Buttons().raised_button(f_left1_interno2, var_bolo1, "Lamon Cake \t", 0)
corn_cake = Buttons().raised_button(f_left1_interno2, var_bolo2,"Corn Cake \t",1,"gray")
strawberry_cake = Buttons().raised_button(f_left1_interno2, var_bolo3,"Strawberry Cake \t",2)
chocolate_pie = Buttons().raised_button(f_left1_interno2, var_bolo4,"Chocolate Pie \t",3,"gray")
lemon_pie = Buttons().raised_button(f_left1_interno2, var_bolo5,"Lemon Pie \t",4)
chocolate_cake = Buttons().raised_button(f_left1_interno2, var_bolo6,"Chocolate Cake \t",5,"gray")
carrot_cake = Buttons().raised_button(f_left1_interno2, var_bolo7,"Carrot Cake \t",6)
pudding = Buttons().raised_button(f_left1_interno2, var_bolo8,"Pudding \t",7,"gray")


# Butões para escolher quantidade: Cafés

latte_amout = Buttons().buttons_amount(f_left1_interno1, 0)
iced_latte_amout = Buttons().buttons_amount(f_left1_interno1, 1)
expresso_amount = Buttons().buttons_amount(f_left1_interno1, 2)
coffe_cropped_amount = Buttons().buttons_amount(f_left1_interno1, 3)
milk_coffe_amount = Buttons().buttons_amount(f_left1_interno1, 4)
black_coffe_amount = Buttons().buttons_amount(f_left1_interno1, 5)
cream_coffe_amount = Buttons().buttons_amount(f_left1_interno1, 6)
cappuccino_amount = Buttons().buttons_amount(f_left1_interno1, 7)

# Butões para escolher quantidade: Bolos

lamon_cake_amout = Buttons().buttons_amount(f_left1_interno2, 0)
corn_cake_amount = Buttons().buttons_amount(f_left1_interno2, 1)
strawberry_cake_amount = Buttons().buttons_amount(f_left1_interno2, 2)
chocolate_pie_amount = Buttons().buttons_amount(f_left1_interno2, 3)
lemon_pie_amount = Buttons().buttons_amount(f_left1_interno2, 4)
chocolate_cake_amount = Buttons().buttons_amount(f_left1_interno2, 5)
carrot_cake_amount = Buttons().buttons_amount(f_left1_interno2, 6)
pudding_amount = Buttons().buttons_amount(f_left1_interno2, 7)


# Campos do recibo

lbl_recibo = Label(f_right1_interno_top, font=("arial", 12, "bold"), text= "Recibo : ", bd=2, anchor=W, bg="gray").grid(row=0, column=0, sticky=W)
txt_recibo = Text(f_right1_interno_top, width=50, height=22, bd=2, bg="lemonchiffon", font=("arial",11, "bold")).grid(row=1, column=0)

# Botões Recibo
btn_total = Button(f_right1_interno_bot, width=10, height=1, text="Total").grid(row=0, column=0)
btn_recibo = Button(f_right1_interno_bot, width=10, height=1, text="Recibo").grid(row=0, column=1)
btn_limpar = Button(f_right1_interno_bot, width=10, height=1, text="Limpar").grid(row=0, column=2)


# acima daqui será executado. abaixo será ignorado
root.mainloop()
#print(help(Frame))