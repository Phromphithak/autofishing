import cv2
import numpy as np
import os
import sys
import pygetwindow as gw
import keyboard as kb
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox
import win32gui, win32ui, win32con

class WindowCapture:
    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        
        self.w = 0
        self.h = 0
        self.cropped_x = 0
        self.cropped_y = 0
        self.offset_x = 0
        self.offset_y = 0

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img


    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)




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

         # เพิ่ม QComboBox
        self.resolution_combo = QComboBox(self)
        self.resolution_combo.addItems(["1920x1080", "1600x900"])
        self.layout.addWidget(self.resolution_combo)
        # เพิ่ม QPushButton เพื่อเรียกใช้ฟังก์ชัน resconfig() เมื่อผู้ใช้คลิกปุ่ม
        self.res_button = QPushButton('Set Resolution', self)
        self.res_button.clicked.connect(self.resconfig)
        self.layout.addWidget(self.res_button)
        
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

    
    def resconfig(self):
        selected_resolution = self.resolution_combo.currentText()
        if selected_resolution == "1920x1080":
            x1, x2, y1, y2 = 1666, 1794, 400, 520
        elif selected_resolution == "1600x900":
            x1, x2, y1, y2 = 1366, 1494, 322, 422
        else:
            # ใส่ค่าเริ่มต้นหรือเงื่อนไขเพิ่มเติมตามที่ต้องการ
            pass
        return x1,x2,y1,y2
    
       

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
                x1, x2, y1, y2 = self.resconfig()               
                screenshot = screenshot[y1:y2, x1:x2]
            if screenshot.size != 0:    
                lower_red = np.array([0, 0, 206])
                upper_red = np.array([8, 8, 226])
                lower_green = np.array([0, 202, 0])
                upper_green = np.array([130, 222, 8])
                red_mask = cv2.inRange(screenshot, lower_red, upper_red)
                green_mask = cv2.inRange(screenshot, lower_green, upper_green)
                
                found = False  # สร้างตัวแปร found เพื่อติดตามว่าพบการทับกันหรือไม่

                # ตรวจสอบจำนวนพิกเซลสีเขียว
                green_pixel_count = cv2.countNonZero(green_mask)
                if green_pixel_count < prev_green_pixel_count:
                    press_keys()

                prev_green_pixel_count = green_pixel_count

                if found:  # ตรวจสอบค่า found เพื่อทำงานเมื่อพบการทับกัน
                    pass
                screenshot_combined = np.hstack((screenshot, cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)))
                cv2.imshow('autofish v2 By XIL', screenshot_combined)
            
            if cv2.waitKey(1) == ord('k') or cv2.getWindowProperty('autofish v2 By XIL', cv2.WND_PROP_VISIBLE) < 1:
                cv2.destroyAllWindows()
                self.is_running = False
                break
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
