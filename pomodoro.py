import tkinter as tk
import time
import pyautogui

class Pomodoro:
	def __init__(self, root):
		self.root = root

	def work_break(self, timer):
	
		minutes, seconds = divmod(timer, 60)
		self.min.set(f"{minutes:02d}")
		self.sec.set(f"{seconds:02d}")
		self.root.update()
		time.sleep(1)

	def work(self):
		timer = 50*60
		while timer >= 0:
			pomo.work_break(timer)
			if timer == 0:
			
				pyautogui.alert("Good Job!", "Take A Break, Click Break Button")
			timer -= 1

	def break_(self):
		timer = 5*60
		while timer >= 0:
			pomo.work_break(timer)
			if timer == 0:
			
				pyautogui.alert("Times Up", "Get Back To Work, Click Work Button")
			timer -= 1

	def main(self):
	
		self.root.geometry("450x455")
		self.root.resizable(False, False)
		self.root.title("Pomodoro Timer")

		self.root.configure(background='black')

		self.min = tk.StringVar(self.root)
		self.min.set("50")
		self.sec = tk.StringVar(self.root)
		self.sec.set("00")

		self.min_label = tk.Label(self.root,
								textvariable=self.min, font=(
			"arial", 50, "bold"), bg="black", fg='white')
		self.min_label.pack()

		self.sec_label = tk.Label(self.root,
								textvariable=self.sec, font=(
			"arial", 50, "bold"), bg="black", fg='white')
		self.sec_label.pack()

		btn_work = tk.Button(self.root, text="Start",
							bd=5, command=self.work,
							bg="red", font=(
			"arial", 15, "bold")).place(x=140, y=380)
		btn_break = tk.Button(self.root, text="Break",
							bd=5, command=self.break_,
							bg="red", font=(
			"arial", 15, "bold")).place(x=240, y=380)

		self.root.mainloop()


if __name__ == '__main__':
	pomo = Pomodoro(tk.Tk())
	pomo.main()
