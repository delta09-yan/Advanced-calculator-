import io

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QInputDialog

template_2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>772</width>
    <height>300</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="tempbtn">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>201</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Цельсия (°C)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="timebtn">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>0</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Секунды (s)</string>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="tempSpinBox">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>181</width>
     <height>22</height>
    </rect>
   </property>
   <property name="minimum">
    <double>-1000000000.000000000000000</double>
   </property>
   <property name="maximum">
    <double>1000000000.000000000000000</double>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="timeSpinBox">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>40</y>
     <width>171</width>
     <height>22</height>
    </rect>
   </property>
   <property name="minimum">
    <double>-100000000.000000000000000</double>
   </property>
   <property name="maximum">
    <double>100000000.000000000000000</double>
   </property>
  </widget>
  <widget class="QPushButton" name="tempbtn_2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>80</y>
     <width>201</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Фаренгейта (°F)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="timebtn_2">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>80</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Минуты (min)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="checktempbtn">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>180</y>
     <width>131</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Convert</string>
   </property>
  </widget>
  <widget class="QPushButton" name="checktimebtn">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>180</y>
     <width>131</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Convert</string>
   </property>
  </widget>
  <widget class="QLabel" name="templabel">
   <property name="geometry">
    <rect>
     <x>6</x>
     <y>129</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="timelabel">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>130</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="weightbtn_2">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>80</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Килограммы (kg)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="weightbtn">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>0</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Тонны (t)</string>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="squareSpinBox">
   <property name="geometry">
    <rect>
     <x>411</x>
     <y>40</y>
     <width>171</width>
     <height>22</height>
    </rect>
   </property>
   <property name="minimum">
    <double>-100000000.000000000000000</double>
   </property>
   <property name="maximum">
    <double>100000000.000000000000000</double>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="weightSpinBox">
   <property name="geometry">
    <rect>
     <x>601</x>
     <y>40</y>
     <width>171</width>
     <height>22</height>
    </rect>
   </property>
   <property name="minimum">
    <double>-100000000.000000000000000</double>
   </property>
   <property name="maximum">
    <double>100000000.000000000000000</double>
   </property>
  </widget>
  <widget class="QPushButton" name="squarebtn_2">
   <property name="geometry">
    <rect>
     <x>390</x>
     <y>80</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Гектары (ha)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="squarebtn">
   <property name="geometry">
    <rect>
     <x>390</x>
     <y>0</y>
     <width>191</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Акры (ac)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="consquarebtn">
   <property name="geometry">
    <rect>
     <x>450</x>
     <y>180</y>
     <width>131</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Convert</string>
   </property>
  </widget>
  <widget class="QPushButton" name="conweightbtn">
   <property name="geometry">
    <rect>
     <x>640</x>
     <y>180</y>
     <width>131</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Convert</string>
   </property>
  </widget>
  <widget class="QLabel" name="squarelabel">
   <property name="geometry">
    <rect>
     <x>400</x>
     <y>130</y>
     <width>181</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="weightlabel">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>120</y>
     <width>181</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class UnitConvertion(QWidget):
    def __init__(self):
        super().__init__()
        n = io.StringIO(template_2)
        uic.loadUi(n, self)
        self.temp_value = 'Цельсия (°C)'
        self.temp_2_value = 'Фаренгейта (°F)'

        self.time_value = 'Секунды (s)'
        self.time_2_value = 'Минуты (min)'

        self.square_value = 'Акры (ac)'
        self.square_2_value = 'Гектары (ha)'

        self.weight_value = 'Тонны (t)'
        self.weight_2_value = 'Килограммы (kg)'

        self.tempbtn.clicked.connect(self.temp)
        self.tempbtn_2.clicked.connect(self.temp_2)
        self.checktempbtn.clicked.connect(self.temp_convert)

        self.timebtn.clicked.connect(self.time)
        self.timebtn_2.clicked.connect(self.time_2)
        self.checktimebtn.clicked.connect(self.time_convert)

        self.squarebtn.clicked.connect(self.square)
        self.squarebtn_2.clicked.connect(self.square_2)
        self.consquarebtn.clicked.connect(self.square_convert)

        self.weightbtn.clicked.connect(self.weight)
        self.weightbtn_2.clicked.connect(self.weight_2)
        self.conweightbtn.clicked.connect(self.weight_convert)

    def temp(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид температуры',
                                                ("Цельсия (°C)", 'Фаренгейта (°F)', 'Кельвина (°K)'), 1, False)
        if ok_pressed:
            self.tempbtn.setText(name)
            self.temp_value = self.tempbtn.text()

    def time(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид времени',
                                                (
                                                    "МИЛсекунды (ms)", 'Секунды (s)', 'Минуты (min)', "Часы (h)",
                                                    "Дни (d)",
                                                    "Недели (wk)"), 1, False)
        if ok_pressed:
            self.timebtn.setText(name)
            self.time_value = self.timebtn.text()

    def temp_2(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид температуры',
                                                ("Цельсия (°C)", 'Фаренгейта (°F)', 'Кельвина (°K)'), 1, False)
        if ok_pressed:
            self.tempbtn_2.setText(name)
            self.temp_2_value = self.tempbtn_2.text()

    def time_2(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид времени',
                                                (
                                                    "МИЛсекунды (ms)", 'Секунды (s)', 'Минуты (min)', "Часы (h)",
                                                    "Дни (d)",
                                                    "Недели (wk)"), 1, False)
        if ok_pressed:
            self.timebtn_2.setText(name)
            self.time_2_value = self.timebtn_2.text()

    def square(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид площади',
                                                (
                                                    "Акры (ac)", 'Ары (a)', 'Гектары (ha)', "Кв. см (cm²)",
                                                    "Кв. футы (ft²)",
                                                    "Кв. дюймы (in²)", "Кв. метры(m²)"), 1, False)
        if ok_pressed:
            self.squarebtn.setText(name)
            self.square_value = self.squarebtn.text()

    def square_2(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид площади',
                                                (
                                                    "Акры (ac)", 'Ары (a)', 'Гектары (ha)', "Кв. см (cm²)",
                                                    "Кв. футы (ft²)",
                                                    "Кв. дюймы (in²)", "Кв. метры(m²)"), 1, False)
        if ok_pressed:
            self.squarebtn_2.setText(name)
            self.square_2_value = self.squarebtn_2.text()

    def weight(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид массы',
                                                (
                                                    "Тонны (t)", 'Анг. тонны (t)', "Ам. тонны (t)",
                                                    "Фунты (lb)",
                                                    "Унции (oz)", "Килограммы (kg)", "Граммы (g)"), 1, False)
        if ok_pressed:
            self.weightbtn.setText(name)
            self.weight_value = self.weightbtn.text()

    def weight_2(self):
        name, ok_pressed = QInputDialog.getItem(self, "", 'Выберите вид массы',
                                                (
                                                    "Тонны (t)", 'Анг. тонны (t)', "Ам. тонны (t)",
                                                    "Фунты (lb)",
                                                    "Унции (oz)", "Килограммы (kg)", "Граммы (g)"), 1, False)
        if ok_pressed:
            self.weightbtn_2.setText(name)
            self.weight_2_value = self.weightbtn_2.text()

    def weight_convert(self):
        if self.weight_value == "Тонны (t)" and self.weight_2_value == "Тонны (t)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() * 0.984206527611
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() * 1.1023
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 35273.96195
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() * 1000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Тонны (t)" and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 1000000
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() * 1.01605
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == 'Анг. тонны (t)':
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() * 1.1200
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 32000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() * 1016.0469
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == 'Анг. тонны (t)' and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 1016046.9088
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() * 0.907185
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() / 1.12
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Ам. тонны (t)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 32000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() * 907.18474
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Ам. тонны (t)" and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 907184.74
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() / 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() / 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() / 2000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Фунты (lb)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 16
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() * 0.45359237
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Фунты (lb)" and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 453.59237
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() / 32000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() / 35840
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() / 32000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 0.0625
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Унции (oz)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() * 0.0283495
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Унции (oz)" and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 28.3495
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() / 1000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() / 1000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() / 1000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 2.20462
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 35.273962
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Килограммы (kg)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')
        elif self.weight_value == "Килограммы (kg)" and self.weight_2_value == "Граммы (g)":
            result = self.weightSpinBox.value() * 1000
            self.weightlabel.setText(f'{result}')

        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Тонны (t)":
            result = self.weightSpinBox.value() / 1000000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == 'Анг. тонны (t)':
            result = self.weightSpinBox.value() / 1016046.9088
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Ам. тонны (t)":
            result = self.weightSpinBox.value() / 1000000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Фунты (lb)":
            result = self.weightSpinBox.value() * 0.00220462
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Унции (oz)":
            result = self.weightSpinBox.value() * 0.035274
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Килограммы (kg)":
            result = self.weightSpinBox.value() / 1000
            self.weightlabel.setText(f'{result}')
        elif self.weight_value == "Граммы (g)" and self.weight_2_value == "Граммы (g)":
            self.weightlabel.setText(f'{self.weightSpinBox.value()}')

    def square_convert(self):
        print(self.squareSpinBox.value())
        if self.square_value == "Акры (ac)" and self.square_2_value == "Акры (ac)":
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() * 40.468564
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() * 0.404686
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 40468564.224
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() * 43560
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 6272640
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Акры (ac)" and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() * 4046.856422
            self.squarelabel.setText(f'{result}')

        elif self.square_value == 'Ары (a)' and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() * 0.02471054
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == 'Ары (a)':
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() / 100
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 1000000
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() * 1076.391
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 155000.310001
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Ары (a)' and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() * 100
            self.squarelabel.setText(f'{result}')

        elif self.square_value == 'Гектары (ha)' and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() * 2.471054
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() * 100
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == 'Гектары (ha)':
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 100000000
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() * 107639.104167
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 15500031.000062
            self.squarelabel.setText(f'{result}')
        elif self.square_value == 'Гектары (ha)' and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() * 10000
            self.squarelabel.setText(f'{result}')

        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() * 2.4711E-8
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() * 0.000001
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() / 100000000
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == "Кв. см (cm²)":
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() * 0.001076
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 0.155
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. см (cm²)" and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() / 10000
            self.squarelabel.setText(f'{result}')

        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() / 43560
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() * 0.0009290304
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() * 9.2903E-6
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 929.0304
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == "Кв. футы (ft²)":
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 144
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. футы (ft²)" and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() / 0.092903
            self.squarelabel.setText(f'{result}')

        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() / 6272640
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() * 6.4516E-6
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() * 6.4516E-8
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 6.4516
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() / 144
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == "Кв. дюймы (in²)":
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')
        elif self.square_value == "Кв. дюймы (in²)" and self.square_2_value == "Кв. метры(m²)":
            result = self.squareSpinBox.value() * 0.000645
            self.squarelabel.setText(f'{result}')

        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == "Акры (ac)":
            result = self.squareSpinBox.value() * 0.000247
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == 'Ары (a)':
            result = self.squareSpinBox.value() / 100
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == 'Гектары (ha)':
            result = self.squareSpinBox.value() / 10000
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == "Кв. см (cm²)":
            result = self.squareSpinBox.value() * 10000
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == "Кв. футы (ft²)":
            result = self.squareSpinBox.value() * 10.76391
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == "Кв. дюймы (in²)":
            result = self.squareSpinBox.value() * 1550
            self.squarelabel.setText(f'{result}')
        elif self.square_value == "Кв. метры(m²)" and self.square_2_value == "Кв. метры(m²)":
            self.squarelabel.setText(f'{self.squareSpinBox.value()}')

    def temp_convert(self):
        #   Конвертирую разные виды температур в другой вид
        if self.temp_value == "Цельсия (°C)" and self.temp_2_value == 'Цельсия (°C)':
            self.templabel.setText(f'{self.tempSpinBox.value()}')
        elif self.temp_value == "Цельсия (°C)" and self.temp_2_value == 'Фаренгейта (°F)':
            result = (self.tempSpinBox.value() * 1.80) + 32
            self.templabel.setText(f'{result}')
        elif self.temp_value == "Цельсия (°C)" and self.temp_2_value == 'Кельвина (°K)':
            result = self.tempSpinBox.value() + 273.15
            self.templabel.setText(f'{result}')

        elif self.temp_value == 'Фаренгейта (°F)' and self.temp_2_value == 'Фаренгейта (°F)':
            self.templabel.setText(f'{self.tempSpinBox.value()}')
        elif self.temp_value == 'Фаренгейта (°F)' and self.temp_2_value == 'Цельсия (°C)':
            result = (self.tempSpinBox.value() - 32) / 1.8
            self.templabel.setText(f'{result}')
        elif self.temp_value == 'Фаренгейта (°F)' and self.temp_2_value == 'Кельвина (°K)':
            result = (self.tempSpinBox.value() - 32) * 0.5555555556 + 273.15
            self.templabel.setText(f'{result}')

        elif self.temp_value == 'Кельвина (°K)' and self.temp_2_value == 'Фаренгейта (°F)':
            result = self.tempSpinBox.value() * 1.8 - 459.67
            self.templabel.setText(f'{result}')
        elif self.temp_value == 'Кельвина (°K)' and self.temp_2_value == 'Цельсия (°C)':
            result = self.tempSpinBox.value() - 273.15
            self.templabel.setText(f'{result}')
        elif self.temp_value == 'Кельвина (°K)' and self.temp_2_value == 'Кельвина (°K)':
            self.templabel.setText(f'{self.tempSpinBox.value()}')

    def time_convert(self):
        #   Конвертирую разные виды времени в другой вид
        if self.time_value == "Секунды (s)" and self.time_2_value == 'Секунды (s)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
        elif self.time_value == "Секунды (s)" and self.time_2_value == 'МИЛсекунды (ms)':
            result = self.timeSpinBox.value() * 1000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Секунды (s)" and self.time_2_value == 'Минуты (min)':
            result = self.timeSpinBox.value() / 60
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Секунды (s)" and self.time_2_value == 'Часы (h)':
            result = self.timeSpinBox.value() / 3600
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Секунды (s)" and self.time_2_value == 'Дни (d)':
            result = self.timeSpinBox.value() / 86400
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Секунды (s)" and self.time_2_value == 'Недели (wk)':
            result = self.timeSpinBox.value() / 604800
            self.timelabel.setText(f'{result}')

        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'Секунды (s)':
            result = self.timeSpinBox.value() / 1000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'МИЛсекунды (ms)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'Минуты (min)':
            result = self.timeSpinBox.value() / 60000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'Часы (h)':
            result = self.timeSpinBox.value() / 3600000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'Дни (d)':
            result = self.timeSpinBox.value() / 86400000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "МИЛсекунды (ms)" and self.time_2_value == 'Недели (wk)':
            result = self.timeSpinBox.value() / 604800000
            self.timelabel.setText(f'{result}')

        elif self.time_value == "Минуты (min)" and self.time_2_value == 'Секунды (s)':
            result = self.timeSpinBox.value() / 60
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Минуты (min)" and self.time_2_value == 'МИЛсекунды (ms)':
            result = self.timeSpinBox.value() / 60000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Минуты (min)" and self.time_2_value == 'Минуты (min)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
        elif self.time_value == "Минуты (min)" and self.time_2_value == 'Часы (h)':
            result = self.timeSpinBox.value() / 60
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Минуты (min)" and self.time_2_value == 'Дни (d)':
            result = self.timeSpinBox.value() / 1440
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Минуты (min)" and self.time_2_value == 'Недели (wk)':
            result = self.timeSpinBox.value() / 10080
            self.timelabel.setText(f'{result}')

        elif self.time_value == "Часы (h)" and self.time_2_value == 'Секунды (s)':
            result = self.timeSpinBox.value() / 3600
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Часы (h)" and self.time_2_value == 'МИЛсекунды (ms)':
            result = self.timeSpinBox.value() / 3600000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Часы (h)" and self.time_2_value == 'Минуты (min)':
            result = self.timeSpinBox.value() * 60
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Часы (h)" and self.time_2_value == 'Часы (h)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
        elif self.time_value == "Часы (h)" and self.time_2_value == 'Дни (d)':
            result = self.timeSpinBox.value() / 24
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Часы (h)" and self.time_2_value == 'Недели (wk)':
            result = self.timeSpinBox.value() / 168
            self.timelabel.setText(f'{result}')

        elif self.time_value == "Дни (d)" and self.time_2_value == 'Секунды (s)':
            result = self.timeSpinBox.value() * 86400
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Дни (d)" and self.time_2_value == 'МИЛсекунды (ms)':
            result = self.timeSpinBox.value() * 86400000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Дни (d)" and self.time_2_value == 'Минуты (min)':
            result = self.timeSpinBox.value() * 1440
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Дни (d)" and self.time_2_value == 'Часы (h)':
            result = self.timeSpinBox.value() * 24
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Дни (d)" and self.time_2_value == 'Дни (d)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
        elif self.time_value == "Дни (d)" and self.time_2_value == 'Недели (wk)':
            result = self.timeSpinBox.value() / 7
            self.timelabel.setText(f'{result}')

        elif self.time_value == "Недели (wk)" and self.time_2_value == 'Секунды (s)':
            result = self.timeSpinBox.value() / 604800
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Недели (wk)" and self.time_2_value == 'МИЛсекунды (ms)':
            result = self.timeSpinBox.value() / 604800000
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Недели (wk)" and self.time_2_value == 'Минуты (min)':
            result = self.timeSpinBox.value() * 10080
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Недели (wk)" and self.time_2_value == 'Часы (h)':
            result = self.timeSpinBox.value() * 168
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Недели (wk)" and self.time_2_value == 'Дни (d)':
            result = self.timeSpinBox.value() * 7
            self.timelabel.setText(f'{result}')
        elif self.time_value == "Недели (wk)" and self.time_2_value == 'Недели (wk)':
            self.timelabel.setText(f'{self.timeSpinBox.value()}')
