'''
Created on 2 lis 2015

@author: Krzysztof 
'''

import codecs
import os.path

from pyspatialite import dbapi2
#import time

from PyQt4.QtGui import QApplication


 


class SilpDb(object):
    '''
    classdocs
    '''
    
#     global db_path
#     global db
#     global cur
    
    def __init__(self, path):
        '''
        Constructor
        '''
        self.db_path = os.path.normpath(path)
        
    def __otworz(self):
        '''
        Otworz baze
        '''
        self.db = dbapi2.connect(self.db_path)
        self.cur = self.db.cursor()
        
    def __zamknij(self):
        
#         self.cur.close()
        self.db.commit()
        self.db.close()
        
    def __wczytaj_plik(self, sciezka_pliku):
        plik = codecs.open(sciezka_pliku, 'r', encoding='cp1250')
        zawartosc = plik.readlines()
        plik.close()
        return zawartosc
    
    def __importuj_wiersz(self, tabela, wiersz):
        
        wiersz = wiersz.replace('"', '""')
        wiersz = wiersz.replace("'", "''")
        
        wiersz = wiersz.split('|')[:-1]
        sql = "INSERT INTO %s VALUES (" % tabela
        for field in wiersz:
            sql += ("'" + field + "', ")
        sql = sql.rstrip(', ') + ')'
        
        result = self.cur.execute(sql)
                
    def __importuj_plik(self, sciezka_pliku, aplikacja):
        #aplikacja.dlg.processEvents()
        QApplication.processEvents()
        tabela = os.path.basename(sciezka_pliku).split('.')[-2]
        zawartosc = self.__wczytaj_plik(sciezka_pliku)
        
        self.__otworz()
        
        self.cur.execute('DELETE FROM %s' % tabela)
        rows_count = len(zawartosc)
        row_now = 1;
        aplikacja.dlg.progressBar_wiersze.setMaximum(rows_count)
        aplikacja.dlg.label_wiersze.setText("Wiersze tabeli %s" % tabela)
        
        for linia in zawartosc:
            #aplikacja.dlg.progressBar_wiersze.setValue(row_now)
            self.__importuj_wiersz(tabela, linia)
            row_now += 1
            #print aplikacja.dlg.progressBar_wiersze.value()
            
        self.db.commit()
        self.cur.execute("VACUUM")
        self.__zamknij() 
    
    def importuj_katalog(self, sciezka_latalogu, aplikacja):
        sciezka_latalogu = os.path.normpath(sciezka_latalogu)
        lista_plikow = os.listdir(sciezka_latalogu)
        files_count = len(lista_plikow)
        file_now = 1;
        
        aplikacja.dlg.progressBar_pliki.setMaximum(files_count)
        
        for plik in lista_plikow:
            if plik.endswith('.txt'):
                self.__importuj_plik(os.path.join(sciezka_latalogu, plik), aplikacja)
                aplikacja.dlg.progressBar_pliki.setValue(file_now)
                file_now += 1
                #print aplikacja.dlg.progressBar_pliki.value()
        
        aplikacja.dlg.progressBar_pliki.setValue(files_count)
  
        
