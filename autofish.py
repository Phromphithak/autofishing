import cv2
import numpy as np
import os
from windowscapture import WindowCapture
import sys
import pygetwindow as gw
import keyboard as kb
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Autofish for berlin v2 By XIL'
        self.left = 100
        self.top = 100
        self.width = 100
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QVBoxLayout()

        self.program_combo = QComboBox(self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)

        self.program_combo.addItems(self.get_window_titles())
        self.start_button.clicked.connect(self.start_capture)
        self.stop_button.clicked.connect(self.stop_capture)

        self.layout.addWidget(self.program_combo)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

        self.is_running = False
        self.wincap = None

    def get_window_titles(self):
        window_titles = []
        for window in gw.getAllTitles():
            window_titles.append(window)
        return window_titles

    def start_capture(self):
        selected_title = self.program_combo.currentText()
        if selected_title:
            self.wincap = WindowCapture(selected_title)
            self.is_running = True
            self.capture_loop()

    def stop_capture(self):
        self.is_running = False
        cv2.destroyAllWindows()
    
    
       

    def capture_loop(self):
        prev_green_pixel_count = 0  # เก็บจำนวนพิกเซลสีเขียวของเฟรมก่อนหน้า
        while self.is_running:
            def press_keys():
                kb.press_and_release('q')
                kb.press_and_release('w')
                kb.press_and_release('e')
                kb.press_and_release('r')
                kb.press_and_release('s')
            if self.wincap:
                screenshot = self.wincap.get_screenshot()
                x1, x2, y1, y2 = 1666, 1794, 400, 520  # แก้ตามที่คุณต้องการ
                screenshot = screenshot[y1:y2, x1:x2]
                hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
                lower_red = np.array([0, 0, 206])
                upper_red = np.array([8, 8, 226])
                lower_green = np.array([0, 202, 0])
                upper_green = np.array([130, 222, 8])
                red_mask = cv2.inRange(screenshot, lower_red, upper_red)
                green_mask = cv2.inRange(screenshot, lower_green, upper_green)
                
                contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                contours_green, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                found = False  # สร้างตัวแปร found เพื่อติดตามว่าพบการทับกันหรือไม่

                for contour_red in contours_red:
                    for contour_green in contours_green:
                        center_red = (int(contour_red[0][0][0]), int(contour_red[0][0][1]))
                        center_green = (int(contour_green[0][0][0]), int(contour_green[0][0][1]))

                # ตรวจสอบจำนวนพิกเซลสีเขียว
                green_pixel_count = cv2.countNonZero(green_mask)
                if green_pixel_count < prev_green_pixel_count:
                    print("Green pixel going down")
                    press_keys()

                prev_green_pixel_count = green_pixel_count

                if found:  # ตรวจสอบค่า found เพื่อทำงานเมื่อพบการทับกัน
                    pass
                screenshot_combined = np.hstack((screenshot, cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)))
                cv2.imshow('Screenshot', screenshot_combined)
            
            if cv2.waitKey(1) == ord('k') or cv2.getWindowProperty('Screenshot', cv2.WND_PROP_VISIBLE) < 1:
                cv2.destroyAllWindows()
                self.is_running = False
                break









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
