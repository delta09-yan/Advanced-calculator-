import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from math import sqrt, sin, cos, tan, radians
from sec_win import UnitConvertion

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QWidget" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>661</width>
    <height>581</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget" native="true">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>321</width>
     <height>581</height>
    </rect>
   </property>
   <widget class="QPushButton" name="addminbtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>30</pointsize>
     </font>
    </property>
    <property name="text">
     <string>+/-</string>
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
   <widget class="QPushButton" name="zerobtn">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>0</string>
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
   <widget class="QPushButton" name="combtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>.</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="eqbtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>480</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>=</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="onebtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>1</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="twobtn">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>2</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="threebtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>3</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="plusbtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>400</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>+</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="fourbtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>4</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="fivebtn">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>5</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="sixbtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>6</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="minusbtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>320</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>70</pointsize>
     </font>
    </property>
    <property name="text">
     <string>-</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="sevenbtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>7</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="eightbtn">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>8</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="ninebtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>9</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="multbtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>240</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>*</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>100</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="clearbtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>C</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="probtn">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>%</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="divbtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>/</string>
    </property>
    <property name="iconSize">
     <size>
      <width>75</width>
      <height>75</height>
     </size>
    </property>
   </widget>
   <widget class="QLCDNumber" name="result">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>311</width>
      <height>71</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="vvod">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>20</y>
      <width>311</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="staplebtn">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>160</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>50</pointsize>
     </font>
    </property>
    <property name="text">
     <string>()</string>
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
  <widget class="QStatusBar" name="statusbar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>3</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="modbtn">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>160</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>|x|</string>
   </property>
   <property name="iconSize">
    <size>
     <width>16</width>
     <height>16</height>
    </size>
   </property>
   <property name="autoRepeatInterval">
    <number>100</number>
   </property>
  </widget>
  <widget class="QPushButton" name="onedivx">
   <property name="geometry">
    <rect>
     <x>350</x>
     <y>320</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>1/x</string>
   </property>
  </widget>
  <widget class="QPushButton" name="cosbtn">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>240</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>cos</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pibtn">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>160</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>50</pointsize>
    </font>
   </property>
   <property name="text">
    <string>PI</string>
   </property>
  </widget>
  <widget class="QPushButton" name="secextbtn">
   <property name="geometry">
    <rect>
     <x>570</x>
     <y>240</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>x²</string>
   </property>
  </widget>
  <widget class="QPushButton" name="sqrtbtn">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>160</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>50</pointsize>
    </font>
   </property>
   <property name="text">
    <string>√</string>
   </property>
   <property name="iconSize">
    <size>
     <width>75</width>
     <height>75</height>
    </size>
   </property>
  </widget>
  <widget class="QPushButton" name="eextx">
   <property name="geometry">
    <rect>
     <x>450</x>
     <y>320</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>30</pointsize>
    </font>
   </property>
   <property name="text">
    <string>e^x</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ebtn">
   <property name="geometry">
    <rect>
     <x>570</x>
     <y>160</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>50</pointsize>
    </font>
   </property>
   <property name="text">
    <string>e</string>
   </property>
  </widget>
  <widget class="QPushButton" name="sinbtn">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>240</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>sin</string>
   </property>
  </widget>
  <widget class="QPushButton" name="xextybtn">
   <property name="geometry">
    <rect>
     <x>550</x>
     <y>320</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>30</pointsize>
    </font>
   </property>
   <property name="text">
    <string>x^y</string>
   </property>
  </widget>
  <widget class="QPushButton" name="tanbtn">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>240</y>
     <width>81</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>35</pointsize>
    </font>
   </property>
   <property name="text">
    <string>tan</string>
   </property>
  </widget>
  <widget class="QLabel" name="doplabel">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>80</y>
     <width>161</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>15</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Additional options</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="vvodext">
   <property name="geometry">
    <rect>
     <x>480</x>
     <y>420</y>
     <width>121</width>
     <height>20</height>
    </rect>
   </property>
   <property name="readOnly">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QPushButton" name="converbtn">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>490</y>
     <width>161</width>
     <height>71</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Push to do convert</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>450</y>
     <width>111</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>17</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Converter</string>
   </property>
  </widget>
  <widget class="QPushButton" name="qbtn">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>0</y>
     <width>75</width>
     <height>61</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>QUIT</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.sequence = ''
        self.sequence_2 = ''
        self.ext = ''
        self.answer = 0
        self.count = 0
        self.w = None

        self.vvodext.textEdited.connect(self.my_slot_function)

        self.clearbtn.clicked.connect(self.clear)
        self.divbtn.clicked.connect(self.div)
        self.multbtn.clicked.connect(self.mult)
        self.minusbtn.clicked.connect(self.min)
        self.plusbtn.clicked.connect(self.sub)
        self.eqbtn.clicked.connect(self.equal)
        self.combtn.clicked.connect(self.com)
        self.probtn.clicked.connect(self.procent)
        self.staplebtn.clicked.connect(self.staples)
        self.addminbtn.clicked.connect(self.addmin)

        self.onebtn.clicked.connect(self.one)
        self.twobtn.clicked.connect(self.two)
        self.threebtn.clicked.connect(self.three)
        self.fourbtn.clicked.connect(self.four)
        self.fivebtn.clicked.connect(self.five)
        self.sixbtn.clicked.connect(self.six)
        self.sevenbtn.clicked.connect(self.seven)
        self.eightbtn.clicked.connect(self.eight)
        self.ninebtn.clicked.connect(self.nine)
        self.zerobtn.clicked.connect(self.zero)

        self.modbtn.clicked.connect(self.mod)
        self.sqrtbtn.clicked.connect(self.sqr)
        self.pibtn.clicked.connect(self.p)
        self.ebtn.clicked.connect(self.e)
        self.sinbtn.clicked.connect(self.sin)
        self.cosbtn.clicked.connect(self.cos)
        self.tanbtn.clicked.connect(self.tan)
        self.secextbtn.clicked.connect(self.secexf)
        self.onedivx.clicked.connect(self.onedivxf)
        self.eextx.clicked.connect(self.eextxf)
        self.xextybtn.clicked.connect(self.xextyf)

        self.converbtn.clicked.connect(self.show_new_window)

        self.qbtn.clicked.connect(self.show_question_message)

    def one(self):
        self.sequence_2 = ''
        self.sequence = '%s1' % (self.sequence)
        self.sequence_2 = '%s1' % (self.sequence_2)


        self.vvod.setText('%s' % self.sequence)

    def two(self):
        self.sequence_2 = ''
        self.sequence = '%s2' % (self.sequence)
        self.sequence_2 = '%s2' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def three(self):
        self.sequence_2 = ''
        self.sequence = '%s3' % (self.sequence)
        self.sequence_2 = '%s3' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def four(self):
        self.sequence_2 = ''
        self.sequence = '%s4' % (self.sequence)
        self.sequence_2 = '%s4' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def five(self):
        self.sequence_2 = ''
        self.sequence = '%s5' % (self.sequence)
        self.sequence_2 = '%s5' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def six(self):
        self.sequence_2 = ''
        self.sequence = '%s6' % (self.sequence)
        self.sequence_2 = '%s6' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def seven(self):
        self.sequence_2 = ''
        self.sequence = '%s7' % (self.sequence)
        self.sequence_2 = '%s7' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def eight(self):
        self.sequence_2 = ''
        self.sequence = '%s8' % (self.sequence)
        self.sequence_2 = '%s8' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def nine(self):
        self.sequence_2 = ''
        self.sequence = '%s9' % (self.sequence)
        self.sequence_2 = '%s9' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def zero(self):
        self.sequence_2 = ''
        self.sequence = '%s0' % (self.sequence)
        self.sequence_2 = '%s0' % (self.sequence_2)

        self.vvod.setText('%s' % self.sequence)

    def clear(self):
        self.sequence = ''
        self.vvod.setText('')
        self.result.display('0')

    def sub(self):
        self.sequence = '%s+' % (self.sequence)
        self.vvod.setText('%s' % self.sequence)

    def min(self):
        self.sequence = '%s-' % (self.sequence)
        self.vvod.setText('%s' % self.sequence)

    def div(self):
        self.sequence = '%s/' % (self.sequence)
        self.vvod.setText('%s' % self.sequence)

    def mult(self):
        self.sequence = '%s*' % (self.sequence)
        self.vvod.setText('%s' % self.sequence)

    def equal(self):
        self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]
        if '+' in self.sequence:
            self.answer = round(eval(self.sequence), 5)
            self.sequence = self.answer
            self.sequence_2 = self.answer
            self.result.display('%s' % (self.answer))
        elif '-' in self.sequence:
            self.answer = round(eval(self.sequence), 5)
            self.sequence = self.answer
            self.sequence_2 = self.answer
            self.result.display('%s' % (self.answer))
        elif '*' in self.sequence:
            self.answer = round(eval(self.sequence), 5)
            self.sequence = self.answer
            self.sequence_2 = self.answer

            self.result.display('%s' % (self.answer))
        elif '/' in self.sequence:
            print(self.sequence_2)
            if '0' not in self.sequence:
                self.answer = eval(self.sequence)
                self.sequence = self.answer
                self.sequence_2 = self.answer
                print(self.answer)
                self.result.display('%s' % (self.answer))
            elif self.sequence_2 == '0':
                self.vvod.setText('НЕЛЬЗЯ ДЕЛИТЬ НА 0')
                self.result.display('ERROR')
                self.sequence = ''
        elif len(self.sequence) != 1:
            self.answer = round(eval(self.sequence), 5)
            self.sequence = self.answer
            self.sequence_2 = self.answer

            self.result.display('%s' % (self.answer))
        else:
            self.answer = round(eval(self.sequence_2), 5)
            self.sequence = self.answer
            self.sequence_2 = self.answer

            self.result.display('%s' % (self.answer))

    def procent(self):
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            leng = len(self.sequence) - len(self.sequence_2)

            self.sequence_2 = str(int(self.sequence_2) / 100)
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            leng = len(self.sequence) - len(self.sequence_2)

            self.sequence_2 = str(int(self.sequence_2) / 100)
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-') + 1:]

            leng = len(self.sequence) - len(self.sequence_2) - 1

            self.sequence_2 = str(int(self.sequence[:leng]) / 100 * int(self.sequence_2))

            self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]

            leng = len(self.sequence) - len(self.sequence_2) - 1

            self.sequence_2 = str(int(self.sequence[:leng]) / 100 * int(self.sequence_2))

            self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            if len(self.sequence) != 1:
                self.sequence = str(int(self.sequence) / 100)
                self.vvod.setText('%s' % (self.sequence))
            else:
                self.sequence_2 = str(int(self.sequence_2) / 100)
                self.sequence = self.sequence_2
                self.vvod.setText('%s' % (self.sequence_2))

    def staples(self):
        if self.sequence == '(':
            pass
        elif self.count != 0:

            self.count -= 1
            self.sequence = '%s(' % (self.sequence)
            self.vvod.setText('%s' % self.sequence)
        elif '*(' in self.sequence[-2:]:
            self.sequence = '%s(' % (self.sequence)
            self.count += 1
            self.vvod.setText('%s' % self.sequence)
        elif '(' not in self.sequence:
            self.sequence = '(%s' % (self.sequence)
            self.vvod.setText('%s' % self.sequence)
        elif '(' in self.sequence:

            if '1)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '2)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '3)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '4)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '5)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '6)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '7)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '8)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '9)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif '0)' in self.sequence[-2:]:
                self.sequence = '%s*(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)



            elif self.sequence[-2] == '(' and self.sequence[-1] == '1':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '2':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '3':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '4':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '5':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '6':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '7':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '8':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '9':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-2] == '(' and self.sequence[-1] == '0':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)


            elif self.sequence[-1] == '1':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '2':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '3':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '4':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '5':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '6':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '7':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '8':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '9':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '0':
                self.sequence = '%s)' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)
            elif self.sequence[-1] == '(':
                self.sequence = '%s(' % (self.sequence)
                self.vvod.setText('%s' % self.sequence)

            else:
                self.sequence = '(%s' % (self.sequence)
                self.count += 1
                self.vvod.setText('%s' % self.sequence)
        elif ')' in self.sequence:
            self.sequence = '(%s' % (self.sequence)
            self.vvod.setText('%s' % self.sequence)

    def addmin(self):
        self.vvod.setText('Press - button')

    def com(self):
        if self.sequence:
            if '.' not in self.sequence:
                self.sequence = '%s.' % (self.sequence)

                self.vvod.setText('%s' % self.sequence)
            elif '+' in self.sequence:
                self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]
                if '.' not in self.sequence_2:
                    self.sequence_2 = '%s.' % (self.sequence_2)

                    leng = len(self.sequence) - len(self.sequence_2)
                    self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
                    self.vvod.setText('%s' % self.sequence)
            elif '-' in self.sequence:
                self.sequence_2 = self.sequence[self.sequence.find('-') + 1:]
                if '.' not in self.sequence_2:
                    self.sequence_2 = '%s.' % (self.sequence_2)

                    leng = len(self.sequence) - len(self.sequence_2)
                    self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
                    self.vvod.setText('%s' % self.sequence)
            elif '/' in self.sequence:
                self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]
                if '.' not in self.sequence_2:
                    self.sequence_2 = '%s.' % (self.sequence_2)

                    leng = len(self.sequence) - len(self.sequence_2)
                    self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
                    self.vvod.setText('%s' % self.sequence)
            elif '*' in self.sequence:
                self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]
                if '.' not in self.sequence_2:
                    self.sequence_2 = '%s.' % (self.sequence_2)

                    leng = len(self.sequence) - len(self.sequence_2)
                    self.sequence = '%s%s' % (self.sequence[:leng + 1], self.sequence_2)
                    self.vvod.setText('%s' % self.sequence)

    def mod(self):
        leng = len(self.sequence) - len(self.sequence_2)
        try:
            if '-' in self.sequence[0]:
                self.sequence = abs(int(self.sequence))
                self.vvod.setText('%s' % self.sequence)
            elif '-' in self.sequence:
                self.sequence_2 = self.sequence[self.sequence.find('-'):]
                self.sequence = self.sequence[:self.sequence.find('-'):]
                print(self.sequence_2)

                self.sequence_2 = abs(int(self.sequence_2))
                self.sequence = '%s+%s' % (self.sequence, self.sequence_2)
                self.vvod.setText('%s' % self.sequence)
        except Exception:
            self.vvod.setText('ERROR')

    def sqr(self):
        leng = len(self.sequence) - len(self.sequence_2)

        if '-' in self.sequence:

            self.sequence_2 = self.sequence[self.sequence.find('-'):]
            if int(self.sequence_2) < 0:
                self.vvod.setText('ERROR')

        elif '+' in self.sequence:

            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]
            self.sequence_2 = sqrt(int(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)

        elif '/' in self.sequence:

            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]
            self.sequence_2 = sqrt(int(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '*' in self.sequence:

            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]
            self.sequence_2 = sqrt(int(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = sqrt(int(self.sequence))
            self.vvod.setText('%s' % self.sequence)

    def p(self):
        if self.sequence[:12] == '2.7182818285':
            self.sequence = '%s*3.1415926536' % (self.sequence)
        else:
            self.sequence = '%s3.1415926536' % (self.sequence)
        self.sequence_2 = '%s3.1415926536' % (self.sequence_2)
        self.vvod.setText('%s' % self.sequence)

    def e(self):
        if self.sequence[:12] == '3.1415926536':
            self.sequence = '%s*2.7182818285' % (self.sequence)
        else:
            self.sequence = '%s2.7182818285' % (self.sequence)
        self.sequence_2 = '%s2.7182818285' % (self.sequence_2)
        self.vvod.setText('%s' % self.sequence)

    def sin(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(sin(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(sin(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(sin(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(sin(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = radians(int(self.sequence))
            self.sequence = str(sin(self.sequence))
            self.vvod.setText('%s' % self.sequence)

    def cos(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(cos(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(cos(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(cos(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(cos(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = radians(int(self.sequence))
            self.sequence = str(cos(self.sequence))
            self.vvod.setText('%s' % self.sequence)

    def tan(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(tan(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(tan(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(tan(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]

            self.sequence_2 = radians(int(self.sequence_2))
            self.sequence_2 = str(tan(self.sequence_2))
            self.sequence = '%s%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = radians(int(self.sequence))
            self.sequence = str(tan(self.sequence))
            self.vvod.setText('%s' % self.sequence)

    def secexf(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            self.sequence_2 = str(int(self.sequence_2) ** 2)
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            self.sequence_2 = str(int(self.sequence_2) ** 2)
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-'):]

            self.sequence_2 = str(int(self.sequence_2) ** 2)
            self.sequence = '%s+%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]

            self.sequence_2 = str(int(self.sequence_2) ** 2)
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = str(int(self.sequence) ** 2)
            self.vvod.setText('%s' % self.sequence)

    def onedivxf(self):
        self.sequence = '%s1/' % (self.sequence)
        self.sequence_2 = '%s1' % (self.sequence_2)
        self.vvod.setText('%s' % self.sequence)

    def eextxf(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if self.sequence == '':
            self.sequence = '%s' % (str(2.7182818285 ** int(self.ext)))
            self.vvod.setText('%s' % self.sequence)
        elif '*' in self.sequence[-1]:
            self.sequence_2 = str(2.7182818285 ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence, self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence[-1]:
            self.sequence_2 = str(2.7182818285 ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence, self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence[-1]:
            self.sequence_2 = str(2.7182818285 ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence, self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence[-1]:
            self.sequence_2 = str(2.7182818285 ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence, self.sequence_2)
            self.vvod.setText('%s' % self.sequence)

    def xextyf(self):
        leng = len(self.sequence) - len(self.sequence_2)
        if '*' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('*') + 1:]

            self.sequence_2 = str(int(self.sequence_2) ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '/' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('/') + 1:]

            self.sequence_2 = str(int(self.sequence_2) ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '-' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('-'):]

            self.sequence_2 = str(int(self.sequence_2) ** int(self.ext))
            self.sequence = '%s+%s' % (self.sequence[:leng - 1], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        elif '+' in self.sequence:
            self.sequence_2 = self.sequence[self.sequence.find('+') + 1:]
            self.sequence_2 = str(int(self.sequence_2) ** int(self.ext))
            self.sequence = '%s%s' % (self.sequence[:leng], self.sequence_2)
            self.vvod.setText('%s' % self.sequence)
        else:
            self.sequence = str(int(self.sequence) ** int(self.ext))
            self.vvod.setText('%s' % self.sequence)

    def my_slot_function(self, text):
        self.ext = text

    def show_new_window(self, checked):
        if self.w is None:
            self.w = UnitConvertion()
        self.w.show()

    def show_question_message(self):
        button = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure you want to quit?",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:
            if self.w:
                self.close()
                self.w.close()
            else:
                self.close()
        else:
            print("stay")
