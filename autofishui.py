# Import Module
import sys
import time as t
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from threading import *

# pyautogui import
from pyautofish import *
import cv2
import numpy

class ListBox(QWidget):

	def __init__(self):
		super(ListBox, self).__init__()

		global msg
		msg = QLabel("Status : พร้อมทำงาน * สถานะยยังไม่เสร็จ", self)
		msg.move(40, 40)

		self.ss = True
		self.MainUI()
		self.startButton()
		self.stopButton()
	#### -------ฟังชั่นตกปลา------####
	def MainUI(self):
		self.setGeometry(300, 100, 300, 100)
		self.setWindowTitle("Berlin auto Fishing - By Lix")
		
	####-------เรียก ฟังชั่นตกปลา--------####
	def Operation(self):
		while self.ss == False:
			print('Calling Fuction!')
			k1()
			t.sleep(0.1)
			k2()
			t.sleep(0.1)
			k3()
			t.sleep(0.1)
			k4()
		else:
			print('Stop Call Fuction!')
			return True
			
	####-------ปิดเปิดการทำงาน------####
	def run(self):
		print('กำลังเริ่ม')
		self.ss = False
		self.Operation()
	
	def stopRun(self):
		print('หยุด!')
		self.ss = True
		self.Operation()

	def startButton(self):
		# text
		# Add Push Button
		start_btn = QPushButton(self)
		start_btn.setText('Start')
		start_btn.clicked.connect(self.thread)
		
		
	
	def stopButton(self):
		# text
		
		# Add Push Button
		stop_btn = QPushButton(self)
		stop_btn.move(80,0)
		stop_btn.setText('Stop')
		stop_btn.clicked.connect(self.thread2)
		t.sleep(2)


	def thread(self):
		self.stb = True
		t1=Thread(target=self.run)
		t1.start()
	
	def thread2(self):
		self.stb = True
		t2=Thread(target=self.stopRun)
		t2.start()	
	



if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = ListBox()
	win.show()
	sys.exit(app.exec_())
