class Mahasiswa: #Mendefinisikan kelas Mahasiswa.
    def __init__(self, nama, nim, jurusan): #Mendefinisikan metode konstruktor __init__ untuk kelas Mahasiswa. Metode ini akan dieksekusi ketika objek Mahasiswa dibuat dan menerima parameter nama, nim, dan jurusan.
        self.nama = nama #Membuat atribut nama pada objek Mahasiswa dan menginisialisasinya dengan nilai yang diterima sebagai parameter.
        self.nim = nim #Membuat atribut nim pada objek Mahasiswa dan menginisialisasinya dengan nilai yang diterima sebagai parameter.
        self.jurusan = jurusan # Membuat atribut jurusan pada objek Mahasiswa dan menginisialisasinya dengan nilai yang diterima sebagai parameter.
    
    def tampilkan_info(self): #Mendefinisikan metode tampilkan_info untuk kelas Mahasiswa.
        print("Nama         : ", self.nama) #Mencetak informasi nama Mahasiswa.
        print("NIM          : ", self.nim) #Mencetak informasi NIM Mahasiswa.
        print("Jurusan      : ", self.jurusan.NamaJurusan) # Mencetak informasi Jurusan Mahasiswa dengan mengakses atribut NamaJurusan dari objek Jurusan yang ditetapkan pada atribut jurusan objek Mahasiswa.
        print() #Mencetak baris kosong untuk memberikan jarak antara setiap info Mahasiswa saat mencetak.

class Jurusan: #Mendefinisikan kelas Jurusan.
    def __init__(self, nama_jurusan): #Mendefinisikan metode konstruktor __init__ untuk kelas Jurusan. Metode ini akan dieksekusi ketika objek Jurusan dibuat. Menerima parameter nama_jurusan.
        self.NamaJurusan = nama_jurusan #Membuat atribut NamaJurusan pada objek Jurusan dan menginisialisasinya dengan nilai yang diterima sebagai parameter.
        self.DaftarMahasiswa = [] #Membuat atribut DaftarMahasiswa pada objek Jurusan yang berupa sebuah list kosong untuk menyimpan objek Mahasiswa yang terdaftar di jurusan tersebut.
    
    def tambah_mahasiswa(self, mahasiswa): #Mendefinisikan metode tambah_mahasiswa
        self.DaftarMahasiswa.append(mahasiswa) #Menambahkan objek Mahasiswa ke dalam daftar DaftarMahasiswa pada objek Jurusan.
    
    def tampilkan_daftar_mahasiswa(self): #Mendefinisikan metode tampilkan_daftar_mahasiswa
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan) #Mencetak judul "Daftar Mahasiswa di Jurusan" diikuti dengan nama jurusan yang disimpan dalam atribut NamaJurusan.
        for mahasiswa in self.DaftarMahasiswa: #Melakukan iterasi untuk setiap objek Mahasiswa dalam daftar DaftarMahasiswa pada objek Jurusan.
            if mahasiswa.jurusan == self: #Memeriksa apakah atribut jurusan dari objek Mahasiswa sama dengan objek Jurusan saat ini.
                mahasiswa.tampilkan_info() #Memanggil metode tampilkan_info() dari objek Mahasiswa untuk mencetak informasinya.

class Universitas: #Mendefinisikan kelas Universitas.
    def __init__(self, nama_universitas): #Mendefinisikan metode konstruktor __init__ untuk kelas Universitas. Metode ini akan dieksekusi ketika objek Universitas dibuat. Menerima parameter nama_universitas.
        self.NamaUniversitas = nama_universitas #Membuat atribut NamaUniversitas pada objek Universitas dan menginisialisasinya dengan nilai yang diterima sebagai parameter.
        self.DaftarJurusan = [] #Membuat atribut DaftarJurusan pada objek Universitas yang berupa sebuah list kosong untuk menyimpan objek Jurusan yang terkait dengan universitas tersebut.
    
    def tambah_jurusan(self, jurusan): #Mendefinisikan metode tambah_jurusan 
        self.DaftarJurusan.append(jurusan) #Menambahkan objek Jurusan ke dalam daftar DaftarJurusan pada objek Universitas.
    
    def tampilkan_daftar_jurusan(self): #Mendefinisikan metode tampilkan_daftar_jurusan
        print("Daftar Jurusan di Universitas", self.NamaUniversitas) #Mencetak judul "Daftar Jurusan di Universitas" diikuti dengan nama universitas yang disimpan dalam atribut NamaUniversitas.
        for i, jurusan in enumerate(self.DaftarJurusan, start=1): #Melakukan iterasi untuk setiap objek Jurusan dalam daftar DaftarJurusan pada objek Universitas. enumerate digunakan untuk mendapatkan indeks dan objek jurusan secara bersamaan, dengan start=1 untuk memulai indeks dari 1.
            print(f"{i}. {jurusan.NamaJurusan}") #Mencetak nomor urut dan nama jurusan dari objek Jurusan yang sedang diiterasi.

# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat beberapa objek Jurusan dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

jurusan_si = Jurusan("Sistem Informasi")
universitas_xyz.tambah_jurusan(jurusan_si)

jurusan_ts = Jurusan("Teknik Sipil")
universitas_xyz.tambah_jurusan(jurusan_ts)

# Membuat beberapa objek Mahasiswa dan memasukkannya ke dalam Jurusan di Universitas XYZ
daftar_mahasiswa = Mahasiswa("RIOLAN PRATAMA", "G1A022047", jurusan_ti)
jurusan_ti.tambah_mahasiswa(daftar_mahasiswa)

daftar_mahasiswa = Mahasiswa("RAZORS", "123456789", jurusan_si)
jurusan_si.tambah_mahasiswa(daftar_mahasiswa)

daftar_mahasiswa = Mahasiswa("THIMO", "987654321", jurusan_ts)
jurusan_ts.tambah_mahasiswa(daftar_mahasiswa)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
jurusan_si.tampilkan_daftar_mahasiswa()
jurusan_ts.tampilkan_daftar_mahasiswa()
