# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:35:47 2023

@author: ceyda
"""
#%%

#-----KÜTÜPHANE-----#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaUI import *

#%%

#-----UYGULAMA OLUŞTUR-----#
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

#%%

#-----VERİ TABANI OLUŞTUR-----#
import sqlite3
global curs
global conn
conn=sqlite3.connect('veritabani_KİTAPKAYIT.db')
curs = conn.cursor()  
sorguCreTblKitap=("CREATE TABLE IF NOT EXISTS Kitap(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 KitapNo TEXT NOT NULL UNIQUE,                        \
                 KitapAd TEXT NOT NULL,                          \
                 YazarAd TEXT NOT NULL,                       \
                 SayfaSayisi TEXT NOT NULL,                           \
                 Tur TEXT NOT NULL,                              \
                 Yayinevi TEXT NOT NULL,                           \
                 KitapBaslangic TEXT NOT NULL,                            \
                 KitapBitis TEXT NOT NULL,                               \
                 Derecelendir TEXT NOT NULL,                               \
                 Dusunceler TEXT NOT NULL)")
curs.execute(sorguCreTblKitap)
conn.commit()

#%%

#-----KAYIT EKLE-----#
def KAYIT_EKLE():
    _leKitapNo=ui.leKitapNo.text() #içeriğini bu şekilde aldık
    _leKitapAd=ui.leKitapAd.text()
    _leYazarAd=ui.leYazarAd.text()
    _leSayfaSayisi=ui.leSayfaSayisi.text()
    _leTur=ui.leTur.text()
    _leYayinevi=ui.leYayinevi.text()
    _cwBaslangic=ui.cwBaslangic.selectedDate().toString(QtCore.Qt.ISODate)
    _calendarWidget_2=ui.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)
    _KitabiDerecelendir=ui.KitabiDerecelendir.value()
    _textEdit=ui.textEdit.toPlainText()
    
    curs.execute("INSERT INTO Kitap \
                         (KitapNo,KitapAd,YazarAd,SayfaSayisi,Tur,Yayinevi,KitapBaslangic,KitapBitis,Derecelendir,Dusunceler) \
                          VALUES(?,?,?,?,?,?,?,?,?,?)",\
                              (_leKitapNo,_leKitapAd,_leYazarAd,_leSayfaSayisi,_leTur,_leYayinevi,\
                               _cwBaslangic,_calendarWidget_2,_KitabiDerecelendir,_textEdit,))

    conn.commit()  
    LİSTELE()
    
#%%

#-----LİSTELE-----#
def LİSTELE():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(('No','Kitap No','Kitap Ad','Yazar Ad','Sayfa Sayısı','Tür', \
                                                  'Yayınevi','Kitap Başlangıç','Kitap Bitiş', 'Derecelendir', \
                                                  'Düşünceler',))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
    curs.execute("SELECT* FROM Kitap")
    for satirIndeks,satirVeri in enumerate(curs):
        for sutunIndeks,sutunVeri in enumerate(satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    ui.leKitapNo.clear()
    ui.leKitapAd.clear()
    ui.leYazarAd.clear()
    ui.leSayfaSayisi.clear()
    ui.leTur.clear()
    ui.leYayinevi.clear()
    ui.KitabiDerecelendir.setValue(0)
    ui.textEdit.clear()
    
    
LİSTELE()

#%%

#-----SİLME-----#
def KAYDI_SİL():
    yanıt=QMessageBox.question(pencere,"KAYDI SİL","Silmek istediğine emin misin?",\
                               QMessageBox.Yes|QMessageBox.No)
    if yanıt==QMessageBox.Yes:
        secili=ui.tableWidget.selectedItems() #seçili olan satırı secili değişkenine attık.
        silinecek=secili[1].text() #secili değişkenini parcaladık/string formatında olması gerektiği için text fonk. ile çevirdik.
        try: 
            curs.execute("DELETE FROM Kitap WHERE KitapNo='%s'" %(silinecek))
            conn.commit()  #veritabanında silecek bunu
            LİSTELE() #silindiğini tabletwidget de görmek için listele fonk. yazdık
            ui.statusbar.showMessage("Kayıt silme başarılı",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi.",10000)
        
#%%
        
#-----ARAMA-----#  
def KAYIT_ARA():
    aranan1=ui.leKitapAd.text()
    aranan2=ui.leYazarAd.text()
    aranan3=ui.leTur.text()
    aranan4=ui.leKitapNo.text()
    aranan5=ui.KitabiDerecelendir.text()
    curs.execute("SELECT * FROM Kitap WHERE KitapAd=? OR YazarAd=? OR Tur=? OR KitapNo=? OR Derecelendir=?", \
                 (aranan1,aranan2,aranan3,aranan4,aranan5))
    conn.commit() 
    ui.tableWidget.clear()
    for satirIndeks,satirVeri in enumerate(curs): #tablewidget içerisine dönen sorgu yerleşir
        for sutunIndeks,sutunVeri in enumerate(satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            
#%%
           
#-----DOLDUR-----# 
def DOLDUR():
    secili=ui.tableWidget.selectedItems()  #selectedItems() yöntemi yalnızca seçili hücreleri içeren bir liste döndürür. 
    ui.leKitapNo.setText(secili[1].text()) #secili[1] deki yazıyı yazıyor/ui.leKitapNo QLineEdit nesnesinin içine yerleştirir. 
    ui.leKitapAd.setText(secili[2].text())
    ui.leYazarAd.setText(secili[3].text())
    ui.leSayfaSayisi.setText(secili[4].text())
    ui.leTur.setText(secili[5].text())
    ui.leYayinevi.setText(secili[6].text())
    
    yil=int(secili[7].text()[0:4]) 
    ay=int(secili[7].text()[5:7])
    gun=int(secili[7].text()[8:10])
    ui.cwBaslangic.setSelectedDate(QtCore.QDate(yil,ay,gun)) 
    
    yil=int(secili[8].text()[0:4]) 
    ay=int(secili[8].text()[5:7])
    gun=int(secili[8].text()[8:10])
    ui.calendarWidget_2.setSelectedDate(QtCore.QDate(yil,ay,gun)) 
    
    ui.KitabiDerecelendir.setValue(int(secili[9].text()))
    ui.textEdit.setText(secili[10].text())
    
#%%

 #-----GÜNCELLE-----#     
def KAYIT_GÜNCELLE():
    yanıt=QMessageBox.question(pencere,"KAYIT GÜNCELLE","Kaydı güncellemek istediğine emin misin?",\
                               QMessageBox.Yes|QMessageBox.No)
    if yanıt==QMessageBox.Yes:
        try: #hata olması muhtemel kodlar/try bir kod bloğunu hatalara karşı denetler.
            secili=ui.tableWidget.selectedItems()
            _Id=int(secili[0].text())
            _leKitapNo=ui.leKitapNo.text() #içeriğini bu şekilde aldık
            _leKitapAd=ui.leKitapAd.text()
            _leYazarAd=ui.leYazarAd.text()
            _leSayfaSayisi=ui.leSayfaSayisi.text()
            _leTur=ui.leTur.text()
            _leYayinevi=ui.leYayinevi.text()
            _cwBaslangic=ui.cwBaslangic.selectedDate().toString(QtCore.Qt.ISODate)
            _calendarWidget_2=ui.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)
            _KitabiDerecelendir=ui.KitabiDerecelendir.value()
            _textEdit=ui.textEdit.toPlainText()
            
            curs.execute("UPDATE Kitap SET KitapNo=?,KitapAd=?,YazarAd=?, \
                         SayfaSayisi=?,Tur=?,Yayinevi=?,KitapBaslangic=?,\
                         KitapBitis=?,Derecelendir=?,Dusunceler=? WHERE Id=?", 
                             (_leKitapNo,_leKitapAd,_leYazarAd,_leSayfaSayisi, \
                              _leTur,_leYayinevi,_cwBaslangic,_calendarWidget_2,\
                                 _KitabiDerecelendir,_textEdit,_Id))
            conn.commit() #bağlantıyı kurduk 
            
            LİSTELE() #güncellenmiş bilgileri listele fonk.çalıştırarak tablewidgetimizde görecez.
        
        except Exception as Hata: #exception hata mesajını yazdırıyor.
            ui.statusbar.showMessage("Şöyle bir hata meeydana geldi"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncelleme iptal edildi",10000)
        
        
            
#%% 
  
#-----SİNYAL-SLOT-----#
ui.btnKayitEkle.clicked.connect(KAYIT_EKLE)   
ui.btnTumKayit.clicked.connect(LİSTELE)  
ui.btnKaydiSil.clicked.connect(KAYDI_SİL)
ui.btnKayitAra.clicked.connect(KAYIT_ARA)
ui.tableWidget.itemSelectionChanged.connect(DOLDUR)    
ui.btnKayitGuncelle.clicked.connect(KAYIT_GÜNCELLE)

#%%

sys.exit(uygulama.exec_()) 