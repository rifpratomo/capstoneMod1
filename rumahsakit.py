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

def menu():
    print('[1] Tampil Data Pasien')
    print('[2] Tambah Data Pasien')
    print('[3] Edit Data Pasien')
    print('[4] Pendataan Pulang Data Pasien')
    
    kode = input('Masukkan Nomor Menu : ')
    if kode =='1':
        print('Menu Daftar Informasi\n')
        # daftarPasien()
        patient_table = tabelPasien(dbPasien)
        cetakTabel(patient_table) 
    elif kode =='2':
        print('Menu Menambah Pasien\n')
        addPasien(dbPasien)
    elif kode =='3':
        
        while True:
            print('Ubah Data Pasien')
            print('[1] Ubah Kamar Pasien')
            print('[2] Pemulangan Pasien')
            kode = input('Masukkan Nomor Menu : ')

            if kode == '1':

                print('Anda memilih menu Ubah Kamar Pasien')
                break 
            elif kode == '2':

                print('Anda memilih menu Pemulangan Pasien')
                idpasien = input("Masukkan ID Pasien yang akan dihapus: ")
                pasienPulang(idpasien)
                break  
            else:
                print('Pilihan tidak valid. Silakan pilih 1 atau 2.')
        
    elif kode =='4':
        print('Program Selesai')
        exit()
    else :
        print('Menu Salah')
    
    while (True):
        menu()
        
def tabelPasien(data):
    table = []
    headers = ["Index", "ID Pasien", "Nama", "Alamat", "Diagnosa", "Kamar"]
    
    for idx, patient in enumerate(data):
        identitas = patient['identitas']
        med_record = patient['medRcrd']
        table.append([
            str(idx + 1),
            patient['idPasien'],
            identitas['nama'],
            identitas['alamat'],
            med_record['diagnosa'],
            patient['room']
        ])
    table.insert(0, headers)
    return table

def cetakTabel(table):
    col_width = [max(len(str(word)) for word in col) for col in zip(*table)]
    for row in table:
        print("  ".join(str(word).ljust(width) for word, width in zip(row, col_width)))
        
# tabel kamar

def roomHitung(data):
    lroom= []
    for i in data:
        lroom.append({i['idPasien']:i['room']})
    roomCounts =    {'C1': 0, 
                   'C2': 0, 
                   'C3': 0,
                   'vip':0,
                   'icu':0
                   }  
    for roomEntry in lroom:
        for roomValue in roomEntry.values():
            if roomValue in roomCounts:
                roomCounts[roomValue] += 1
    return roomCounts


def addIdentitas():
    print('Masukkan Identitas Pasien')
    noIdentitas = input('NIK : ')
    namaPasien = input('nama lengkap (sesuai KTP) : ')
    alamatRumah = input('Alamat rumah : ')
    return {'nama':namaPasien,'NIK' : noIdentitas,'alamat' : alamatRumah}

def addWali():
    print('Masukkan Identitas Wali')
    noIdentitas = input('NIK : ')
    namaWali = input('nama lengkap (sesuai KTP) : ')
    alamatRumah = input('Alamat rumah : ')
    hubungan = input('Hubungan : ')
    return {'nama': namaWali,'NIK' : noIdentitas,'hubPasien': hubungan,'alamat' : alamatRumah}

def rekamMedis():
    golDarah = input('golongan Darah : ')
    diagnosa = input('diagnosa : ')
    return {'golDrh' : golDarah,'diagnosa':diagnosa}

def regIdPasien(dbPasien):
    while True:
        idPasien = 'ID' + str(random.randint(1, 99))
        id_exists = any(item['idPasien'] == idPasien for item in dbPasien)
        if not id_exists:
            return idPasien
        
def addPasien(dbPasien):
    pasienbaru= {}
    pasienbaru={'identitas':addIdentitas(),'medRcrd' : rekamMedis(),'Wali':addWali(),'idPasien':regIdPasien(dbPasien),'room':assignRoomPasien(dbPasien)}
    dbPasien.append(pasienbaru)

def assignRoomPasien(dbPasien):
    roomCapacity=   {'C1':8,
                 'C2':12,
                 'C3':24,
                 'vip':4,
                 'icu':4
    }
    roomCounts = roomHitung(dbPasien)
   
    pilihanKamar = int(input('Pilih nomor ruangan: '))
    print('Pilih Ruang Inap')
    print(f'1. Kelas VIP')
    print('2. Kelas 1')
    print('3. Kelas 2')
    print('4. Kelas 3')
    room = ''
    if pilihanKamar == 1:
        room = 'vip'
    elif pilihanKamar == 2:
        room = 'C1'
    elif pilihanKamar == 3:
        room = 'C2'
    elif pilihanKamar == 4:
        room = 'C3'
    else:
        print('Pilihan ruangan tidak valid.')
        assignRoomPasien(dbPasien)
    
    if room in roomCounts and room in roomCapacity:
        if roomCounts[room] < roomCapacity[room]:
            roomCounts[room] += 1
            print(f'Pasien telah ditugaskan ke Ruang {room}')
        else:
            print(f'Ruang {room} sudah penuh. Pilih ruangan lain.')
    else:
        print(f'Ruang {room} tidak valid.')
    return room

def pasienPulang(patient_id):
    for index, patient in enumerate(dbPasien):
        if patient['idPasien'] == patient_id:
            del dbPasien[index]
            print(f"pasien dengan ID {patient_id} telah pulang.")
            return True
    print(f"Tidak ditemukan pasien dengan ID {patient_id}")
    return False    
    
menu()
