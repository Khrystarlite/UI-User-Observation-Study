################################################################################
# set_clock.py
#		- versoion 2
# T. Chua - November 20, 2018
#
# A software implementation for Graphical User Interface (GUI) for an audio clock using the tk library.
# This initial version is a prototype.
################################################################################
__author__ = 'chua'

# Collaborators/Citations:
#   Anthony Hornof's Tkinter_sample.py (2017)
#	Eric Levieil:
#		Used to simulate GUI buttons being pressed during keystroke
#		https://stackoverflow.com/questions/32073202/tkinter-press-button-with-command
# 	Tutorial Websites:
#		https://www.python-course.eu/tkinter_layout_management.php
#		http://effbot.org/tkinterbook/pack.htm

# Dependencies
import sound
import tkinter as tk

# For data collection purposes
import os

def main():

	initAudPaths()		# Initializes the global paths to the sound files
	global   data_path
	data_path = init_data_paths()

	root = tk.Tk()		# Invoke GUI framework
	root.configure(background='white')	# Make sure background is uniform white
	myapp = userInterface(root)		# Initialize the interface
	root.mainloop()		# run the interfaces.,



	return 0


# Adapted from the MyApp class by AJ Hornof in Tkinter_sample.py (2017)
class userInterface:
	def __init__(self, parent):

		self.keyCount = 0;
		self.trial_data = []
		# self.target_dates = [
		# 	["Wednesday",4,31,"PM"],
		# 	["Sunday",1,12,"AM"],
		# 	["Thursday",6,42,"PM"],
		# 	["Friday",11,59,"PM"],
		# 	["Wednesday",4,31,"PM"],
		# 	["Tuesday",4,44,"AM"],
		# 	["Saturday",7,18,"PM"],
		# 	["Monday",8,30,"AM"],
		# 	["Sunday",0,0,"AM"],
		# 	["Wednesday",4,31,"PM"]
		#
		# ]

		self.myParent = parent	# parent is equivalent to root. The parent framework is invoked and everything is built upon it. primarily needed for keystrokes amd

		# Construct the frames that all the different parts of the GUI will be attached to

		# Instruction Frame
		self.instructFrame = tk.Frame(parent, width=500,height=500)
		self.instructFrame.grid(row=0,column=0,padx=10,pady=0)

		self.instructions = tk.Label(self.instructFrame, text="Enter the Time:\nWednesday 04:31 PM\n\nWhen you are done,\n Reset the Time")
		self.instructions.config(height=10,width=15)
		self.instructions.grid(row=0,column=0,padx=10,pady=0)





		# Main Menu Frame
		self.MM_Frame = tk.Frame(parent, bg="#ffffff")
		self.MM_Frame.grid(row=0, column=1,rowspan=5,columnspan=1,sticky="NSEW")


		self.OtherFrame = tk.Frame(parent,bg="#ffffff")
		self.OtherFrame.grid(row=0, column=2,rowspan=5,columnspan=1,sticky="NSEW")

		# Binds the three keyboard keys to keylogger for info.
		self.myParent.bind("<j>", self.keyPress)      # Left Button_1
		# self.myParent.bind("<k>", self.keyPress)      # Right Button_1
		# self.myParent.bind("<d>", self.keyPress)      # Left Button_2
		self.myParent.bind("<f>", self.keyPress)      # Right Button_3
		self.myParent.bind("<Key>", self.keyPress)      # Right Button_3
		self.myParent.bind("<space>", self.keyPress)  # Select Button

		# Utilitiy variables
		# Color of GUI elements
		self.mm_HC = 'red'
		self.cursor_Col = 'yellow'	# Need to make this flashing
		self.clock_Col = 'SteelBlue1'
		# Clock info/ default time
		self.day = "Sunday"		# unused for now
		self.hour = 12
		self.minute = 00
		self.ampm = 'AM'
		# placeholder for playing combined soundfiles
		self.TMP_WAV = 'tmp.wav'

		# Data arrays
		self.date_ARR = ["Sunday","Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday"]
		self.date_ARR_index = 0
		self.hour_ARR = [23,0,1]
		self.min_ARR = [59,0,1]

		# Main Menu
		self.MM_Label = tk.Label(self.MM_Frame,width=10)
		self.MM_Label.configure(text="Main Menu", background=self.mm_HC, relief=tk.SUNKEN)
		self.MM_Label.grid(row=0,column=0,rowspan=1,columnspan=1,sticky="nsew")
		self.PAD = tk.Label(self.MM_Frame,width=10)
		self.PAD.configure(text="", background="#ffffff", relief="solid")
		self.PAD.grid(row=1,column=0,rowspan=1,columnspan=1,sticky="nsew")
		self.Set_Day = tk.Label(self.MM_Frame,width=10)
		self.Set_Day.configure(text="Set Day", background=self.cursor_Col, relief="solid")
		self.Set_Day.grid(row=2,column=0,rowspan=1,columnspan=1,sticky="nsew")
		self.Set_Hour = tk.Label(self.MM_Frame,width=10)
		self.Set_Hour.configure(text="Set Hour", background="#ffffff", relief="solid")
		self.Set_Hour.grid(row=3,column=0,rowspan=1,columnspan=1,sticky="nsew")
		self.Set_Min = tk.Label(self.MM_Frame,width=10)
		self.Set_Min.configure(text="Set Minute", background="#ffffff", relief="solid")
		self.Set_Min.grid(row=4,column=0,rowspan=1,columnspan=1,sticky="nsew")
		self.Reset = tk.Label(self.MM_Frame,width=10)
		self.Reset.configure(text="Reset Time", background="#ffffff", relief="solid")
		self.Reset.grid(row=5,column=0,rowspan=1,columnspan=1,sticky="nsew")

		## CLock
		self.PAD = tk.Label(self.OtherFrame,width=10)
		self.PAD.configure(text="", background="#ffffff")
		self.PAD.grid(row=0,column=2,rowspan=1,columnspan=1,sticky="nsew")

		self.Day = tk.Label(self.OtherFrame,width=10)
		self.Day.configure(text=self.day, background=self.clock_Col, relief="solid")
		self.Day.grid(row=1,column=2,rowspan=1,columnspan=1,sticky="nsew")

		self.Hour = tk.Label(self.OtherFrame,width=10)
		self.Hour.configure(text=self.hour_Str(self.hour), background=self.clock_Col, relief="solid")
		self.Hour.grid(row=1,column=3,rowspan=1,columnspan=1,sticky="nsew")

		# Semicolon
		self.SC = tk.Label(self.OtherFrame,width=10)
		self.SC.configure(text=":", background=self.clock_Col, relief="solid")
		self.SC.grid(row=1,column=4,rowspan=1,columnspan=1,sticky="nsew")

		# Set Minute
		self.Min = tk.Label(self.OtherFrame,width=10)
		self.Min.configure(text=self.min_Str(self.minute), background=self.clock_Col, relief="solid")
		self.Min.grid(row=1,column=5,rowspan=1,columnspan=1,sticky="nsew")

		#AM/PM
		self.AM_PM = tk.Label(self.OtherFrame,width=10)
		self.AM_PM.configure(text=self.ampm, background=self.clock_Col, relief="solid")
		self.AM_PM.grid(row=1,column=6,rowspan=1,columnspan=1,sticky="nsew")



		# Set Day
		# The first part is "padding to make the gui more symmetrical"
		# self.PAD = tk.Label(self.Day_Frame,width=10)
		# self.PAD.configure(text="", background="#ffffff")
		# self.PAD.grid(row=2,column=2,rowspan=1,columnspan=1,sticky="nsew")
		# self.PAD = tk.Label(self.OtherFrame,width=10)
		# self.PAD.configure(text="", background="#ffffff")
		# self.PAD.grid(row=3,column=2,rowspan=1,columnspan=1,sticky="nsew")

		self.D_LEFT= tk.Label(self.OtherFrame,width=10)
		self.D_LEFT.configure(text="Saturday", background="#ffffff",relief="solid")
		self.D_LEFT.grid(row=4,column=3,rowspan=1,columnspan=1,sticky="nsew")
		# middle dial element
		self.D_MID= tk.Label(self.OtherFrame,width=10)
		self.D_MID.configure(text="Sunday", background="#ffffff",relief="solid")
		self.D_MID.grid(row=4,column=4,rowspan=1,columnspan=1,sticky="nsew")
		# innner right dial element
		self.D_RIGHT= tk.Label(self.OtherFrame,width=10)
		self.D_RIGHT.configure(text="Monday", background="#ffffff",relief="solid")
		self.D_RIGHT.grid(row=4,column=5,rowspan=1,columnspan=1,sticky="nsew")







		# Hour Dial
		# self.PAD = tk.Label(self.OtherFrame,width=10)
		# self.PAD.configure(text="", background="#ffffff")
		# self.PAD.grid(row=5,column=5,rowspan=1,columnspan=1,sticky="nsew")
		# innner left dial element
		self.H_LEFT= tk.Label(self.OtherFrame,width=10)
		self.H_LEFT.configure(text="11pm", background="#ffffff",relief="solid")
		self.H_LEFT.grid(row=5,column=3,rowspan=1,columnspan=1,sticky="nsew")
		# middle dial element
		self.H_MID= tk.Label(self.OtherFrame,width=10)
		self.H_MID.configure(text="12am", background="#ffffff",relief="solid")
		self.H_MID.grid(row=5,column=4,rowspan=1,columnspan=1,sticky="nsew")
		# innner right dial element
		self.H_RIGHT= tk.Label(self.OtherFrame,width=10)
		self.H_RIGHT.configure(text="01am", background="#ffffff",relief="solid")
		self.H_RIGHT.grid(row=5,column=5,rowspan=1,columnspan=1,sticky="nsew")

		# Minute Dial
		# self.PAD = tk.Label(self.OtherFrame,width=10)
		# self.PAD.configure(text="", background="#ffffff")
		# self.PAD.grid(row=4,column=5,rowspan=1,columnspan=1,sticky="nsew")
		# innner left dial element
		self.M_LEFT= tk.Label(self.OtherFrame,width=10)
		self.M_LEFT.configure(text="59", background="#ffffff",relief="solid")
		self.M_LEFT.grid(row=6,column=3,rowspan=1,columnspan=1,sticky="nsew")
		# middle dial element
		self.M_MID= tk.Label(self.OtherFrame,width=10)
		self.M_MID.configure(text="00", background="#ffffff",relief="solid")
		self.M_MID.grid(row=6,column=4,rowspan=1,columnspan=1,sticky="nsew")
		# innner right dial element
		self.M_RIGHT= tk.Label(self.OtherFrame,width=10)
		self.M_RIGHT.configure(text="01", background="#ffffff",relief="solid")
		self.M_RIGHT.grid(row=6,column=5,rowspan=1,columnspan=1,sticky="nsew")

		self.PAD = tk.Label(self.OtherFrame,width=10)
		self.PAD.configure(text="", background="#ffffff")
		self.PAD.grid(row=7,column=2,rowspan=1,columnspan=1,sticky="nsew")

		# Sync keystrokes with GUI button presses,
		# Left Click - Go up/left.
		self.button1 = tk.Label(self.OtherFrame ,text="Left (F)", background= "white",width=10,relief=tk.SOLID)
		self.button1.grid(column=2, row=8, sticky="NSWE")
		# self.button1.bind("<Button-1>", self.Left_Click)  ### (1)
		# self.button1.bind("<j>",self.Left_Click) ### (1)

		# Right Click - Go down/right
		self.button2 = tk.Label(self.OtherFrame,text="Right (J)", background="white",width=10,relief=tk.SOLID)
		self.button2.grid(column=6, row=8, sticky="NSWE")
		# self.button2.bind("<k>", self.Right_Click)  ### (2)
		# self.button2.bind("<Button-1>", self.Right_Click)  ### (1)

		# Select Click - Pick item
		self.button3 = tk.Label(self.OtherFrame,text="Select (Space)", background="white",width=10,relief=tk.SOLID)
		self.button3.grid(column=4, row=9, sticky="NSWE")
		# self.button3.bind("<space>", self.Select_Click)  ### (2)
		# self.button3.bind("<Button-1>",self.Select_Click)

		# binds keystrokes to button functions
		# self.myParent.bind("<j>", self.Left_Click)      # Left Button_1
		# self.myParent.bind("<k>", self.Right_Click)      # Right Button_1
		# self.myParent.bind("<d>", self.Left_Click)      # Left Button_2
		# self.myParent.bind("<f>", self.Right_Click)      # Right Button_2
		self.myParent.bind("<f>", self.Left_Click)      # Left Button_2
		self.myParent.bind("<j>", self.Right_Click)      # Right Button_2
		self.myParent.bind("<space>", self.Select_Click)  # Select Button
		self.myParent.bind("<Key>", self.Invalid_Click)		#


	def Invalid_Click(self,event):
		report_event(event)
		event_time =  str(event.time)
		self.trial_data.append([event_time, event.char])
		self.keyCount = self.keyCount + 1


	# All functions for the left click depending on the mode
	def Left_Click(self, event):
		report_event(event)        ### (3)
		event_time =  str(event.time)
		self.trial_data.append([event_time, event.char])
		self.keyCount = self.keyCount + 1

		if self.MM_Label["background"] ==  self.mm_HC:
			if self.Set_Day["background"] ==  self.cursor_Col:
				self.Set_Day["background"] = "#ffffff"
				self.Reset["background"] = self.cursor_Col
				sound.Play("extra_wav/reset.wav")
			elif self.Set_Hour["background"] ==  self.cursor_Col:
				self.Set_Hour["background"] = "#ffffff"
				self.Set_Day["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_day_f.wav")
			elif self.Set_Min["background"] ==  self.cursor_Col:
				self.Set_Min["background"] = "#ffffff"
				self.Set_Hour["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_hour_f.wav")
			elif self.Reset["background"] ==  self.cursor_Col:
				self.Reset["background"] = "#ffffff"
				self.Set_Min["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_minute_f.wav")
		elif self.Set_Day["background"] == self.mm_HC:
				self.D_RIGHT["text"] = self.D_MID["text"]
				self.D_MID["text"] = self.D_LEFT["text"]
				if self.D_LEFT["text"] == "Monday":
					self.D_LEFT["text"] = "Sunday"
					sound.Play(DAYS_PATH + "monday_f.wav")
				elif self.D_LEFT["text"] == "Tuesday":
					self.D_LEFT["text"] = "Monday"
					sound.Play(DAYS_PATH + "tuesday_f.wav")
				elif self.D_LEFT["text"] == "Wednesday":
					self.D_LEFT["text"] = "Tuesday"
					sound.Play(DAYS_PATH + "wednesday_f.wav")
				elif self.D_LEFT["text"] == "Thursday":
					self.D_LEFT["text"] = "Wednesday"
					sound.Play(DAYS_PATH + "thursday_f.wav")
				elif self.D_LEFT["text"] == "Friday":
					self.D_LEFT["text"] = "Thursday"
					sound.Play(DAYS_PATH + "friday_f.wav")
				elif self.D_LEFT["text"] == "Saturday":
					self.D_LEFT["text"] = "Friday"
					sound.Play(DAYS_PATH + "saturday_f.wav")
				elif self.D_LEFT["text"] == "Sunday":
					self.D_LEFT["text"] = "Saturday"
					sound.Play(DAYS_PATH + "sunday_f.wav")

				# self.D_LEFT.config(relief=tk.SUNKEN, background=self.cursor_Col)
				# self.D_LEFT.after(150, lambda: self.D_LEFT.config(relief=tk.SOLID, background="#ffffff"))
		elif self.Set_Hour["background"] == self.mm_HC:
			for i in range(0,len(self.hour_ARR)):
				if self.hour_ARR[i] == 0:
					self.hour_ARR[i] = 23
				else:
					self.hour_ARR[i] = self.hour_ARR[i] - 1
			self.H_LEFT["text"] = self.hour_Str_ampm(self.hour_ARR[0])
			self.H_RIGHT["text"] = self.hour_Str_ampm(self.hour_ARR[2])
			# index 2 goes last to ensure consistent am-pm with user chouice
			self.H_MID["text"] = self.hour_Str_ampm(self.hour_ARR[1])
			sound.combine_wav_files(self.TMP_WAV, NUM_PATH + self.hour_Str(self.hour_ARR[1]) + '_f.wav', MISC_PATH + self.ampm + '_f.wav')
			sound.Play(self.TMP_WAV)

			# self.H_LEFT.config(relief=tk.SUNKEN, background=self.cursor_Col)
			# self.H_LEFT.after(150, lambda: self.H_LEFT.config(relief=tk.SOLID, background="#ffffff"))

		elif self.Set_Min["background"] == self.mm_HC:
			for i in range(0,len(self.min_ARR)):
				if self.min_ARR[i] == 0:
					self.min_ARR[i] = 59
				else:
					self.min_ARR[i] = self.min_ARR[i] - 1
			self.M_LEFT["text"] = self.min_Str(self.min_ARR[0])
			self.M_RIGHT["text"] = self.min_Str(self.min_ARR[2])
			# index 2 goes last to ensure consistent am-pm with user chouice
			self.M_MID["text"] = self.min_Str(self.min_ARR[1])
			sound.Play(NUM_PATH + self.min_Str(self.min_ARR[1]) + '_f.wav')

			# self.M_LEFT.config(relief=tk.SUNKEN, background=self.cursor_Col)
			# self.M_LEFT.after(150, lambda: self.M_LEFT.config(relief=tk.SOLID, background="#ffffff"))

		self.button1.config(relief=tk.SUNKEN, background=self.cursor_Col)
		# self.button1.after(150, lambda: self.button1.config(relief=tk.SOLID, background="#ffffff"))


	# All functions for the right click depending on the mode
	def Right_Click(self, event):
		report_event(event)        ### (3)
		event_time =  str(event.time)
		self.trial_data.append([event_time, event.char])
		self.keyCount = self.keyCount + 1

		if self.MM_Label["background"] ==  self.mm_HC:
			if self.Set_Day["background"] ==  self.cursor_Col:
				self.Set_Day["background"] = "#ffffff"
				self.Set_Hour["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_hour_f.wav")
			elif self.Set_Hour["background"] ==  self.cursor_Col:
				self.Set_Hour["background"] = "#ffffff"
				self.Set_Min["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_minute_f.wav")
			elif self.Set_Min["background"] ==  self.cursor_Col:
				self.Set_Min["background"] = "#ffffff"
				self.Reset["background"] = self.cursor_Col
				sound.Play("extra_wav/reset.wav")
			elif self.Reset["background"] ==  self.cursor_Col:
				self.Reset["background"] = "#ffffff"
				self.Set_Day["background"] = self.cursor_Col
				sound.Play(MISC_PATH + "Set_day_f.wav")
		elif self.Set_Day["background"] == self.mm_HC:
				self.D_LEFT["text"] = self.D_MID["text"]
				self.D_MID["text"] = self.D_RIGHT["text"]
				if self.D_RIGHT["text"] == "Monday":
					self.D_RIGHT["text"] = "Tuesday"
					sound.Play(DAYS_PATH + "monday_f.wav")
				elif self.D_RIGHT["text"] == "Tuesday":
					self.D_RIGHT["text"] = "Wednesday"
					sound.Play(DAYS_PATH + "tuesday_f.wav")
				elif self.D_RIGHT["text"] == "Wednesday":
					self.D_RIGHT["text"] = "Thursday"
					sound.Play(DAYS_PATH + "wednesday_f.wav")
				elif self.D_RIGHT["text"] == "Thursday":
					self.D_RIGHT["text"] = "Friday"
					sound.Play(DAYS_PATH + "thursday_f.wav")
				elif self.D_RIGHT["text"] == "Friday":
					self.D_RIGHT["text"] = "Saturday"
					sound.Play(DAYS_PATH + "friday_f.wav")
				elif self.D_RIGHT["text"] == "Saturday":
					self.D_RIGHT["text"] = "Sunday"
					sound.Play(DAYS_PATH + "saturday_f.wav")
				elif self.D_RIGHT["text"] == "Sunday":
					self.D_RIGHT["text"] = "Monday"
					sound.Play(DAYS_PATH + "sunday_f.wav")

				# self.D_RIGHT.config(relief=tk.SUNKEN, background=self.cursor_Col)
				# self.D_RIGHT.after(150, lambda: self.D_RIGHT.config(relief=tk.SOLID, background="#ffffff"))

		elif self.Set_Hour["background"] == self.mm_HC:
			for i in range(0,len(self.hour_ARR)):
				if self.hour_ARR[i] == 23:
					self.hour_ARR[i] = 0
				else:
					self.hour_ARR[i] = self.hour_ARR[i] + 1
			self.H_LEFT["text"] = self.hour_Str_ampm(self.hour_ARR[0])
			self.H_RIGHT["text"] = self.hour_Str_ampm(self.hour_ARR[2])
			# index 2 goes last to ensure consistent am-pm with user chouice
			self.H_MID["text"] = self.hour_Str_ampm(self.hour_ARR[1])
			sound.combine_wav_files(self.TMP_WAV, NUM_PATH + self.hour_Str(self.hour_ARR[1]) + '_f.wav', MISC_PATH + self.ampm + '_f.wav')
			sound.Play(self.TMP_WAV)

			# self.H_RIGHT.config(relief=tk.SUNKEN, background=self.cursor_Col)
			# self.H_RIGHT.after(150, lambda: self.H_RIGHT.config(relief=tk.SOLID, background="#ffffff"))
		elif self.Set_Min["background"] == self.mm_HC:
			for i in range(0,len(self.min_ARR)):
				if self.min_ARR[i] == 59:
					self.min_ARR[i] = 0
				else:
					self.min_ARR[i] = self.min_ARR[i] +  1
			self.M_LEFT["text"] = self.min_Str(self.min_ARR[0])
			self.M_RIGHT["text"] = self.min_Str(self.min_ARR[2])
			# index 2 goes last to ensure consistent am-pm with user chouice
			self.M_MID["text"] = self.min_Str(self.min_ARR[1])
			sound.Play(NUM_PATH + self.min_Str(self.min_ARR[1]) + '_f.wav')

			# self.M_RIGHT.config(relief=tk.SUNKEN, background=self.cursor_Col)
			# self.M_RIGHT.after(150, lambda: self.M_RIGHT.config(relief=tk.SOLID, background="#ffffff"))

		self.button2.config(relief=tk.SUNKEN, background=self.cursor_Col)
		self.button2.after(150, lambda: self.button2.config(relief=tk.SOLID, background="#ffffff"))


	# All functions for the spacebar depending on the mode
	def Select_Click(self, event):
		report_event(event)
		event_time =  str(event.time)
		self.trial_data.append([event_time, event.char])
		self.keyCount = self.keyCount + 1

		if self.MM_Label["background"] ==  self.mm_HC:
			self.MM_Label["background"] = "white"
			self.MM_Label["relief"] = tk.SOLID
			if self.Set_Day["background"] ==  self.cursor_Col:
				self.Set_Day["background"] = self.mm_HC
				self.Set_Day["relief"] = tk.SUNKEN
				self.D_MID["background"] = self.cursor_Col
				# sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', MISC_PATH + 'Set_day_of_week_f.wav')
				# sound.Play(self.TMP_WAV)
			elif self.Set_Hour["background"] ==  self.cursor_Col:
				self.Set_Hour["background"] = self.mm_HC
				self.Set_Hour["relief"] = tk.SUNKEN
				self.H_MID["background"] = self.cursor_Col
				# sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', MISC_PATH + 'Set_hour_f.wav')
				# sound.Play(self.TMP_WAV)
			elif self.Set_Min["background"] ==  self.cursor_Col:
				self.Set_Min["background"] = self.mm_HC
				self.Set_Min["relief"] = tk.SUNKEN
				self.M_MID["background"] = self.cursor_Col
				# sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', MISC_PATH + 'Set_minute_f.wav')
				# sound.Play(self.TMP_WAV)

			############# RESET BUTTON #############
			elif self.Reset["background"] ==  self.cursor_Col:

				trial_count = 1
				trial_time = int(self.trial_data[-1][0]) - int(self.trial_data[0][0])

				while (os.path.exists(data_path + "trial_" + str(trial_count) + ".txt")):
					trial_count = trial_count + 1





				f = open(data_path + "trial_" + str(trial_count) + ".txt", "w+")
				f.write(str(self.keyCount) + ", " + str(trial_time) + "\n")
				for item in self.trial_data:
					f.write(str(item[0]) + ", " + str(item[1]) + "\n" )

				# print(self.day)
				# print(self.hour)
				# print(self.minute)
				# print(self.ampm)
				# if(self.day != self.target_dates[trial_count-1][0]
				# 		and self.hour != self.target_dates[trial_count-1][1]
				# 		and self.minute != self.target_dates[trial_count-1][2]
				# 		and self.ampm != self.target_dates[trial_count-1][3]
				# 		):
				# 	f.write(["Wrong date entered!" + str(trial_count)])
				# 	print("Wrong date entered!")


				self.day = "Sunday"		# unused for now
				self.hour = 12
				self.minute = 00
				self.ampm = 'AM'


				self.D_LEFT["text"] = "Saturday"
				self.D_MID["text"] = "Sunday"
				self.D_RIGHT["text"] = "Monday"
				self.hour_ARR = [23,0,1]
				self.H_LEFT["text"] = self.hour_Str_ampm(self.hour_ARR[0])
				self.H_RIGHT["text"] = self.hour_Str_ampm(self.hour_ARR[2])
				self.H_MID["text"] = self.hour_Str_ampm(self.hour_ARR[1])

				self.min_ARR = [59,0,1]
				self.M_LEFT["text"] = self.min_Str(self.min_ARR[0])
				self.M_RIGHT["text"] = self.min_Str(self.min_ARR[2])
				self.M_MID["text"] = self.min_Str(self.min_ARR[1])

				self.Day["text"] = "Sunday"
				self.Hour["text"] = "12"
				self.Min["text"] = "00"
				self.AM_PM["text"] = "AM"
				self.Reset["background"] = "#ffffff"
				self.Set_Day["background"] = self.cursor_Col
				self.MM_Label["background"]=self.mm_HC
				self.MM_Label["relief"]= tk.SUNKEN

				self.keyCount = 0
				self.trial_data = []
				# sound.Play("extra_wav/reset.wav")
				if (trial_count == 1):

					self.instructions["text"] = "Enter the Time:\nSunday 01:12 AM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 2):
					self.instructions["text"] = "Enter the Time:\nThursday 06:42 AM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 3):
					self.instructions["text"] = "Enter the Time:\nFriday 11:59 PM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 4):
					self.instructions["text"] = "Enter the Time:\nWednesday 04:31 PM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 5):
					self.instructions["text"] = "Enter the Time:\nTuesday 04:44 AM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 6):
					self.instructions["text"] = "Enter the Time:\nSaturday 07:18 PM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 7):
					self.instructions["text"] = "Enter the Time:\nMonday 08:30 AM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 8):
					self.instructions["text"] = "Enter the Time:\nSunday 00:00 PM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count == 9):
					self.instructions["text"] = "Enter the Time:\nWednesday 04:31 PM\n\nWhen you are done,\n Reset the Time"
					self.instructions.grid(row=0,column=0,padx=10,pady=2)
				elif (trial_count >= 11):
					sound.Play(MISC_PATH + "Exiting_program_f.wav")
					try:
						self.myParent.after(1500,self.myParent.destroy)
					except:
						pass
			########



		########
		elif self.Set_Day["background"] == self.mm_HC:
			self.Set_Day["relief"] = tk.SOLID
			self.Set_Day["background"] = self.cursor_Col
			self.MM_Label["background"]=self.mm_HC
			self.MM_Label["relief"]= tk.SUNKEN
			tmp = ""
			self.Day["text"] = self.D_MID["text"]
			self.Set_Day["relief"] = tk.SOLID
			self.Set_Day["background"] = self.cursor_Col
			self.MM_Label["background"]=self.mm_HC
			self.MM_Label["relief"]= tk.SUNKEN
			self.D_MID["background"] = "white"
			self.day = self.Day["text"]

			# if self.day == "Sunday":
			# 	tmp = "sunday_f"
			# elif self.day == "Monday":
			# 	tmp = "monday_f"
			# elif self.day == "Tuesday":
			# 	tmp = "tuesday_f"
			# elif self.day == "Wednesday":
			# 	tmp = "wednesday_f"
			# elif self.day == "Thursday":
			# 	tmp = "thursday_f"
			# elif self.day == "Friday":
			# 	tmp = "friday_f"
			# elif self.day == "Saturday":
			# 	tmp = "saturday_f"

			# sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', DAYS_PATH + tmp + '.wav')
			# sound.Play(self.TMP_WAV)

		elif self.Set_Hour["background"] == self.mm_HC:
			self.Hour["text"] = self.hour_Str(self.hour_ARR[1])
			self.AM_PM["text"] = self.ampm
			self.Set_Hour["relief"] = tk.SOLID
			self.Set_Hour["background"] = self.cursor_Col
			self.MM_Label["background"]=self.mm_HC
			self.MM_Label["relief"]= tk.SUNKEN
			self.H_MID["background"] = "white"
			self.hour = self.hour_ARR[1]
			# # sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', NUM_PATH + self.hour_Str(self.hour) + '_f.wav', MISC_PATH + self.ampm + '_f.wav')
			# sound.Play(self.TMP_WAV)
		elif self.Set_Min["background"] == self.mm_HC:
			self.Min["text"] = self.min_Str(self.min_ARR[1])
			self.Set_Min["relief"] = tk.SOLID
			self.Set_Min["background"] = self.cursor_Col
			self.MM_Label["background"]=self.mm_HC
			self.MM_Label["relief"]= tk.SUNKEN
			self.M_MID["background"] = "white"
			self.minute = self.min_ARR[1]
			# # sound.combine_wav_files(self.TMP_WAV, MISC_PATH + 'you_selected_f.wav', NUM_PATH + self.min_Str(self.minute) + '_f.wav')
			# sound.Play(self.TMP_WAV)


		self.button3.config(relief=tk.SUNKEN, background=self.cursor_Col)
		self.button3.after(150, lambda: self.button3.config(relief=tk.SOLID, background="#ffffff"))


	# Converts hour integers to strings without concating AM/PM - still converts am/pm when appropriate
	def hour_Str(self,hour_int):
		if hour_int == 0 or hour_int == 24:
			hour_int = 12
			hour_str = str(hour_int)
			self.ampm = 'AM'
		elif hour_int > 12:               # for PM times
			hour_int = hour_int - 12
			if hour_int < 10:
				hour_str='0' + str(hour_int)
			else:
				hour_str = str(hour_int)
			self.ampm = 'PM'
		else:
			self.ampm = 'AM'
			if hour_int < 10:
				hour_str='0' + str(hour_int)
			else:
				hour_str = str(hour_int)
		return hour_str


	# convets hours intefers to strings with AM/PM
	def hour_Str_ampm(self,hour_int):
		if hour_int == 0 or hour_int == 24:
			hour_int = 12
			self.ampm = 'AM'
		if hour_int > 12:               # for PM times
			hour_int = hour_int - 12
			self.ampm  = 'PM'
		else:
			self.ampm  = 'AM'

		if hour_int < 10:
			hour_str='0' + str(hour_int)
		else:
			hour_str = str(hour_int)

		return hour_str+self.ampm

	# Converts minute integers to strings
	def min_Str(self,min_int):
		if min_int < 10:
			return '0' + str(min_int)
		else:
			return str(min_int)


	# handoff method for reporting keystroke event when something happens in the GUI
	def keyPress(self, event):
		report_event(event)   ### (4)


# Prints a report when the GUI is interacted with.
def report_event(event):     ### (5)
	"""Print a description of an event, based on its attributes.
	"""
	event_name = {"2": "KeyPress", "4": "ButtonPress"}
	event_time =  str(event.time)
	print ("Time:", str(event.time))   ### (6)
	print ("event:", event)

	# Sample sound
	# sound.Play( "wav_files_provided/numbers_f/01_f.wav" )

# Get current subject number





# Initalize qudio paths - this way the program can be flexible about when
# accounting for gender for the voice clips.
def initAudPaths():
	# Like before, these are global.
	global  DAYS_PATH,NUM_PATH, MISC_PATH, EXITING_PROGRAM_WAV_DURATION, DAYS, \
			DAYS_ARR, NUM


	# All the paths, using just female voice this iteration
	DAYS_PATH = "wav_files_provided/days_of_week_f/"
	NUM_PATH = "wav_files_provided/numbers_f/"
	MISC_PATH = "wav_files_provided/miscellaneous_f/"

	# Holds each weekday as string
	DAYS = ['sunday_f','monday_f','tuesday_f', 'wednesday_f', 'thursday_f', 'friday_f',
				'saturday_f']
	# Holds each day's sound file path
	DAYS_ARR = [0]*7
	# Holds sound file path for each number
	NUM = [0]*60

	# Loads all the number sound file paths into NUM
	for i in range(60):
		if i < 10:  # Numbers 0-9 are lead by a 0
			NUM[i] = NUM_PATH + '0' + str(i) + '_f.wav'
		else:
			NUM[i] = NUM_PATH + str(i) + '_f.wav'

	# Load all the day sound file path s into DAYS_ARR
	for j in range(7):
		DAYS_ARR[j] = DAYS_PATH + DAYS[j] + '.wav'
	# Currently experimenting with the duration
	EXITING_PROGRAM_WAV_DURATION = 1.09
	# EXITING_PROGRAM_WAV_DURATION = 0.45

def init_data_paths():
	sub_num = 1
	path = "data/"
	if not os.path.exists(path):
		os.mkdir(path)

	while (os.path.exists(path + "subject_" + str(sub_num) + "/")):
		sub_num  = sub_num + 1

	path = path + "subject_" + str(sub_num) + "/"
	os.mkdir(path)
	path = path + "version_1/"

	if not os.path.exists(path):
		os.mkdir(path)

	return path

main()
