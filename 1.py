import sys
import io

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>328</width>
    <height>611</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/+-.webp</normaloff>../../OneDrive/Изображения/+-.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
    <property name="flat">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/0.webp</normaloff>../../OneDrive/Изображения/0.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
    <property name="checkable">
     <bool>false</bool>
    </property>
    <property name="autoRepeat">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/,.webp</normaloff>../../OneDrive/Изображения/,.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/=.png</normaloff>../../OneDrive/Изображения/=.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/Un1.svg.png</normaloff>../../OneDrive/Изображения/Un1.svg.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/2.jpg</normaloff>../../OneDrive/Изображения/2.jpg</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/3.jpg</normaloff>../../OneDrive/Изображения/3.jpg</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/+.webp</normaloff>../../OneDrive/Изображения/+.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_9">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/4.webp</normaloff>../../OneDrive/Изображения/4.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_10">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/5.webp</normaloff>../../OneDrive/Изображения/5.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_11">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/6.webp</normaloff>../../OneDrive/Изображения/6.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_12">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/-.png</normaloff>../../OneDrive/Изображения/-.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_13">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/7.webp</normaloff>../../OneDrive/Изображения/7.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_14">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/8.png</normaloff>../../OneDrive/Изображения/8.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_15">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/9.webp</normaloff>../../OneDrive/Изображения/9.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_16">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/um.jpg</normaloff>../../OneDrive/Изображения/um.jpg</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>100</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_17">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/c.png</normaloff>../../OneDrive/Изображения/c.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_18">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/().webp</normaloff>../../OneDrive/Изображения/().webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_19">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/%.webp</normaloff>../../OneDrive/Изображения/%.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_20">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/del.jpeg</normaloff>../../OneDrive/Изображения/del.jpeg</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_21">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/линейка.webp</normaloff>../../OneDrive/Изображения/линейка.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_22">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>110</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>../../OneDrive/Изображения/про.webp</normaloff>../../OneDrive/Изображения/про.webp</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>80</y>
      <width>101</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>182</x>
      <y>10</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>328</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

    def sub(self):
        pass

    def min(self):
        pass

    def div(self):
        pass

    def mult(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
