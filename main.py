# ===================================
# SISTEM PENJUALAN MOBIL KOLEKTOR BEKAS
# ===================================
# Developed by. Muhammad Rafi Andrianto
# JCDS - 33


# /************************************/

# /===== Data Model =====/
# The primary data collection containing our current inventory
data_mobil = {
    "JDM-001": {
        "kategori": "JDM",
        "nama_mobil": "Nissan Silvia S15 Spec-R",
        "tahun": 1999,
        "mesin": "SR20DET",
        "harga": 1250000000.00,
        "status_unit": "Available"
    },
    "JDM-002": {
        "kategori": "JDM",
        "nama_mobil": "Toyota Supra JZA80 RZ",
        "tahun": 1997,
        "mesin": "2JZ-GTE",
        "harga": 2100000000.00,
        "status_unit": "Reserved"
    },
    "USD-001": {
        "kategori": "USDM",
        "nama_mobil": "Ford Mustang Boss 302",
        "tahun": 1970,
        "mesin": "V8 5.0L",
        "harga": 2800000000.00,
        "status_unit": "Available"
    },
    "USD-002": {
        "kategori": "USDM",
        "nama_mobil": "Dodge Viper GTS",
        "tahun": 1996,
        "mesin": "8.0L V10",
        "harga": 3200000000.00,
        "status_unit": "Sold"
    },
    "EDM-001": {
        "kategori": "EDM",
        "nama_mobil": "Porsche 911 Carrera RS 2.7",
        "tahun": 1973,
        "mesin": "2.7L Flat-6",
        "harga": 4500000000.00,
        "status_unit": "Available"
    },
    "EDM-002": {
        "kategori": "EDM",
        "nama_mobil": "BMW M3 E30 Sport Evolution",
        "tahun": 1990,
        "mesin": "S14 Inline-4",
        "harga": 2300000000.00,
        "status_unit": "Available"
    }
}


# /===== Feature Program =====/
def main_menu():
    """
    print layout main menu sistemnya
    """
    print("\n" + "="*50)
    print(" "*13 + "WJKSN SHOWROOM DATABASE")
    print("="*50)
    print("1. Lihat Showroom Inventory")
    print("2. Tambah Koleksi Baru")
    print("3. Perbarui Data Mobil")
    print("4. Hapus Unit dari Sistem")
    print("5. Exit Program")
    print("="*50)


def show_table(data):
    """
    helper function untuk print hasil sub menu
    """
    if not data:
        print("\n Tidak ada data mobil yang cocok dengan kriteria.")
        return

    print("\n")
    print("-" * 115)
    print(f"{'ID':<10} | {'Kategori':<10} | {'Nama Mobil':<30} | {'Tahun':<6} | {'Mesin':<15} | {'Harga (IDR)':<18} | {'Status':<10}")
    print("-" * 115)
    
    for car_id, info in data.items():

        harga_format = f"Rp {info['harga']:,.2f}"
        
        print(f"{car_id:<10} | {info['kategori']:<10} | {info['nama_mobil']:<30} | {info['tahun']:<6} | {info['mesin']:<15} | {harga_format:<18} | {info['status_unit']:<10}")
    
    print("-" * 115)


def sub_menu_read():
    """
    untuk handle pilihan submenu read
    """
    while True:
        print("\n" + "-"*35)
        print("    SUB-MENU VIEW SHOWROOM STOCK    ")
        print("-"*35)
        print("1. Tampilkan Semua Koleksi")
        print("2. Cari Mobil Berdasarkan ID")
        print("3. Filter Berdasarkan Kategori (JDM/USDM/EDM)")
        print("4. Kembali ke Menu Menu")
        print("-"*35)
        
        sub_pilihan = input("Pilih menu (1-4): ")
        
        if sub_pilihan == "1":
            show_table(data_mobil)
            
        elif sub_pilihan == "2":
            target_id = input("\nMasukkan ID Mobil yang dicari (Contoh: JDM-001): ").upper()

            if target_id in data_mobil:
                #buat temp dictionary baru untuk menampilkan 1 mobil aja
                single_car = {}
                single_car[target_id] = data_mobil[target_id]
                show_table(single_car)

            else:
                print(f"\n[ERROR] Mobil dengan ID '{target_id}' tidak ditemukan di sistem!")
                
        elif sub_pilihan == "3":
            target_kat = input("Masukkan Kategori Filter (JDM / USDM / EDM): ").upper()

            if target_kat in ["JDM", "USDM", "EDM"]:

                #dictionary baru untuk memfilter per kategori yang terpilih
                filtered_cars = {}
                for car_id, info in data_mobil.items():
                    if info['kategori'] == target_kat:
                        filtered_cars[car_id] = info
                show_table(filtered_cars)

            else:
                print("\n[ERROR] Kategori tidak valid! Pilih antara JDM, USDM, atau EDM.")
                
        elif sub_pilihan == "4":
            print("\nKembali ke Main Menu...")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1 sampai 4.")


def generate_id(kategori):
    """
    Automatically generates car_id
    misal kalau JDM-001 and JDM-002 exist, akan return 'JDM-003'
    """
    #determine prefixnya
    if kategori == "JDM":
        prefix = "JDM"
    elif kategori == "USDM":
        prefix = "USD"
    else:
        prefix = "EDM"
        
    max_num = 0
    
    for i in data_mobil.keys():
        if i.startswith(prefix):
            try:
                num_part = int(i.split("-")[1]) #split nomornya
                if num_part > max_num:
                    max_num = num_part
            except (IndexError, ValueError):
                continue #skip format anex just in case
                
    # +1 untuk next id
    next_num = max_num + 1
    
    #return dengan 3-digit zero padding
    return f"{prefix}-{next_num:03d}"


def sub_menu_create():
    """
    untuk handle sub menu create
    """
    while True:
        print("\n" + "-"*35)
        print("     SUB-MENU TAMBAH UNIT BARU     ")
        print("-"*35)
        print("1. Daftarkan Mobil Baru")
        print("2. Kembali ke Main Menu")
        print("-"*35)
        
        sub_pilihan = input("Pilih menu (1-2): ").strip()
        
        if sub_pilihan == "1":
            print("\n>>> INPUT DATA ACQUISITION BARU <<<")
            
            #validate kategori sesuai dengan yang tersedia
            while True:
                kategori = input("Masukkan Kategori (JDM / USDM / EDM): ").strip().upper()
                if kategori in ["JDM", "USDM", "EDM"]:
                    break
                print("[ERROR] Kategori tidak valid! Wajib memilih JDM, USDM, atau EDM.")
            
            #generate new id
            new_id = generate_id(kategori)
            print(f"ID Mobil Otomatis Dibuat: {new_id}")
            
            
            nama_mobil = input("Masukkan Nama/Model Mobil: ").strip()
            mesin = input("Masukkan Tipe/Seri Mesin: ").strip()
            
            #validate tahun
            while True:
                try:
                    tahun = int(input("Masukkan Tahun Perakitan: ").strip())
                    if 1900 <= tahun <= 2026:
                        break
                    print("[ERROR] Tahun harus masuk akal (1900 - 2026)!")
                except ValueError:
                    print("[ERROR] Input tidak valid! Tahun wajib berupa angka bulat.")
            
            #validate harga
            while True:
                try:
                    harga = float(input("Masukkan Harga Unit (IDR): ").strip())
                    if harga > 0:
                        break
                    print("[ERROR] Harga harus lebih besar dari Rp 0!")
                except ValueError:
                    print("[ERROR] Input tidak valid! Harga wajib berupa angka nominal.")
            
            #summary input
            print("\n--- RINGKASAN DATA UNIT BARU ---")
            print(f"ID Mobil    : {new_id} (Generated)")
            print(f"Kategori    : {kategori}")
            print(f"Nama Mobil  : {nama_mobil}")
            print(f"Tahun       : {tahun}")
            print(f"Mesin       : {mesin}")
            print(f"Harga       : Rp {harga:,.2f}")
            print("-" * 32)
            
            konfirmasi = input("Apakah data di atas sudah benar & ingin disimpan? (Y/N): ").upper()
            
            if konfirmasi == "Y":
                data_mobil[new_id] = {
                    "kategori": kategori,
                    "nama_mobil": nama_mobil,
                    "tahun": tahun,
                    "mesin": mesin,
                    "harga": harga,
                    "status_unit": "Available"
                }
                print(f"\n[SUCCESS] Unit '{nama_mobil}' dengan ID '{new_id}' berhasil didaftarkan!")
            else:
                print("\n[Batal] Pendaftaran unit baru dibatalkan oleh operator.")
            
        elif sub_pilihan == "2":
            print("\nKembali ke Main Menu...")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1 atau 2.")



while True:
    main_menu()
    
    usr_inp = input("Masukkan menu yang ingin dijalankan (1-5): ")
    
    if usr_inp == "1":
        sub_menu_read()

    elif usr_inp == "2":
        sub_menu_create()

    elif usr_inp == "3":
        pass

    elif usr_inp == "4":
        pass

    elif usr_inp == "5":
        print("\nTerima kasih telah menggunakan sistem showroom kami. Goodbye!")
        break
    else:
        print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1 sampai 5.")