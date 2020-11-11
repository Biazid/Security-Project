import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
from pathlib import Path  
import math

filelist = []
user=""
passw=""

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

def nxtprimegen(n):
    m = n
    n = n + 100
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            if p > m:
                return p
            else:
                val = p

    return val


def rsa(p,q):
    p=nxtprimegen(p)
    q=nxtprimegen(q)
    print("prime: ", p, " ", q)
    n = p * q
    print("n: ", n)
    tor = (p - 1) * (q - 1)
    e = 2
    while (1):
        if math.gcd(e, tor) == 1:
            break
        else:
            e += 1
    print("public key: ", e)
    d = modInverse(e, tor)
    if d == 1:
        print("no multiplicative_inverse")
        return

    print("private key: ", d)
    return e, d, n



class App(QMainWindow):
    n=0
    e=0
    d=0
    pp=0
    qq=0
    filename=""
    def __init__(self):
        super().__init__()
        self.title = 'File Encryptor & Decryptor'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 200
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray )
        self.setPalette(p)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.label1 = QLabel("Enter Username: " , self)
        self.label1.move(20, 10)
        self.label1.resize(280, 40)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 17)
        self.textbox.resize(300, 25)

        self.label2 = QLabel("Enter Password: ", self)
        self.label2.move(20, 50)
        self.label2.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 57)
        self.textbox2.resize(300, 25)
        
        
        
        self.label3 = QLabel("Your files are shown", self)
        self.label3.move(20, 20)
        self.label3.resize(280, 20)
        self.label3.hide()

        self.textbox3 = QTextEdit(self)
        self.textbox3.move(150, 30)
        self.textbox3.resize(300, 100)
        self.textbox3.hide()
        
        # Create a button in the window
        self.button4 = QPushButton('Login', self)
        self.button4.move(150, 130)
        self.button4.clicked.connect(self.login)
#        self.button2.hide()
        
        self.button5 = QPushButton('Register', self)
        self.button5.move(350, 130)
        self.button5.clicked.connect(self.register)
#        self.button2.hide()
        
        self.button = QPushButton('Encrypt', self)
        self.button.move(20, 150)
        self.button.clicked.connect(self.encrypt)
        self.button.hide()

        self.button2 = QPushButton('Open a file', self)
        self.button2.move(170, 150)
        self.button2.clicked.connect(self.openFileNameDialog)
        self.button2.hide()

        self.button3 = QPushButton('Decrypt', self)
        self.button3.move(350, 150)
        self.button3.clicked.connect(self.decrypt)
        self.button3.hide()

        self.show()


    def login(self):
        global user
        global passw
        user = self.textbox.text()
        pas = self.textbox2.text()
        pas = pas.strip()
        filepath='C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt'
        if not os.path.exists(filepath):
            QMessageBox.question(self, 'Message - pythonspot.com', "Not register" , QMessageBox.Ok, QMessageBox.Ok)
            
        else:
            f1 = open(r'C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt', 'r') 
            passw=f1.readline()
            passw = passw.strip()
#            passw=passw.split(' ')[0]
            print(passw)
            if pas == passw:
                global filelist
                strs=""
                for x in f1:
                    strs+=x
                    filelist.append(x.strip())
                self.textbox3.append(strs)
                self.textbox3.setReadOnly(Qt.Checked)
#                print(strs)
                print(filelist)
                f1.close()
                self.button4.hide()
                self.button5.hide()
                self.button.show()
                self.button2.show()
                self.button3.show()
                self.label1.hide()
                self.label2.hide()
                self.textbox.hide()
                self.textbox2.hide()
                self.label3.show()
                self.textbox3.show()
            else:
                QMessageBox.question(self, 'Message - pythonspot.com', "Password not maching" , QMessageBox.Ok, QMessageBox.Ok)
            
    def register(self):
        global user,passw
        user = self.textbox.text()
        filepath='C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt'
        if os.path.exists(filepath):
            QMessageBox.question(self, 'Message - pythonspot.com', "Already exist" , QMessageBox.Ok, QMessageBox.Ok)
            
        else:
            pas = self.textbox2.text()
            pas = pas.strip()
            if not pas:
                QMessageBox.question(self, 'Message - pythonspot.com', "Enter right password" , QMessageBox.Ok, QMessageBox.Ok)
            else:
                passw=pas
                f1 = open(r'C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt', 'w') 
                f1.write(pas)
                f1.close
    
                self.textbox3.setReadOnly(Qt.Checked)
                print(filelist)
                self.button4.hide()
                self.button5.hide()
                self.button.show()
                self.button2.show()
                self.button3.show()
                self.label1.hide()
                self.label2.hide()
                self.textbox.hide()
                self.textbox2.hide()
                self.label3.show()
                self.textbox3.show()
            
        
    def encrypt(self):
        nam=Path(self.filename).name
        if self.filename=="":
            QMessageBox.question(self, 'Message - pythonspot.com', "Please select a file" , QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open(self.filename, "rb") as image:
                f = image.read()
                msg = bytearray(f)
            en = []
            de = []
            print("msg: ", msg)
            for x in msg:
                en.append(pow(x, self.e, self.n))
            print("\nencrypt msg: ", en)
            
            print(self.filename+'.encrypt')
            ss = ""
            f3 = open(self.filename+'.encrypt', 'w')
            for x in en:
                ss += (str(x) + " ")
            f3.write(ss)
            
            global user
            f = open(r'C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt', "a")
            f.write("\n"+nam)
            f.close()
            filelist.append(nam)
            print(nam)
            self.textbox3.append(nam)
            if os.path.isfile(self.filename):
                os.remove(self.filename)

    def decrypt(self):
        global passw,filelist
        print(self.filename)
        nam=Path(self.filename).name
        nam2=os.path.splitext(nam)[0]
        if not nam2 in filelist:
            QMessageBox.question(self, 'Message - pythonspot.com', "Not your file" , QMessageBox.Ok, QMessageBox.Ok)
            self.filename=""
        textboxValue = 299
        self.de_key = int(textboxValue)
        self.n = 565
#        textboxValue2 = self.textbox3.text()
#        self.file_type = textboxValue2
        en = []
        de = []
        if self.filename=="":
            QMessageBox.question(self, 'Message - pythonspot.com', "Please select a file" , QMessageBox.Ok, QMessageBox.Ok)
        else:
            f3 = open(self.filename, 'r')
            str2=f3.read()
            en2 = str2.split(" ")
            for x in en2:
                if len(x) > 0:
                    en.append(int(x))
            for x in en:
                de.append(pow(x, self.de_key, self.n))
            bytearray(de[:4])
            
            p = Path(self.filename)
            print(p.parent) 
            f2 = open(os.path.join(p.parent, nam2), 'wb')
            f2.write(bytearray(de))
            f2.close()
            print("decrypt msg: ", de)
            
            global user
            filelist.remove(nam2)
            print(filelist)
            f = open(r'C:/Users/Biazid Bostame/Desktop/1507053/.idea/'+user+'.txt', "w")
            f.write(passw+"\n")
            strs=""
            for x in filelist:
                if strs=="":
                    strs+=x
                else:
                    strs+="\n"+x
            f.write(strs)
            f.close()
            f3.close()
            self.textbox3.setText(strs)
            print(strs)
            if os.path.isfile(self.filename):
                os.remove(self.filename)


    def openFileNameDialog(self):
        p=111
        self.pp=int(p)
        q=3
        #priv=299,n=565
        self.qq = int(q)
        self.e, self.d, self.n = rsa(self.pp,self.qq)
        
        self.filename==""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.filename = fileName
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())