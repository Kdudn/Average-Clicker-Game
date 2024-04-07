import tkinter as tk
from tkinter import ttk
import ast

#it saves!!1

make_windows = False

root = tk.Tk()
root.resizable(False, False)
root.title("Average Clicker Game")

with open('save.txt', 'r') as file:
	data = int(file.read())

with open('cps.txt', 'r') as file:
	cps = int(file.read())

with open('save-upgrades.txt', 'r') as file:
	upgrades = ast.literal_eval(file.read())

rows_for_upgrades = 1
clicked = False

if data > 0:
	clicks = data
else:
	clicks = 0

def make_msg(msg):
	global root
	if make_windows == True:	
		new_win = tk.Tk()
		new_win.title(str(msg))
		tk.Label(new_win, font=('', 16), text=str(msg)).pack()
	else:
		root.title(str(msg))

#make_msg("Please Click 🥺 👉👈")

def click():
	global clicks, text_label, root, clicked
	if clicked == False:
		make_msg("You Clicked!")
		clicked = True
	clicks += 1
	text_label = tk.Label(root, font=('', 16), text=f"Clicks: " + '{:,}'.format(clicks))
	text_label.grid(column=0, row=0)
	with open('save.txt', 'w') as file:
		file.write(str(clicks))

def upgrades_cps():
	global clicks, text_label, root
	clicks += cps
	text_label = tk.Label(root, font=('', 16), text=f"Clicks: " + '{:,}'.format(clicks))
	text_label.grid(column=0, row=0)
	tk.Label(root, font=('', 16), text=f"CPS: " + '{:,}'.format(cps)).grid(column=1, row=0)
	with open('save.txt', 'w') as file:
		file.write(str(clicks))
	with open('cps.txt', 'w') as file:
		file.write(str(cps))
	root.after(1000, upgrades_cps)

upgrades_cps()

def upgrade_price_cps(index_of_item):
	global clicks, text_label, root, cps, clicked, rows_for_upgrades
	rows_for_upgrades = 1
	if clicks >= upgrades[index_of_item][2]:
		clicks -= upgrades[index_of_item][2]
		cps += upgrades[index_of_item][1]
		with open('cps.txt', 'w') as file:
			file.write(str(cps))
		make_msg(f"You bought a {upgrades[index_of_item][0]}  -{upgrades[index_of_item][2]}")
		upgrades[index_of_item][2] = round(upgrades[index_of_item][2] * 1.25)
		for i in range(len(upgrades)):
			rows_for_upgrades += 1
			tk.Label(root, font=('', 12), text=f'{upgrades[i][0]}, CPS: '+ '{:,}'.format(upgrades[i][1]) + ', Price: ' + '{:,}'.format(upgrades[i][2])).grid(row=rows_for_upgrades, column=1)
		with open('save-upgrades.txt', 'w') as file:
			file.write(str(upgrades))
	else:
		make_msg("Insuffecient funds")

text_label = tk.Label(root, font=('', 16), text=f"Clicks: " + '{:,}'.format(clicks))
add_button = tk.Button(root, font=('', 12), text="Click me!", command=click)

for i in range(len(upgrades)):
	rows_for_upgrades += 1
	tk.Label(root, font=('', 12), text=f'{upgrades[i][0]}, CPS: '+ '{:,}'.format(upgrades[i][1]) + ', Price: ' + '{:,}'.format(upgrades[i][2])).grid(row=rows_for_upgrades, column=1)

autoclicker_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(0)).grid(row=2)
mouse_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(1)).grid(row=3)
keyboard_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(2)).grid(row=4)
computer_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(3)).grid(row=5)
programmer_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(4)).grid(row=6)
website_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(5)).grid(row=7)
franchise_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(6)).grid(row=8)
company_buy = tk.Button(root, font=('', 12), text="Buy", command=lambda:upgrade_price_cps(7)).grid(row=9)

text_label.grid(column=0, row=0)
add_button.grid(column=0, row=1)

root.mainloop()

#notes
#YIPEE