import random

dbPasien = [
    {
        'identitas': {'nama': 'budi', 'NIK': '38518100', 'alamat': 'Jalan Merdeka No. 123, Jakarta'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'asam lambung'},
        'wali': {'nama': 'ratih', 'NIK': '38512200', 'hubungan': 'kakak','alamat': 'Jalan Merdeka No. 123, Jakarta'},
        'idPasien': 'id88', 'room': 'C2'
    },
    {
        'identitas': {'nama': 'cahyo', 'NIK': '38518144', 'alamat': 'Jalan Pahlawan No. 456, Bandung'},
        'medRcrd': {'golDrh': 'B', 'diagnosa': 'demam berdarah'},
        'wali': {'nama': 'sigit', 'NIK': '38541100', 'hubungan': 'kakak', 'alamat': 'Jalan Pahlawan No. 456, Bandung'},
        'idPasien': 'id24', 'room': 'C2'
    },
    {
        'identitas': {'nama': 'dewi', 'NIK': '38518101', 'alamat': 'Jalan Proklamasi No. 789, Surakarta'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'flu'},
        'wali': {'nama': 'sari', 'NIK': '38512201', 'hubungan': 'saudara','alamat': 'Jalan Proklamasi No. 789, Surakarta'},
        'idPasien': 'id33', 'room': 'C2'
    },
    {
        'identitas': {'nama': 'eko', 'NIK': '38518102', 'alamat': 'Jalan Perjuangan No. 101, Semarang'},
        'medRcrd': {'golDrh': 'AB', 'diagnosa': 'alergi'},
        'wali': {'nama': 'wulan', 'NIK': '38512202', 'hubungan': 'kakak', 'alamat': 'Jalan Perjuangan No. 101, Semarang'},
        'idPasien': 'id12', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'fajar', 'NIK': '38518103', 'alamat': 'Jalan Patriot No. 555, Surabaya'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'migrain'},
        'wali': {'nama': 'bayu', 'NIK': '38512203', 'hubungan': 'saudara', 'alamat': 'Jalan Patriot No. 555, Surabaya'},
        'idPasien': 'id76', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'galuh', 'NIK': '38518104', 'alamat': 'Jalan Mawar No. 222, Jakarta'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'asma'},
        'wali': {'nama': 'rini', 'NIK': '38512204', 'hubungan': 'orang tua', 'alamat': 'Jalan Mawar No. 222, Jakarta'},
        'idPasien': 'id91', 'room': 'C1'
    },
    {
        'identitas': {'nama': 'hendra', 'NIK': '38518105', 'alamat': 'Jalan Kenari No. 333, Bandung'},
        'medRcrd': {'golDrh': 'B', 'diagnosa': 'hipertensi'},
        'wali': {'nama': 'yudi', 'NIK': '38512205', 'hubungan': 'saudara', 'alamat': 'Jalan Kenari No. 333, Bandung'},
        'idPasien': 'id55', 'room': 'vip'
    },
    {
        'identitas': {'nama': 'indra', 'NIK': '38518106', 'alamat': 'Jalan Cendana No. 444, Surakarta'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'diabetes'},
        'wali': {'nama': 'putri', 'NIK': '38512206', 'hubungan': 'kakak', 'alamat': 'Jalan Cendana No. 444, Surakarta'},
        'idPasien': 'id19', 'room': 'icu'
    },
    {
        'identitas': {'nama': 'joko', 'NIK': '38518107', 'alamat': 'Jalan Anggrek No. 777, Semarang'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'batu ginjal'},
        'wali': {'nama': 'rudi', 'NIK': '38512207', 'hubungan': 'saudara', 'alamat': 'Jalan Anggrek No. 777, Semarang'},
        'idPasien': 'id02', 'room': 'icu'
    },
    {
        'identitas': {'nama': 'krisna', 'NIK': '38518108', 'alamat': 'Jalan Melati No. 888, Surabaya'},
        'medRcrd': {'golDrh': 'AB', 'diagnosa': 'gagal jantung'},
        'wali': {'nama': 'sinta', 'NIK': '38512208', 'hubungan': 'kakak', 'alamat': 'Jalan Melati No. 888, Surabaya'},
        'idPasien': 'id44', 'room': 'icu'
    },
    {
        'identitas': {'nama': 'lina', 'NIK': '38518109', 'alamat': 'Jalan Teratai No. 999, Jakarta'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'radang tenggorokan'},
        'wali': {'nama': 'bambang', 'NIK': '38512209', 'hubungan': 'orang tua', 'alamat': 'Jalan Teratai No. 999, Jakarta'},
        'idPasien': 'id66', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'maya', 'NIK': '38518110', 'alamat': 'Jalan Dahlia No. 111, Bandung'},
        'medRcrd': {'golDrh': 'B', 'diagnosa': 'pneumonia'},
        'wali': {'nama': 'siska', 'NIK': '38512210', 'hubungan': 'saudara', 'alamat': 'Jalan Dahlia No. 111, Bandung'},
        'idPasien': 'id87', 'room': 'C1'
    },
    {
        'identitas': {'nama': 'nanda', 'NIK': '38518111', 'alamat': 'Jalan Cempaka No. 222, Surakarta'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'malaria'},
        'wali': {'nama': 'vino', 'NIK': '38512211', 'hubungan': 'kakak','alamat': 'Jalan Cempaka No. 222, Surakarta'},
        'idPasien': 'id09', 'room': 'C1'
    },
    {
        'identitas': {'nama': 'opik', 'NIK': '38518112', 'alamat': 'Jalan Mawar No. 333, Semarang'},
        'medRcrd': {'golDrh': 'AB', 'diagnosa': 'anemia'},
        'wali': {'nama': 'dina', 'NIK': '38512212', 'hubungan': 'saudara', 'alamat': 'Jalan Mawar No. 333, Semarang'},
        'idPasien': 'id31', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'pratiwi', 'NIK': '38518113', 'alamat': 'Jalan Kenanga No. 444, Surabaya'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'tuberkulosis'},
        'wali': {'nama': 'adit', 'NIK': '38512213', 'hubungan': 'saudara', 'alamat': 'Jalan Kenanga No. 444, Surabaya'},
        'idPasien': 'id53', 'room': 'vip'
    },
    {
        'identitas': {'nama': 'qonita', 'NIK': '38518114', 'alamat': 'Jalan Seroja No. 555, Jakarta'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'rabies'},
        'wali': {'nama': 'vina', 'NIK': '38512214', 'hubungan': 'kakak', 'alamat': 'Jalan Seroja No. 555, Jakarta'},
        'idPasien': 'id77', 'room': 'C1'
    },
    {
        'identitas': {'nama': 'raka', 'NIK': '38518115', 'alamat': 'Jalan Alamanda No. 666, Bandung'},
        'medRcrd': {'golDrh': 'B', 'diagnosa': 'kanker'},
        'wali': {'nama': 'rama', 'NIK': '38512215', 'hubungan': 'saudara', 'alamat': 'Jalan Alamanda No. 666, Bandung'},
        'idPasien': 'id13', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'sari', 'NIK': '38518116', 'alamat': 'Jalan Melati No. 777, Surakarta'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'ginjal kronis'},
        'wali': {'nama': 'dian', 'NIK': '38512216', 'hubungan': 'kakak', 'alamat': 'Jalan Melati No. 777, Surakarta'},
        'idPasien': 'id05', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'tika', 'NIK': '38518117', 'alamat': 'Jalan Mawar No. 888, Semarang'},
        'medRcrd': {'golDrh': 'AB', 'diagnosa': 'hipotiroid'},
        'wali': {'nama': 'rio', 'NIK': '38512217', 'hubungan': 'kakak', 'alamat': 'Jalan Mawar No. 888, Semarang'},
        'idPasien': 'id70', 'room': 'vip'
    },
    {
        'identitas': {'nama': 'udin', 'NIK': '38518118', 'alamat': 'Jalan Kenari No. 999, Surabaya'},
        'medRcrd': {'golDrh': 'A', 'diagnosa': 'obesitas'},
        'wali': {'nama': 'linda', 'NIK': '38512218', 'hubungan': 'saudara', 'alamat': 'Jalan Kenari No. 999, Surabaya'},
        'idPasien': 'id29', 'room': 'C3'
    },
    {
        'identitas': {'nama': 'vivi', 'NIK': '38518119', 'alamat': 'Jalan Puspa No. 1234, Jakarta'},
        'medRcrd': {'golDrh': 'O', 'diagnosa': 'asma'},
        'wali': {'nama': 'eko', 'NIK': '38512219', 'hubungan': 'saudara', 'alamat': 'Jalan Puspa No. 1234, Jakarta'},
        'idPasien': 'id37', 'room': 'C3'
    }
]
roomCapacity = {'vip': 4,
                    'icu': 6,
                    'C1' : 8,
                    'C2' : 12,
                    'C3' : 24}

db=[]

def pilihMenu():
    print ('Menu data rumah sakit ')
    print('[1] Tampil Data Pasien')
    print('[2] Tambah Data Pasien')
    print('[3] Ubah kamar Pasien')
    print('[4] Pemulangan pasien')
    print('[5] Program Selesai\n')  
    menunum = int(input('Masukkan nomor opsi yang dipilih : ')) 
    return menunum

def menu(dbPasien,roomCapacity):
    while True:
        menuSelection = pilihMenu()
        if menuSelection ==1:
            print('[1] Tampil Data Pasien')
            tabelPasien(dbPasien)
        elif menuSelection ==2:
            print('[2] Tambah Data Pasien')
            dbPasien.append(tambahPasien())

        elif menuSelection ==3:
            print('[3] Ubah kamar Pasien')
            tabelPasien(dbPasien)
            pilihPasien= input('Masukan id Pasien')
            for i in dbPasien:
                if i['idPasien'] == pilihPasien:
                    i['room'] = ubahRoom(dbPasien,roomCapacity)
                False

        elif menuSelection ==4:
            print('[4] Pemulangan pasien')
            tabelPasien(dbPasien)
            print ('\n')
            pulangpasien()
        elif menuSelection ==5:
            print('program selesai')
            break
            
def pulangpasien():
    print('opsi pasien')
    print('1. pasien sembuh/Pulang')
    print('2. pasien meninggal')
    pilihopsi= int(input('Masukan opsi Pasien'))
    pilihPasien= input('Masukan id Pasien')
    while True:
        if pilihopsi == 1:
            for i in dbPasien:
                if i['idPasien'] == pilihPasien:
                    namaPasien= i['identitas']['nama']
                    wali = i['wali']['nama']
                    pindahDb = {'identitas' : i['identitas'],'medRcrd' : i['medRcrd']}
                    print(f'Persiapan pemulangan pasien {namaPasien}, menghubungi wali {wali} h-1 sebelum pulang ')
                    db.append(pindahDb)
                    dbPasien.remove(i)
                break
            else:
                print (f"Pasien dengan ID {pilihPasien} tidak ditemukan")
            break
        elif pilihopsi == 2:
            for i in dbPasien:
                if i['idPasien'] == pilihPasien:
                    namaPasien= i['identitas']['nama']
                    wali = i['wali']['nama']
                    print(f'Persiapan pemulangan jenazah {namaPasien}, menghubungi wali {wali} untuk penjemputan jenazah')
                break
            else:
                print (f"Pasien dengan ID {pilihPasien} tidak ditemukan")
            break
                        
def tabelPasien(data):
    print ('Tabel Seluruh Pasien')
    print("{:<15} {:<15} {:<40} {:<25} {:<10}".format("Nama", "ID Pasien", "Alamat", "Diagnosa", "Kamar"))
    
    for pasien in data:
        print("{:<15} {:<15} {:<40} {:<25} {:<10}".format(
            pasien['identitas']['nama'], pasien['idPasien'], pasien['identitas']['alamat'], pasien['medRcrd']['diagnosa'],pasien['room']
        ))
    
    
def tambahPasien():
    formKosong = {'identitas': {'nama': None, 'NIK': None, 'alamat': None},
        'medRcrd': {'golDrh': None, 'diagnosa': None},
        'wali': {'nama': None, 'NIK': None, 'hubungan': None, 'alamat': None},
        'idPasien': None, 'room': None}
    
    dataPasien = formKosong.copy()  # Copy formKosong untuk mengisi data pasien baru

    # Mengisi data pasien dari input pengguna
    dataPasien['identitas']['nama'] = input("Masukkan nama pasien: ")
    dataPasien['identitas']['NIK'] = input("Masukkan NIK pasien: ")
    dataPasien['identitas']['alamat'] = input("Masukkan alamat pasien: ")
    dataPasien['medRcrd']['golDrh'] = input("Masukkan golongan darah pasien: ")
    dataPasien['medRcrd']['diagnosa'] = input("Masukkan diagnosa pasien: ")
    dataPasien['wali']['nama'] = input("Masukkan nama wali pasien: ")
    dataPasien['wali']['NIK'] = input("Masukkan NIK wali pasien: ")
    dataPasien['wali']['hubungan'] = input("Masukkan hubungan dengan pasien: ")
    dataPasien['wali']['alamat'] = input("Masukkan alamat wali pasien: ")
    dataPasien['idPasien'] = regIdPasien(dbPasien)
    dataPasien['room'] = assignRoom(dbPasien,roomCapacity)
    
    return dataPasien
    
def regIdPasien(dbPasien):
    while True:
        idPasien = 'ID' + str(random.randint(1, 99))
        idExists = any(item['idPasien'] == idPasien for item in dbPasien)
        if not idExists:
            return idPasien

def assignRoom(data_pasien, roomCapacity):
    rc=sisaKamar(data_pasien, roomCapacity)
    print ('Menu pilihan Kamar')
    print ('1. VIP')
    print ('2. Kelas 1')
    print ('3. Kelas 2')
    print ('4. Kelas 3')
    
    while True:
        nomenu = int(input('Pilih Kamar Yang diinginkan'))
        if nomenu == 1:
            if rc['vip'] > 0:
                pilihanKamar = 'vip'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
                
        elif nomenu == 2:
            if rc['C1'] > 0:
                pilihanKamar = 'C1'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 3:
            if rc['C2'] > 0:
                pilihanKamar = 'C2'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 4:
            if rc['C3'] > 0:
                pilihanKamar = 'C3'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        else:
            print ('Menu salah')

def ubahRoom(data_pasien, roomCapacity):
    rc=sisaKamar(data_pasien, roomCapacity)
    print ('Menu pilihan Kamar')
    print ('1. VIP')
    print ('2. Kelas 1')
    print ('3. Kelas 2')
    print ('4. Kelas 3')
    print ('5. ICU')
    
    while True:
        nomenu = int(input('Pilih Kamar Yang diinginkan'))
        if nomenu == 1:
            if rc['vip'] > 0:
                pilihanKamar = 'vip'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 2:
            if rc['C1'] > 0:
                pilihanKamar = 'C1'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 3:
            if rc['C2'] > 0:
                pilihanKamar = 'C2'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 4:
            if rc['C3'] > 0:
                pilihanKamar = 'C3'
                return pilihanKamar
            else:
                print ('Kamar Penuh')
        elif nomenu == 5:
            if rc['icu'] > 0:
                pilihanKamar = 'icu'
                return pilihanKamar
            else:
                print ('ICU Penuh, akan dirujuk ke rumah sakit lainnya')
        else:
            print ('Menu salah')   
    
def sisaKamar(data_pasien, roomCapacity):
    kamarTersisa = dict(roomCapacity) 
    for pasien in data_pasien:
        room_type = pasien['room']
        if room_type in kamarTersisa:
            kamarTersisa[room_type] -= 1
    return kamarTersisa

def caripasienbyid(patient_id):
    for patient in dbPasien:
        if patient['idPasien'] == patient_id:
            return patient
    return None

menu(dbPasien,roomCapacity)
    
