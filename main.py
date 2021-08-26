import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# no NavigationToolbar2TkAgg but NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
# live matplotlib graph
import matplotlib.animation as animation

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12) # style, size
style.use("ggplot")

def f():
	pass

def theOnlyFunction():
	pass
def spinAgain():
	pass


def new_window():
	window = tk.Toplevel()
	window.wm_title("list of keyword")
	# window.geometry("200x200")
	for i in range(30):
		lbl = tk.Label(window, text="word "+str(i)+" meaning "+str(i), padx=5, pady=5).pack()

def start_practice():
	global practice_type
	practice_type = practice_select.get()
	# practice_mutipleChoice()
	print(practice_type)
	if practice_type == "Multiple choice":
		practice_mutipleChoice()
	elif practice_type =="Flash Card":
		practice_flashCard()
	else:
		pass

def practice_list():
	window = tk.Toplevel()
	window.wm_title("PRACTICE LIST")
	window.geometry("400x600")
	word_lbl = tk.Label(window, text="測試用", padx=10, pady=10, font=("Arial",50)) # w/o font
	word_lbl.pack()

def practice_mutipleChoice():
	global lesson_selection
	window = tk.Toplevel()
	window.wm_title("PRACTICE MC")
	window.geometry("400x600")

	info_frame = tk.Frame(window)
	word_frame = tk.Frame(window)
	select_frame = tk.Frame(window)
	stop_and_ctr_frame= tk.Frame(window)
	info_frame.pack()
	word_frame.pack()
	select_frame.pack()
	stop_and_ctr_frame.pack()

	time = str(lesson_selection.get())
	time_lbl = tk.Label(info_frame, text=time)
	time_lbl.pack(side=tk.LEFT)

	word_lbl = tk.Label(word_frame, text="blablabla", padx=10, pady=10, font=("Arial",50)) # w/o font
	word_lbl.pack()

	option = tk.StringVar()
	radio_selection1=tk.Radiobutton(select_frame, text="Selection 1", variable=option, value=1, font = ("Comic Sans MS", 30))
	radio_selection2=tk.Radiobutton(select_frame, text="Selection 2", variable=option, value=2, font = ("Comic Sans MS", 30))
	radio_selection3=tk.Radiobutton(select_frame, text="Selection 3", variable=option, value=3, font = ("Comic Sans MS", 30))
	radio_selection4=tk.Radiobutton(select_frame, text="Selection 4", variable=option, value=4, font = ("Comic Sans MS", 30))

	radio_selection1.grid(row=0, column=0)
	radio_selection2.grid(row=1, column=0)
	radio_selection3.grid(row=2, column=0)
	radio_selection4.grid(row=3, column=0)

	send_btn = tk.Button(stop_and_ctr_frame, text = "STOP", width=25, height=10, padx=20,pady=5)
	send_btn.grid(row=0, column=0)

	test_lbl = tk.Label(stop_and_ctr_frame, text="1/50", padx=10)
	test_lbl.grid(row=0, column=1)



def practice_flashCard():	
	window = tk.Toplevel()
	window.wm_title("PRACTICE FC")
	window.geometry("400x600")

	switch_frame = tk.Frame(window)
	switch_frame.pack()
	word_display_frame = tk.LabelFrame(window, borderwidth=5)
	word_display_frame.pack(anchor="center")
	press_frame = tk.Frame(window)
	press_frame.pack(side=tk.BOTTOM)

	btn_en = tk.Button(switch_frame, text="英", width=10, font = ("Comic Sans MS", 10))
	btn_ch = tk.Button(switch_frame, text="中", width=10, font = ("Comic Sans MS", 10))
	btn_chen = tk.Button(switch_frame, text="英 中", width=10, font = ("Comic Sans MS", 10))
	word_lbl = tk.Label(word_display_frame, text="TESTING",padx=10, pady=10, font = ("Comic Sans MS", 10),width=30, height=10)
	btn_iknow = tk.Button(press_frame, text="我會", width=10, height=7, font = ("Comic Sans MS", 20))
	btn_notknow = tk.Button(press_frame, text="我不會", width=10, height=7, font = ("Comic Sans MS", 20))

	btn_en.grid(row=0, column=0)
	btn_ch.grid(row=0, column=1)
	btn_chen.grid(row=0, column=2)
	word_lbl.pack()
	btn_iknow.grid(row=0, column=1, padx=10)
	btn_notknow.grid(row=0, column=2, padx=10)





# baseline
class LearningApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# tk.Tk.iconbitmap(self, default='ndhu_icon.ico')
		tk.Tk.wm_title(self, "Learning Application")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True) # fill -> fill->fill the limited that user set # expand -> beyond the limits that user set
		# basic config
		container.grid_rowconfigure(0, weight=1) # min, priotity
		container.grid_columnconfigure(0, weight=1)
 
		self.frames = {}
		for F in (Page_slots, Page_Classification, Page_Practicing, Page_Review, Page_Report, Page_Identification):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(Page_slots) # initial pages

		# basic fundimental switch(btn)
		# Bottom Page Switch
		page_switch_frame = tk.Frame(self)
		page_switch_frame.pack(side=tk.BOTTOM)
		# function btn
		# back2last_page_btn = tk.Button(page_switch_frame, text='回上\n一頁', command=lambda: self.show_frame(StartPage), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		catagory_page_btn = tk.Button(page_switch_frame, text='分類', command=lambda: self.show_frame(Page_Classification), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		practice_page_btn = tk.Button(page_switch_frame, text='測驗', command=lambda: self.show_frame(Page_Practicing), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		review_page_btn = tk.Button(page_switch_frame, text='複習', command=lambda: self.show_frame(Page_Review), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		report_page_btn = tk.Button(page_switch_frame, text='報告', command=lambda: self.show_frame(Page_Report), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		personal_page_btn = tk.Button(page_switch_frame, text='身分', command=lambda: self.show_frame(Page_Identification), height= 2, width= 7, font=LARGE_FONT).pack(side=tk.LEFT, padx=5, pady=5)
		quit_btn = tk.Button(page_switch_frame, text='關閉', command=self.destroy, height= 2, width= 7, font=LARGE_FONT, fg='red').pack(side=tk.RIGHT, padx=5, pady=5)

	def show_frame(self, cont): # self and controller/container
		frame = self.frames[cont]
		frame.tkraise()


class Page_slots(tk.Frame, LearningApp):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent) # parent class in Class SeaofBTC
		# label = tk.Label(self, text="SLOTTINGGGGG Page", font=LARGE_FONT).pack(padx=10, pady=10)
		# --------------------------------------------------------------------------------------------------------
		# LOTTERY 
		target_frame = tk.Frame(self)
		target_frame.grid(row=0,column=0)
		# target_frame.place(anchor="center")
		btn_slot1 = tk.Button(target_frame, text='A', command= theOnlyFunction, height= 30, width= 40)
		btn_slot1.grid(row=0, column=0, padx=10, pady=10)
		btn_slot2 = tk.Button(target_frame, text='B', command= theOnlyFunction, height= 30, width= 40)
		btn_slot2.grid(row=0, column=1, padx=10, pady=10)
		btn_slot3 = tk.Button(target_frame, text='C', command= theOnlyFunction, height= 30, width= 40)
		btn_slot3.grid(row=0, column=2, padx=10, pady=10)
		# LOTTERY POINT DISPLAY
		A_point = tk.Label(target_frame, text='+58')
		A_point.grid(row=1, column=0,  padx=70, pady=10)
		B_point = tk.Label(target_frame, text='x8')
		B_point.grid(row=1, column=1, padx=75, pady=10)
		C_point = tk.Label(target_frame, text='+75')
		C_point.grid(row=1, column=2, padx=75, pady=10)
		# --------------------------------------------------------------------------------------------------------
		# RANDOM
		ramdom_frame = tk.Frame(self)
		ramdom_frame.grid(row=1,column=0)
		ramdom_btn = tk.Button(ramdom_frame, text='SPIN AGAIN', command= spinAgain, height= 1, width= 20)
		ramdom_btn.pack(side='left',anchor='ne', padx=10, pady=10)
		# --------------------------------------------------------------------------------------------------------
		# DISPLAY
		display_point_frame = tk.Frame(self)
		display_point_frame.grid(row=2,column=0)
		display_point_label = tk.Label(display_point_frame, text='You EARN xxx Point!')
		display_point_label.pack()


class Page_Classification(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Classification", font=LARGE_FONT).pack(padx=10, pady=10)
		for i in range(1, 11):
			tk.Button(self, text="Lesson "+str(i), padx = 200, pady=15, command=new_window).pack()

		## Scroll Bar to show external data


class Page_Practicing(tk.Frame):
	def __init__(self, parent, controller):
		global lesson_selection, practice_select
		lesson_list = [
		"Lesson 1","Lesson 2","Lesson 3",
		"Lesson 4","Lesson 5","Lesson 6",
		"Lesson 7","Lesson 8",
		"Lesson 9","Lesson 10",
		"一字多義",
		"字形相似"]
		lesson_selection = tk.StringVar()
		lesson_selection.set(lesson_list[0])

		praztice_list = ["List(測試用)","Flash Card","Multiple choice"]
		practice_select = tk.StringVar()
		practice_select.set(praztice_list[2])

		option = tk.StringVar()

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Practicing", font=LARGE_FONT).pack(padx=10, pady=10)
		
		start_button = tk.Button(self, text='start', padx=20, pady=5, command= start_practice)
		start_button.pack()
		config_frame = tk.LabelFrame(self, text='Configuration',padx=5, pady=100)
		config_frame.pack(padx=10, pady=100)

		lbl_lesson = tk.Label(config_frame, text='Lesson : ',padx=5, pady=5)
		lbl_lesson.grid(row=0, column=0)
		drop_lesson = tk.OptionMenu(config_frame, lesson_selection, *lesson_list)
		drop_lesson.grid(row=0, column=1)

		lbl_type = tk.Label(config_frame, text='類型 : ',padx=5, pady=5)
		lbl_type.grid(row=1, column=0)
		en2ch_radiobtn=tk.Radiobutton(config_frame,text="英->中", variable=option, value=1)
		en2ch_radiobtn.grid(row=1, column=1)
		ch2en_radiobtn=tk.Radiobutton(config_frame,text="中->英", variable=option, value=2)
		ch2en_radiobtn.grid(row=1, column=2)
		option.set("1")
		
		lbl_time = tk.Label(config_frame, text='答題時間 : 秒',padx=5, pady=5)
		lbl_time.grid(row=2, column=0)
		horizontal = tk.Scale(config_frame, from_=300, to=5, orient= tk.HORIZONTAL, resolution=5, bigincrement=10)
		horizontal.grid(row=3, column=0)

		lbl_difficulty = tk.Label(config_frame, text='難度 : ',padx=5, pady=5)
		# lbl_difficulty.grid(row=4, column=0)


		lbl_ways = tk.Label(config_frame, text='方式 : ',padx=5, pady=5)
		lbl_ways.grid(row=5, column=0)
		drop_lesson = tk.OptionMenu(config_frame, practice_select, *praztice_list)
		drop_lesson.grid(row=5, column=1)

	# def slide_value(self, value):
	# 	mylbl1 = tk.Label(self.config_frame, text=horizontal.get()).grid(row=2, column=1)


class Page_Review(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Reviewing", font=LARGE_FONT).pack(padx=10, pady=10)


class Page_Report(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Search", font=LARGE_FONT).pack(padx=10, pady=10)

		frame_input = tk.Frame(self)
		frame_input.pack()
		search_lbl = tk.Label(frame_input, text="Searching Keyword: ")
		search_lbl.grid(row=0, column=0)
		search_blank = tk.Entry(frame_input, width=30)
		search_blank.grid(row=0, column=1, padx=10)
		search_btn = tk.Button(frame_input, text="Search", width= 10, padx=10)
		search_btn.grid(row=0, column=2)

		frame_output = tk.LabelFrame(self, text="Searching Result")
		frame_output.pack(padx= 50)
		default_lbl =  tk.Label(frame_output, text='Searching Result:')
		default_lbl.grid(row=0, column=0, padx=200)

		## Scroll Bar to show external data

class Page_Identification(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		info_frame = tk.LabelFrame(self, text="Page Identification", font=LARGE_FONT, padx=10, pady=10)
		info_frame.pack(pady=100)

		lbl_name = tk.Label(info_frame, text="Name : Justin Chang", font=LARGE_FONT).grid(row=1, column=0)
		lbl_id = tk.Label(info_frame, text="Student ID : 610921211", font=LARGE_FONT).grid(row=2, column=0)
		lbl_maj = tk.Label(info_frame, text="Student Major : CSIE", font=LARGE_FONT).grid(row=3, column=0)
		lbl_score = tk.Label(info_frame, text="Point : 100", font=LARGE_FONT).grid(row=4, column=0)
		lbl_openPage = tk.Label(info_frame, text="Available Level : \n Lesson1, Lesson2", font=LARGE_FONT)
		lbl_openPage.grid(row=5, column=0)


app = LearningApp()
app.geometry("1280x720")
app.mainloop()