import psycopg2 as psy
import random

listword = [] #list untuk kata penyemangat
listsong = [] #list untuk referensi lagu

class Database:

    def __init__(self):
        #sambungkan koneksi ke database server
        self.con = psy.connect(database="wordiary",
                       user="postgres",
                       password="13012006",
                       host="localhost", port="5432")
        self.cursor = self.con.cursor()
        #print("Database opened successfully")
        self.cursor.execute('select * from Word')
        rows = self.cursor.fetchall() #ambil semua record dari tabel Word
        for row in rows:
            listword.append(list(row)) #masukkan record ke dalam list kata penyemangat
        self.cursor.execute('select * from Lagu')
        songs = self.cursor.fetchall() #ambil semua record dari tabel Lagu
        for song in songs:
            listsong.append(list(song)) #masukkan record ke dalam list referensi lagu

    #fungsi untuk return kata penyemangat pilihan sedih secara acak
    def output_sad(self):
        sadword = []
        for word in listword:
            if word[0] == 'sedih':
                sadword.append(word[1])
        return random.choice(sadword)

    #fungsi untuk return kata penyemangat pilihan marah secara acak
    def output_angry(self):
        angryword = []
        for word in listword:
            if word[0] == 'marah':
                angryword.append(word[1])
        return random.choice(angryword)

    #fungsi untuk return kata penyemangat pilihan sakit secara acak
    def output_sick(self):
        sickword = []
        for word in listword:
            if word[0] == 'sakit':
                sickword.append(word[1])
        return random.choice(sickword)

    #fungsi untuk return kata penyemangat pilihan patah hati secara acak
    def output_broke(self):
        brokenword = []
        for word in listword:
            if word[0] == 'galau':
                brokenword.append(word[1])
        return random.choice(brokenword)

    #fungsi untuk return lagu pilihan sedih secara acak
    def sadsong(self):
        listsadsong = []
        for song in listsong:
            if song[0] == 'sedih':
                listsadsong.append(song[1:])
        return random.choice(listsadsong)

    #fungsi untuk return lagu pilihan marah secara acak
    def angrysong(self):
        listangrysong = []
        for song in listsong:
            if song[0] == 'marah':
                listangrysong.append(song[1:])
        return random.choice(listangrysong)

    #fungsi untuk return lagu pilihan sakit secara acak
    def sicksong(self):
        listsicksong = []
        for song in listsong:
            if song[0] == 'sakit':
                listsicksong.append(song[1:])
        return random.choice(listsicksong)

    # fungsi untuk return lagu pilihan patah hati secara acak
    def brokensong(self):
        listbrokensong = []
        for song in listsong:
            if song[0] == 'patah hati':
                listbrokensong.append(song[1:])
        return random.choice(listbrokensong)

    def insertdiary(self, text, date, title):
        #insert data ke tabel diary
        self.cursor.execute(f'insert into diary values({date!r},{text!r},{title!r})')
        print("Data inserted succesfully")
        self.con.commit() #simpan perubahan

    def deletediary(self, date):
        recorddelete = date
        #hapus data dari tabel diary berdasarkan tanggal
        self.cursor.execute(f'delete from diary where tanggal={recorddelete!r}')
        self.con.commit() #simpan perubahan

    def searchdiary(self, date):
        loop = 0
        self.cursor.execute("select * from diary")
        diary = self.cursor.fetchall() #ambil semua record dari tabel diary
        listdiary = []
        for i in diary:
            listdiary.append(list(i)) #masukkan semua record ke dalam list diary
        self.con.commit() #simpan perubahan
        for text in listdiary:
            if loop < len(listdiary):
                #cek apakah tanggal yang diinput ada di list diary
                if text[0] == date:
                    c = text[1].count('\\n')
                    k = text[1].replace('\\n', '\n', c)
                    return k #return text diary
                else:
                    loop += 1
                    continue
            else:
                return 'Data tidak ditemukan'

    def searchtitle(self, date):
        loop = 0
        self.cursor.execute("select * from diary")
        diary = self.cursor.fetchall() #ambil semua record dari tabel diary
        listdiary = []
        for i in diary:
            listdiary.append(list(i))
        self.con.commit() #simpan perubahan
        for text in listdiary:
            if loop < len(listdiary):
                #cek apakah tanggal yang diinput ada di list diary
                if text[0] == date:
                    return text[2] #return title diary
                else:
                    loop += 1
                    continue

    def getdiarydate(self):
        self.cursor.execute("select * from diary")
        date = self.cursor.fetchall() #amibl semua record dari tabel diary
        datelist = [] #list tanggal
        for i in date:
            datelist.append(i[0]) #masukkan record tanggal ke list tanggal
        self.con.commit() #simpan perubahan
        print(datelist)
        return datelist

    def addpin(self, pin, pertanyaan, jawaban):
        insertpin = "insert into pin values(%s, %s, %s)"
        recordpin = (pin, pertanyaan, jawaban)
        #masukkan data ke tabel pin
        self.cursor.execute(insertpin, recordpin)
        print("PIN added succesfully")
        self.con.commit() #simpan perubahan

    def verifypin(self):
        self.cursor.execute("select * from pin")
        userpin = self.cursor.fetchall() #ambil semua record dari tabel pin
        listpin = []
        for i in userpin:
            listpin.append(list(i)) #masukkan record ke dalam listpin
        self.con.commit() #simpan perubahan
        if listpin == []:
            #jika listpin masih kosong maka return nilai none
            return None
        else:
            #jika listpin sudah terisi return nilai pin tsb
            return listpin[0][1]

    def deletepin(self):
        self.cursor.execute("delete from pin") #hapus pin
        self.con.commit() #simpan perubahan

    def close(self):
        self.con.close() #tutup koneksi database


#semangat gais
