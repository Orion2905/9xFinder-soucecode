import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, Qt, QEvent, QTimer, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPen)
from PySide6.QtWidgets import *

from threading import Thread
import win32com.client

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLineEdit
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QWidget

from PIL import Image
import imagehash
import _osx_support
import time
import os

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import sys
import sqlite3
from sqlite3 import Error
import subprocess

from ui_main import *
from showinfm import show_in_file_manager

import platform
import userpaths

class Database:
    def __init__(self) -> None:
        self.CONN = None
        newpath = f'{userpaths.get_my_documents()}/9xFINDER'.replace("/", os.sep)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        self.DB_FILE = f"{userpaths.get_my_documents()}/9xFINDER/DATABASE.db".replace("/", os.sep)
        print(self.DB_FILE)

        try: 
            self.CONN = sqlite3.connect(self.DB_FILE)
            print(sqlite3.version)
        except Error as e:
            print(e)
        
        self.create_table("users", "id integer PRIMARY KEY, fullname text NOT NULL, username text NOT NULL, email text NOT NULL, password text NOT NULL, firstAccess text NOT NULL, stayLogged text NOT NULL, pc text NOT NULL")
        self.create_table("directories", "id integer PRIMARY KEY, path text NOT NULL")
        self.create_table("images", "id integer PRIMARY KEY, mainImage text NOT NULL, similarImage text NOT NULL")
        #self.select_data("directories")
        #self.insert_data_2("directories", "path", ("TEst",))
        #self.drop_table("Users")
        #self.delete("images")
        if not self.select_data_where("users", f"username='TestAccount' AND password = '1234';"):
            self.insert_data("users", "fullname, username, email, password, firstAccess, stayLogged, pc", ("Test Account", "TestAccount", "test@tes.com", "1234", "True", "False", "None",))
        self.select_data("users")

    def drop_table(self, table_name):
        sql = f''' DROP TABLE {table_name}'''
        cur =self.CONN.cursor()
        cur.execute(sql)
        self.CONN.commit()

    def create_table(self, table_name, columns):
        sql_create_table = f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns})"""
        if self.CONN is not None:
            try:
                c = self.CONN.cursor()
                c.execute(sql_create_table)
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")
    
    def insert_data(self, table_name, columns, data):
        sql = f''' INSERT INTO {table_name}({columns})
              VALUES(?,?,?,?,?,?,?) '''
        cur =self.CONN.cursor()
        cur.execute(sql, data)
        self.CONN.commit()

        return cur.lastrowid
    
    def insert_data_2(self, table_name, columns, data):
        
        sql = f''' INSERT INTO {table_name}({columns})
              VALUES(?) '''
        cur =self.CONN.cursor()
        cur.execute(sql, data)
        self.CONN.commit()

        return cur.lastrowid
    
    def insert_data_3(self, table_name, columns, data):
        
        sql = f''' INSERT INTO {table_name}({columns})
              VALUES(?, ?) '''
        cur =self.CONN.cursor()
        cur.execute(sql, data)
        self.CONN.commit()

        return cur.lastrowid

    def select_data(self, table_name):
        cur = self.CONN.cursor()
        cur.execute(f"SELECT * FROM {table_name}")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        return rows

    def delete(self, table_name):
        sql = f''' delete from {table_name} '''
        cur =self.CONN.cursor()
        cur.execute(sql)
        self.CONN.commit()

    def select_data_where(self, table_name, condition):
        cur = self.CONN.cursor()
        cur.execute(f"SELECT * FROM {table_name} WHERE {condition}")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        return rows
    
    def update_data(self, table_name, variation, condition):
        sql = f''' UPDATE {table_name}
              SET {variation}
              WHERE {condition}'''
        cur = self.CONN.cursor()
        cur.execute(sql)
        self.CONN.commit()
    
    def delete_data_where(self, table_name, condition):
        cur = self.CONN.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.CONN.commit()

class Login:
    def __init__(self):
        
        self.DB = Database()
    
    def login(self, password, username="TestAccount", check="False"):
        self.DB = Database()
        if not self.DB.select_data_where("users", f"username='{username}' AND password = '{password}';"):  # An empty result evaluates to False.
            #print("Login failed")
            return False
        else:
            self.DB = Database()
            data = self.DB.select_data_where("users", f"username='{username}' AND password = '{password}';")
            #print("Welcome")
            #print(data[0][5])
            if data[0][5] == "True":
                #self.DB.insert_data("users", "fullname, username, email, password, firstAccess, stayLogged, pc", ("Test Account", "TestAccount", "test@tes.com", "1234", "True", "False", "None",))
                self.DB = Database()
                self.DB.update_data(table_name="users", variation="firstAccess='False'", condition=f"username='{username}' AND password = '{password}';")
                self.DB.update_data(table_name="users", variation=f"pc='{platform.node()}'", condition=f"username='{username}' AND password = '{password}';")
                self.DB = Database()
                return True
            else:
                self.DB = Database()
                my_pc = platform.node()
                data = self.DB.select_data_where("users", f"username='{username}' AND password = '{password}' AND pc = '{my_pc}';")
                print(1, data)
                if not self.DB.select_data_where("users", f"username='{username}' AND password = '{password}' AND pc = '{my_pc}';"):  # An empty result evaluates to False.
                #print("Login failed")
                    return False
                else:
                    print(data)
                    return True
        
class ImagesInImages:
    def __init__(self, dirname, main_image, obj, parent, threads_to_use, stop, accuracy) -> None:
        self.main_image = main_image
        self.obj = obj
        self.right_files = []
        self.parent = parent
        self.parent.ui.pushButton_18.setEnabled(False)
        self.cnt = 0
        self.threads_to_use = threads_to_use
        self.stop = False
        self.accuracy = accuracy
        print("Accuracy", self.accuracy)

    def split(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    
    def get_images_from_folders(self):
        self.parent.ui.label.setText(f"9x Finder © {time.strftime('%Y')} - Loading all files...")
        db = Database()
        main_folders = db.select_data("directories")
        all_folders = []
        for main_folder in main_folders:
            all_folders_inside = [x[0] for x in os.walk(f"{main_folder[1].replace('/', os.sep)}")]
            for folder in all_folders_inside:
                all_folders.append(folder)
        files = []
        for folder in all_folders:
            onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            for file in onlyfiles:
                files.append(folder+os.sep+file)
        print("QUI", files)
        images_extensions = ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]
        self.right_files = []
        for x in range(len(files)):          
            test = files[x].split(".")[1]
            if test in images_extensions:
                self.right_files.append(files[x])
        print("QUI", self.right_files)
        all_files_lenght = len(self.right_files)
        self.parent.ui.progressBar_2.setMaximum(all_files_lenght)
        t = list(self.split(self.right_files, int(self.threads_to_use)))
        self.parent.ui.progressBar_2.setFormat("%p%")   
        for x in t:
            if self.stop:
                self.parent.ui.progressBar_2.setFormat("Process stopped!")   
                self.parent.ui.pushButton_15.setEnabled(False)
                break
            t1 = Thread(target=self.compare_image, args=(x,))
            t1.start()

    def compare_image(self, right_images):
        db = Database()
        for image in right_images:
            print(self.stop)
            if self.stop:
                self.parent.ui.progressBar_2.setFormat("Process stopped!")   
                self.parent.ui.pushButton_15.setEnabled(False)
                break
            self.parent.ui.label.setText(f"9x Finder © {time.strftime('%Y')} - Comparing the images...")
            if not db.select_data_where("images", f"mainImage='{str(self.main_image)}' and similarImage='{str(image.replace(os.sep, '/'))}';"):
                try:
                    main_response = False
                    img_rgb = cv.imread(image)
                    assert img_rgb is not None, "file could not be read, check with os.path.exists()"
                    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
                    template = cv.imread(self.main_image, cv.IMREAD_GRAYSCALE)
                    assert template is not None, "file could not be read, check with os.path.exists()"
                    w, h = template.shape[::-1]
                    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
                    threshold = float(self.accuracy)
                    loc = np.where( res >= threshold)
                    #print(loc)
                    if len((loc[0])) > 0:
                        main_response = True
                        print("Imgae Found!")
                        self.parent.ui.label.setText(f"9x Finder © {time.strftime('%Y')} - Image found...")
                        if not db.select_data_where("images", f"mainImage='{str(self.main_image)}' and similarImage='{str(image.replace(os.sep, '/'))}';"):
                            db.insert_data_3(table_name="images", columns="mainImage, similarImage", data=(str(self.main_image),str(image.replace(os.sep, "/")),))
                        #self.obj.addItem(image.replace(os.sep, "/"))
                    else:
                        main_response = False
                        print("Imgae Not Found!")
                    """for pt in zip(*loc[::-1]):
                        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)"""
                    #cv.imwrite('res.png',img_rgb)
                except Exception as e:
                    print(e)
                    main_response = False
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            else:
                main_response = False
            
            self.cnt += 1
            self.parent.ui.progressBar_2.setValue(self.cnt)
             
        
        self.parent.ui.label.setText(f"9x Finder © {time.strftime('%Y')} - Process complete!")
        time.sleep(1)
        
        self.parent.ui.pushButton_18.setEnabled(True)
        return main_response
        
class DuplicateRemover:
    def __init__(self,parent,dirname,hash_size = 8,):
        self.dirname = dirname
        self.hash_size = hash_size
        self.parent = parent
        
    def find_duplicates(self):
        db = Database()
        main_folders = db.select_data("directories")
        all_folders = []
        for main_folder in main_folders:
            all_folders_inside = [x[0] for x in os.walk(f"{main_folder[1].replace('/', os.sep)}")]
            for folder in all_folders_inside:
                all_folders.append(folder)
        
        files = []
        for folder in all_folders:
            onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            for file in onlyfiles:
                files.append(folder+os.sep+file)
        print("QUI", files)
        images_extensions = ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]
        right_files = []
        for x in range(len(files)):          
            test = files[x].split(".")[1]
            if test in images_extensions:
                right_files.append(files[x])
        print("QUI", right_files)
        hashes = {}
        duplicates = []
        print("Finding Duplicates Now!\n")
        for image in right_files:
            with Image.open(os.path.join(self.dirname,image)) as img:
                temp_hash = imagehash.average_hash(img, self.hash_size)
                if temp_hash in hashes:
                    print("Duplicate {} \nfound for Image {}!\n".format(image,hashes[temp_hash]))
                    duplicates.append(image)
                else:
                    hashes[temp_hash] = image
              
    def find_similar(self,location,similarity=80):
        self.parent.ui.label.setText(f"9x Finder © {time.strftime('%Y')} - Loading all files...")
        db = Database()
        main_folders = db.select_data("directories")
        all_folders = []
        for main_folder in main_folders:
            all_folders_inside = [x[0] for x in os.walk(f"{main_folder[1].replace('/', os.sep)}")]
            for folder in all_folders_inside:
                all_folders.append(folder)
        files = []
        for folder in all_folders:
            onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            for file in onlyfiles:
                files.append(folder+os.sep+file)
        print("QUI", files)
        images_extensions = ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]
        self.right_files = []
        for x in range(len(files)):          
            test = files[x].split(".")[1]
            if test in images_extensions:
                self.right_files.append(files[x])
        print("QUI", self.right_files)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        similar_images = []
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        print("Finding Similar Images to {} Now!\n".format(location))
        for image in self.right_files:
            with Image.open(os.path.join(self.dirname,image)) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    print("{} image found {}% similar to {}".format(f"{image}",similarity,location))
                    similar_images.append(f"{image}")
        
        for i in similar_images:
                self.parent.ui.listWidget.addItem(i.replace(os.sep, "/"))
        return similar_images

class MainAppScreen(QMainWindow):
    def __init__(self):
        super(MainAppScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.last_page = 1
        self.ui.Pages.setCurrentIndex(0)
        self.iw = ImagesInImages
        QtGui.QImageReader.setAllocationLimit(0)
        self.ui.pushButton.setEnabled(False)

        self.oldPos = self.pos()
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_10.clicked.connect(lambda: self.accept_login(Login().login(password=self.ui.lineEdit_2.text())))
        self.ui.pushButton_3.clicked.connect(lambda: self.switch_page(2, 1))
        self.ui.pushButton_4.clicked.connect(lambda: self.switch_page(3, 1))
        self.ui.pushButton.clicked.connect(lambda: self.ui.Pages.setCurrentIndex(self.last_page))
        self.ui.pushButton_11.clicked.connect(self.toggleVisibility)
        self.ui.pushButton_5.clicked.connect(lambda: self.upload_file(self.ui.lineEdit_3))
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.lineEdit_4.setReadOnly(True)
        self.ui.ErrorLabel.setHidden(True)
        
        self.ui.horizontalSlider_2.setMinimum(1)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.update_slider(label=self.ui.label_17, value=self.ui.horizontalSlider.value()))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.update_slider(label=self.ui.label_10, value=self.ui.horizontalSlider_2.value()))
        self.ui.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget.itemChanged.connect(lambda: self.ui.label_13.setText(f"0/{str(self.ui.listWidget.count())}"))
        self.ui.listWidget.itemSelectionChanged.connect(self.change_selection)

        self.ui.label.setText(f"9x Finder © {time.strftime('%Y')}")

        self.ui.pushButton_9.clicked.connect(lambda: self.ui.listWidget.setCurrentRow(self.ui.listWidget.currentRow()+1))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.listWidget.setCurrentRow(self.ui.listWidget.currentRow()-1))

        self.ui.pushButton_15.clicked.connect(self.stop)
        self.ui.pushButton_15.setEnabled(False)
    
        self.ui.pushButton_8.clicked.connect(lambda: self.open_file_in_directory(self.ui.lineEdit_4.text()))
        self.ui.pushButton_12.clicked.connect(self.add_url)

        self.ui.pushButton_18.clicked.connect(lambda: self.start_searching(mode=1))
        self.ui.pushButton_6.clicked.connect(lambda: self.start_searching(mode=0))
        self.ui.pushButton_17.clicked.connect(lambda: self.upload_file(self.ui.lineEdit_6))
        self.ui.pushButton_13.clicked.connect(self.remove_url)
        self.ui.pushButton_14.clicked.connect(self.update_data)
        self.ui.label_6.setAcceptDrops(True)

        self.ui.pushButton_16.clicked.connect(self.update_listwidget2)
        self.ui.pushButton_19.clicked.connect(self.delete_data_from_listwidget)

        self.update_listwidget()


        self.show()

    def delete_data_from_listwidget(self):
        db = Database()
        main_image = self.ui.lineEdit_6.text()
        list_of_images = self.ui.listWidget
        items = []
        for x in range(list_of_images.count()):
            print(x, list_of_images.item(x))
            items.append(list_of_images.item(x).text())
        for item in items:  
            db.delete_data_where(table_name="images", condition=f"mainImage='{main_image}' and similarImage='{item}'")
        

    def stop(self):
        self.iw.stop = True

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
            self.ui.label_6.setStyleSheet(f"image: url({f});")
            try:
                self.ui.lineEdit_3.setText(f)
                self.ui.lineEdit_6.setText(f)
                #self._pixmap = QPixmap(self.filename[0])
                #print(self.filename)
                if f:
                    self.ui.label_6.setStyleSheet(f"image: url({f});")
                else:
                    pass
                # self.ui.label_6.setScaledContents(True)
            except:
                pass

    def update_listwidget2(self):
        db = Database()
        data = db.select_data_where("images", f"mainImage = '{self.ui.lineEdit_6.text()}'")
        item = self.ui.listWidget
        item.clear()
        items = []
        for x in range(item.count()):
            print(x, item.item(x))
            items.append(item.item(x).text())
        for x in data:
            if x[1] not in items:
                self.ui.listWidget.addItem(x[2])

    def update_listwidget(self):
        db = Database()
        data = db.select_data("directories")
        item = self.ui.listWidget_2
        items = []
        for x in range(item.count()):
            print(x, item.item(x))
            items.append(item.item(x).text())
        for x in data:
            if x[1] not in items:
                self.ui.listWidget_2.addItem(x[1])
        
    def open_file_in_directory(self, file):
        file = file.replace("/", os.sep)
        if file:
            print(file)
            subprocess.Popen(rf'explorer /select, "{file}"')
 
    def change_selection(self):
        self.ui.label_13.setText(f"{self.ui.listWidget.currentRow()+1}/{str(self.ui.listWidget.count())}")
        #print(self.ui.listWidget.currentItem().text())
        print(self.ui.listWidget.currentItem().text().replace(os.sep, '/'))
        self.ui.label_7.setStyleSheet(f"image: url({self.ui.listWidget.currentItem().text()});")
        self.ui.lineEdit_4.setText(self.ui.listWidget.currentItem().text())

    def update_data(self):
        self.ui.progressBar.setFormat("Updating data...")
        item = self.ui.listWidget_2
        items = []
        for x in range(item.count()):
            print(x, item.item(x))
            items.append(item.item(x).text())
        db = Database()
        print("QUI", items)
        for item in items:
            if not db.select_data_where("directories", f"path='{str(item)}';"):
                db.insert_data_2(table_name="directories", columns="path", data=(str(item),))
        database_items = db.select_data(table_name="directories")
        for j in database_items:
            if j[1] not in items:
                print("j",j)
                db.delete_data_where(table_name="directories", condition=f"id='{j[0]}';")
        self.update_listwidget()
        time.sleep(1)
        self.ui.progressBar.setFormat("Updating completed...")

    def remove_url(self):
        listItems=self.ui.listWidget_2.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(item))

    def add_url(self):
        def search_urls():
            self.ui.progressBar.setValue(0)
            self.ui.progressBar.setFormat("Loading files...")
            #a = [x[0] for x in os.walk(f"{file.replace('/', os.sep)}")]
            #self.ui.progressBar.setMaximum(len(a))
            #print(a)
                
            datoMinimo = 0
            #datoMassimo = len(a)
            valoreNormalizzato = 1
            #print(len(a))
            """for i in range(len(a)):
                valoreDato = i  # Cambia questo valore con i tuoi dati effettivi

                valoreNormalizzato = ((valoreDato - datoMinimo) / (datoMassimo - datoMinimo)) * 100
                #time.sleep(0.1)
                self.ui.progressBar.setValue(valoreNormalizzato)
                print(valoreNormalizzato)

            if valoreNormalizzato < 100 and valoreNormalizzato >98:
                valoreNormalizzato +=2"""
            item = self.ui.listWidget_2
            items = []
            for x in range(item.count()):
                print(x, item.item(x))
                items.append(item.item(x).text())
            time.sleep(1)
            if file not in items:
                self.ui.listWidget_2.addItem(file)
            self.ui.progressBar.setFormat("File loaded, click on update data to update the database...")
            return None
        try:
            file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            #self._pixmap = QPixmap(self.filename[0])
            #print(self.filename)
            if file:
                t1 = Thread(target=search_urls)
                t1.start()
                #a = [x[0] for x in os.walk(f"{file.replace('/', os.sep)}")]
                #self.ui.progressBar.setMaximum(len(a)
            else:
                pass
            # self.ui.label_6.setScaledContents(True)
        except:
            pass

    def start_searching(self, mode):
        self.ui.listWidget.clear()
        db = Database()
        if mode == 0:
            
            # Remove Duplicates
            dr = DuplicateRemover(dirname="", parent=self)

            # Find Similar Images 
            t1 = Thread(target=dr.find_duplicates)
            t1.start()
            t2 = Thread(target=dr.find_similar, args=(self, self.ui.lineEdit_3.text(),int(float(self.ui.label_17.text())),))
            t2.start()
           
        elif mode == 1:
            self.iw = ImagesInImages("", self.ui.lineEdit_6.text(), self.ui.listWidget, self, threads_to_use=self.ui.horizontalSlider_2.value(), stop=False, accuracy=self.ui.doubleSpinBox.value())
            t1 = Thread(target=self.iw.get_images_from_folders)
            t1.start()
            self.ui.pushButton_15.setEnabled(True)
            #time.sleep(20)
            #iw.stop = True
            data = db.select_data_where("images", f"mainImage='{str(self.ui.lineEdit_6.text().replace(os.sep, '/'))}';")
            if data:
                for i in data:
                    self.ui.listWidget.addItem(i[2])

    def update_slider(self, value, label):
        label.setText(str(float(value)))

    def upload_file(self, label_):
        db = Database()
        try:
            self.filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
            #self._pixmap = QPixmap(self.filename[0])
            #print(self.filename)
            data = db.select_data_where("images", f"mainImage='{str(self.filename[0].replace(os.sep, '/'))}';")
            if self.filename[0]:
                label_.setText(self.filename[0])
                self.ui.label_6.setStyleSheet(f"image: url({self.filename[0]});")
                if data:
                    for i in data:
                        self.ui.listWidget.addItem(i[2])
            else:
                pass
            # self.ui.label_6.setScaledContents(True)
        except:
            pass

    def toggleVisibility(self):
        if self.ui.lineEdit_2.echoMode()==QLineEdit.Normal:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
            icon = QtGui.QIcon(u":/UI_ICONS/images/icons/eye-slash.svg")
            self.ui.pushButton_11.setIcon(icon)
        else:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
            icon = QtGui.QIcon(u":/UI_ICONS/images/icons/eye.svg")
            self.ui.pushButton_11.setIcon(icon)

    def accept_login(self, x):
        if x:
            self.ui.Pages.setCurrentIndex(1)
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.ErrorLabel.setHidden(False)
            self.ui.ErrorLabel.setText("Login failed")
    
    def switch_page(self, page, last_page):
        self.ui.Pages.setCurrentIndex(page)
        self.last_page = last_page

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


if __name__ == "__main__":
    Database()
    app = QtWidgets.QApplication(sys.argv)
    window = MainAppScreen()
    sys.exit(app.exec())
