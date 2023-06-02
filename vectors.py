#Vectors calculator by: CABUNGCAL, PAGULAYAN AND DELA CRUZ S12-A
from tkinter import *

root = Tk()
root.title("Vectors Calculator")
import math
#row
r = 0
#sums
xsum = 0
ysum = 0
forget = 0
row_list = []

#defines
def compute():
	global r
	global xsum
	global ysum
	global res_lab
	global ysum_lab
	global xsum_lab
	global summation_lab
	global resultant_lab
	global direction_lab
	global dirnum_lab
	global forget
	force.focus_set()
	force_val = float(force.get())
	direction_val = direction.get().upper()
	degree_val = float(degree.get())
	force.delete(0, "end")
	direction.delete(0, "end")
	degree.delete(0, "end")
	#x components and y components
	if direction_val == "W":
		xcomp = -(abs(force_val))
		ycomp = 0
	elif direction_val == "S":
		xcomp = 0
		ycomp = -(abs(force_val))
	elif direction_val == "N":
		xcomp = 0
		ycomp = abs(force_val)
	elif direction_val == "E":
		xcomp = abs(force_val)
		ycomp = 0
	elif direction_val == "W OF N" or direction_val == "E OF N" or direction_val == "E OF S" or direction_val == "W OF S":
		xcomp = force_val * math.sin(math.radians(degree_val))
		ycomp = force_val * math.cos(math.radians(degree_val))
	else:
		xcomp = force_val * math.cos(math.radians(degree_val))
		ycomp = force_val * math.sin(math.radians(degree_val))
	#directionvariety
	if direction_val == "N OF W" or direction_val == "W OF N":
		xcomp = -(abs(xcomp))
		ycomp = abs(ycomp)
	elif direction_val == "N OF E" or direction_val == "E OF N":
		xcomp = abs(xcomp)
		ycomp = abs(ycomp)
	elif direction_val == "S OF E" or direction_val == "E OF S":
		xcomp = abs(xcomp)
		ycomp = -(abs(ycomp))
	elif direction_val == "S OF W" or direction_val == "W OF S":
		xcomp = -(abs(xcomp))
		ycomp = -(abs(ycomp))
	#xsums and ysums
	if xsum == 0:
		xsum = float(xcomp)
	else:
		xsum = xsum + xcomp
	if ysum == 0:
		ysum = float(ycomp)
	else:
		ysum = ysum + ycomp
	#resultant
	res = math.sqrt((xsum) ** 2 + (ysum) ** 2)
	#direction value
	if xsum == 0 or ysum == 0:
		dirnum = 0
	else:
		dirnum = abs(round(math.degrees(math.atan(ysum/xsum)),2))
	#vector direction
	if xsum > 0 and ysum > 0:
		direction_vec = " N OF E"
	elif xsum < 0 and ysum > 0:
		direction_vec = " N OF W"
	elif xsum < 0 and ysum < 0:
		direction_vec = " S OF W"
	elif xsum >  0 and ysum < 0:
		direction_vec = " S OF E"
	elif xsum == 0 and ysum < 0:
		direction_vec = " S"
	elif xsum == 0 and ysum > 0:
		direction_vec = " N"
	elif xsum > 0 and ysum == 0:
		direction_vec = " E"
	elif xsum < 0 and ysum == 0:
		direction_vec = " W"
	elif xsum == 0 and ysum == 0:
		direction_vec = " "
	#printing outputs 
	if r == 0:
		r = 1
	#forget
	if forget == 1:
		res_lab.grid_forget()
		xsum_lab.grid_forget()
		ysum_lab.grid_forget()
		summation_lab.grid_forget()
		resultant_lab.grid_forget()
		direction_lab.grid_forget()
		dirnum_lab.grid_forget()
	#outputslabs
	force_lab = Label(root, text=float(force_val)).grid(row=r, column=4)
	direction1_lab = Label(root, text=direction_val).grid(row=r, column=5)
	degree_lab = Label(root, text=round(float(degree_val),2)).grid(row=r, column=6)
	xcomp_lab = Label(root, text=round(xcomp,2)).grid(row=r, column=7)
	ycomp_lab = Label(root, text=round(ycomp,2)).grid(row=r, column=8)
	#outputslabs2
	summation_lab = Label(root, text="Summation:")
	summation_lab.grid(row=r + 1, column=6)
	space7 = Label(root, text= " ").grid(row=r + 2, column=6)
	resultant_lab = Label(root, text="Resultant:")
	resultant_lab.grid(row=r + 3, column=6)
	direction_lab = Label(root, text="Direction:")
	direction_lab.grid(row=r + 4, column=6)
	#vector final sums
	xsum_lab = Label(root, text=round(xsum,2))
	xsum_lab.grid(row=r + 1, column=7)
	ysum_lab = Label(root, text=round(ysum,2))
	ysum_lab.grid(row=r + 1, column=8)
	res_lab = Label(root, text=round(res,2))
	res_lab.grid(row=r + 3, column=7)
	dirnum_lab = Label(root, text=str(dirnum) + direction_vec)
	dirnum_lab.grid(row=r + 4, column=7)
	row_list.append(r)
	r += 1
	forget = 1

def enter4(event):
	global xsum
	global ysum
	global r
	global forget
	global row_list
	forget = 0
	xsum = 0
	ysum = 0
	ans = answered.get().upper()
	if ans == "Y":
		res_lab.grid_forget()
		xsum_lab.grid_forget()
		ysum_lab.grid_forget()
		summation_lab.grid_forget()
		resultant_lab.grid_forget()
		direction_lab.grid_forget()
		dirnum_lab.grid_forget()
		ask1.grid_forget()
		answer.grid_forget()
		answered.grid_forget()
		for x in row_list: 
			force_lab = Label(root, text="                             ").grid(row=x, column=4)
			direction1_lab = Label(root, text="                       ").grid(row=x, column=5)
			degree_lab = Label(root, text="                       ").grid(row=x, column=6)
			xcomp_lab = Label(root, text="                               ").grid(row=x, column=7)
			ycomp_lab = Label(root, text="                               ").grid(row=x, column=8)
		force.config(state=NORMAL)
		direction.config(state=NORMAL)
		degree.config(state=NORMAL)
		r = 0
		row_list = []
		force.focus_set()
	elif ans == "N":
		root.destroy()
	else:
		answered.delete(0, "end")
		answered.insert(0, "INVALID INPUT!")

def ask():
	global answered
	global ask1
	global answer
	ask1 = Label(root, text="Would you like to put new entry?")
	ask1.grid(row=7, column=1)
	answer = Label(root, text="Type Y for Yes. N to Exit")
	answer.grid(row=8, column=1)
	answered = Entry(root)
	answered.grid(row=9, column=1)
	answered.focus_set()
	answered.bind("<Return>", enter4)
	
def num_check1():
	try:
		float(force.get())
	except ValueError:
		force.delete(0, "end")
		force.insert(0, "Invalid Input!")
		force.focus_set()
	else:
	    f = float(force.get())
	    if f > 999999:
	    	force.delete(0,"end")
	    	force.insert(0, "VALUE IS TOO HIGH!")
	    elif f == 0:
	    	if r == 0:
	    		force.delete(0,"end")
	    		force.insert(0, "NO 0 ON 1st INPUT")
	    	else:
	        	ask()
	        	force.delete(0,"end")
	        	force.config(state=DISABLED)
	        	direction.config(state=DISABLED)
	        	degree.config(state=DISABLED)
	    else:
	        direction.focus_set()

def dir_check():
	d = direction.get().upper()
	if d == "N" or d == "S" or d == "E" or d == "W" or d == "N OF E" or d == "E OF N" or d == "N OF W" or d == "W OF N" or d == "S OF E" or d == "E OF S" or d == "S OF W" or d == "W OF S":
	    degree.focus_set()
	else:
	    direction.delete(0, "end")
	    direction.insert(0, "Not a Direction!")
	    direction.focus_set()

def num_check2():
	try:
		float(degree.get())
	except ValueError:
		degree.delete(0, "end")
		degree.insert(0, "Invalid Input!")
		degree.focus_set()
	else:
		deg = float(degree.get())
		if deg > 999999:
			degree.delete(0,"end")
			degree.insert(0, "VALUE IS TOO HIGH!")
		else:
			compute()

def enter1(event):
	num_check1()
def enter2(event):
	dir_check()
def enter3(event):
	num_check2()

#SPACES
space1 = Label(root, text="      ").grid(row=0, column=0)
space2 = Label(root, text="      ").grid(row=1, column=3)
space4 = Label(root, text="      ").grid(row=4, column=0)
space5 = Label(root, text="      ").grid(row=5, column=0)
space6 = Label(root, text="      ").grid(row=6, column=0)
#LABELS for INPUT
label1 = Label(root, text="Force:").grid(row=1, column=0)
label2 = Label(root, text="Direction:").grid(row=2, column=0)
label3 = Label(root, text="Degree:").grid(row=3, column=0)
#LABELS for OUTPUT
label5 = Label(root, text="     Force     ").grid(row=0, column=4)
label6 = Label(root, text="     Direction     ").grid(row=0, column=5)
label7 = Label(root, text="     Degree     ").grid(row=0, column=6)
label8 = Label(root, text="     X Component     ").grid(row=0, column=7)
label9 = Label(root, text="     Y Component     ").grid(row=0, column=8)
#Input fields
force = Entry(root)
force.grid(row=1, column=1)
force.bind("<Return>", enter1)
direction = Entry(root)
direction.grid(row=2, column=1)
direction.bind("<Return>", enter2)
degree = Entry(root)
degree.grid(row=3, column=1)
degree.bind("<Return>", enter3)

root.mainloop()