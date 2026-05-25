# ===================================
# SISTEM PENJUALAN MOBIL KOLEKTOR BEKAS
# ===================================
# Developed by. Muhammad Rafi Andrianto
# JCDS - 33


class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    #reset back to normal terminal text
    RESET = '\033[0m'

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


def main_menu():
    """
    printing layout for the main menu
    """
    print("\n")
    print(f"{Color.CYAN}{Color.BOLD}" + "="*50)
    print(" "*13 + "WJKSN SHOWROOM DATABASE")
    print("="*50 + f"{Color.RESET}")
    print(f"{Color.BLUE}1.{Color.RESET} Lihat Showroom Inventory")
    print(f"{Color.BLUE}2.{Color.RESET} Tambah Koleksi Baru")
    print(f"{Color.BLUE}3.{Color.RESET} Perbarui Data Mobil")
    print(f"{Color.BLUE}4.{Color.RESET} Hapus Unit dari Sistem")
    print(f"{Color.BLUE}5.{Color.RESET} Exit Program")
    print(f"{Color.CYAN}{Color.BOLD}" + "="*50 + f"{Color.RESET}")


def show_table(data):
    """
    helper function for printing the results
    """
    if not data:
        print(f"\n {Color.YELLOW} Tidak ada data mobil yang cocok dengan kriteria {Color.RESET}")
        return

    print("\n")
    print(f"{Color.CYAN}" + "-" * 115 + f"{Color.RESET}")
    print(f"{'ID':<10} {Color.CYAN}|{Color.RESET} {'Kategori':<10} {Color.CYAN}|{Color.RESET} {'Nama Mobil':<30} {Color.CYAN}|{Color.RESET} {'Tahun':<6} {Color.CYAN}|{Color.RESET} {'Mesin':<15} {Color.CYAN}|{Color.RESET} {'Harga (IDR)':<19} {Color.CYAN}|{Color.RESET} {'Status':<10}")
    print(f"{Color.CYAN}" + "-" * 115 + f"{Color.RESET}")
    
    for key, value in data.items():

        harga_format = f"Rp {value['harga']:,.2f}"
        
        print(f"{key:<10} {Color.CYAN}|{Color.RESET} {value['kategori']:<10} {Color.CYAN}|{Color.RESET} {value['nama_mobil']:<30} {Color.CYAN}|{Color.RESET} {value['tahun']:<6} {Color.CYAN}|{Color.RESET} {value['mesin']:<15} {Color.CYAN}|{Color.RESET} {harga_format:<18} {Color.CYAN}|{Color.RESET} {value['status_unit']:<10}")
    
    print(f"{Color.CYAN}" + "-" * 115 + f"{Color.RESET}")


def read():
    """
    to show the data stored in the system
    """
    while True:
        print("\n")
        print(f"{Color.CYAN}{Color.BOLD}"+ "-"*35)
        print("    SUB-MENU VIEW SHOWROOM STOCK    ")
        print("-"*35 + f"{Color.RESET}")
        print(f"{Color.BLUE}1.{Color.RESET} Tampilkan Semua Koleksi")
        print(f"{Color.BLUE}2.{Color.RESET} Cari Mobil Berdasarkan ID")
        print(f"{Color.BLUE}3.{Color.RESET} Filter Berdasarkan Kategori (JDM/USDM/EDM)")
        print(f"{Color.BLUE}4.{Color.RESET} Filter Berdasarkan Keyword Mobil / Mesin")
        print(f"{Color.BLUE}5.{Color.RESET} Kembali ke Menu Menu")
        print(f"{Color.CYAN}{Color.BOLD}" + "-"*35 + f"{Color.RESET}")
        
        sub_pilihan = input("Pilih menu (1-5): ")
        
        if sub_pilihan == "1":
            show_table(data_mobil)
            
        elif sub_pilihan == "2":
            target_id = input("\nMasukkan ID Mobil yang dicari (Contoh: JDM-001): ").upper()

            if target_id in data_mobil:
                #creating temp dictionary for showing 1 car only
                single_car = {}
                single_car[target_id] = data_mobil[target_id]
                show_table(single_car)

            else:
                print(f"\n{Color.RED}[ERROR] Mobil dengan ID '{target_id}' tidak ditemukan {Color.RESET}")
                
        elif sub_pilihan == "3":
            target_kat = input("Masukkan Kategori Filter (JDM / USDM / EDM): ").upper()

            if target_kat in ["JDM", "USDM", "EDM"]:

                #temp dictionary for saving chosen category
                filtered_cars = {}
                for car_id, info in data_mobil.items():
                    if info['kategori'] == target_kat:
                        filtered_cars[car_id] = info
                show_table(filtered_cars)

            else:
                print(f"\n{Color.RED}[ERROR] Kategori tidak valid! Pilih antara JDM, USDM, atau EDM {Color.RESET}")
                
        elif sub_pilihan == "4":
            keyword = input("\nMasukkan kata kunci pencarian (Nama Mobil / Seri Mesin): ").strip().lower()
            
            #validate
            if not keyword:
                print(f"{Color.RED}\n[ERROR] Keyword tidak boleh kosong!{Color.RESET}")
                continue
                
            filtered_cars = {}
            
            for key, value in data_mobil.items():

                nama_scan = value['nama_mobil'].lower()
                mesin_scan = value['mesin'].lower()

                
                #check
                if keyword in nama_scan or keyword in mesin_scan:
                    filtered_cars[key] = value
            
            show_table(filtered_cars)
                
        elif sub_pilihan == "5":
            print("\nKembali ke Main Menu...")
            break
        else:
            print(f"{Color.RED}\n[ERROR] Pilihan tidak valid! {Color.RESET}")


def generate_id(kategori):
    """
    Automatically generates car_id
    ex if JDM-001 and JDM-002 exist, will return 'JDM-003'
    """
    #determine prefix
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
                num_part = int(i.split("-")[1]) #split the number
                if num_part > max_num:
                    max_num = num_part
            except (IndexError, ValueError):
                continue #skip format anex just in case
                
    # +1 for the next id
    next_num = max_num + 1
    
    #return dengan 3-digit zero padding
    return f"{prefix}-{next_num:03d}"


def create():
    """
    to create new data for the system
    """
    while True:
        print("\n" + f"{Color.CYAN}" + "-"*35 + f"{Color.RESET}")
        print("     SUB-MENU TAMBAH UNIT BARU")
        print(f"{Color.CYAN}" + "-"*35 + f"{Color.RESET}")
        print(f"{Color.BLUE}1.{Color.RESET} Daftarkan Mobil Baru")
        print(f"{Color.BLUE}2.{Color.RESET} Kembali ke Main Menu")
        print(f"{Color.CYAN}" + "-"*35 + f"{Color.RESET}")
        
        sub_pilihan = input("Pilih menu (1-2): ").strip()
        
        if sub_pilihan == "1":
            #validate 
            while True:
                kategori = input("Masukkan kategori (JDM / USDM / EDM): ").strip().upper()

                if kategori == "0": #cancel
                    break

                if kategori in ["JDM", "USDM", "EDM"]:
                    break

                print(f"{Color.YELLOW}\n[WARNING] Kategori tidak valid! Wajib memilih JDM, USDM, atau EDM {Color.RESET}\n")
            
            if kategori == "0":
                print(f"\n{Color.YELLOW}[Batal] Proses dibatalkan. Kembali ke menu...{Color.RESET}")
                continue

            #generate new id
            new_id = generate_id(kategori)
            print(f"ID Mobil Otomatis Dibuat: {new_id}")
            
            
            nama_mobil = input("Masukkan Nama/Model Mobil: ").strip()
            mesin = input("Masukkan Tipe/Seri Mesin: ").strip()
            
            #validate year
            while True:
                try:
                    tahun = int(input("Masukkan Tahun Pembuatan: ").strip())
                    if 1900 <= tahun <= 2026:
                        break
                    print(f"{Color.YELLOW}[WARNING] Tahun harus masuk akal (1900 - 2026)! {Color.RESET}")
                except ValueError:
                    print(f"{Color.YELLOW}[WARNING] Input tidak valid! Tahun wajib berupa angka bulat {Color.RESET}")
            
            #validate price
            while True:
                try:
                    harga = float(input("Masukkan Harga Unit (IDR): ").strip())
                    if harga > 0:
                        break
                    print(f"{Color.YELLOW}[WARNING] Harga harus lebih besar dari Rp 0{Color.RESET}")
                except ValueError:
                    print(f"{Color.YELLOW}[WARNING] Input tidak valid! Harga wajib berupa angka nominal{Color.RESET}")
            
            #summary input
            print(f"{Color.CYAN}\n--- RINGKASAN DATA UNIT BARU ---{Color.RESET}")
            print(f"ID Mobil    : {new_id} (Generated)")
            print(f"Kategori    : {kategori}")
            print(f"Nama Mobil  : {nama_mobil}")
            print(f"Tahun       : {tahun}")
            print(f"Mesin       : {mesin}")
            print(f"Harga       : Rp {harga:,.2f}")
            print(f"{Color.CYAN}" + "-" * 32 + f"{Color.RESET}")
            
            konfirmasi = input(f"Yakin mau disimpan? ({Color.GREEN}Y{Color.RESET}/{Color.RED}N{Color.RESET}): ").upper()
            
            if konfirmasi == "Y":
                data_mobil[new_id] = {
                    "kategori": kategori,
                    "nama_mobil": nama_mobil,
                    "tahun": tahun,
                    "mesin": mesin,
                    "harga": harga,
                    "status_unit": "Available"
                }
                print(f"\n{Color.GREEN}[SUCCESS] Unit '{nama_mobil}' dengan ID '{new_id}' berhasil didaftarkan!{Color.RESET}")
            else:
                print(f"\n{Color.RED}[Batal] Pendaftaran unit baru dibatalkan oleh operator {Color.RESET}")
            
        elif sub_pilihan == "2":
            print("\nKembali ke Main Menu...")
            break
        else:
            print(f"\n{Color.YELLOW}[WARNING] Pilihan tidak valid! Masukkan angka 1 atau 2{Color.RESET}")


def update():
    """
    to update existinf data in the system
    """
    while True:
        print("\n")
        print(f"{Color.CYAN}" + "-"*35)
        print("     SUB-MENU PERBARUI DATA     ")
        print("-"*35 + f"{Color.RESET}")
        print(f"{Color.BLUE}1.{Color.RESET} Ubah Atribut Data Mobil")
        print(f"{Color.BLUE}2.{Color.RESET} Kembali ke Main Menu")
        print(f"{Color.CYAN}" + "-"*35 + f"{Color.RESET}")
        
        sub_pilihan = input("Pilih menu (1-2): ").strip()
        
        if sub_pilihan == "1":

            target_id = input("Masukkan ID Mobil yang ingin diupdate: ").strip().upper()
            
            if target_id == "0": #cancel
                print(f"\n{Color.RED}[Batal] Proses dibatalkan. Kembali ke menu... {Color.RESET} ")
                continue

            #check if the car exist
            if target_id not in data_mobil:
                print(f"\n{Color.RED} [ERROR] Mobil dengan ID '{target_id}' tidak terdaftar di sistem! {Color.RESET}")
                continue
            
            
            car = data_mobil[target_id]
            
            print(f"\n{Color.CYAN}--- CURRENT DATA UNTUK ID {target_id} ---{Color.RESET}")
            print(f"1. Nama Mobil : {car['nama_mobil']}")
            print(f"2. Tahun      : {car['tahun']}")
            print(f"3. Mesin      : {car['mesin']}")
            print(f"4. Harga      : Rp {car['harga']:,.2f}")
            print(f"5. Status Unit: {car['status_unit']}")
            print(f"{Color.CYAN}" + "-" * 35 + f"{Color.RESET}")
            
            pilihan_field = input("Pilih nomor atribut yang ingin diubah (1-5): ").strip()
            
            #to track the field name and the new value input
            field_key = ""
            new_value = None
            
            if pilihan_field == "1":
                field_key = "nama_mobil"
                new_value = input("Masukkan nama/model mobil baru: ").strip()
                
            elif pilihan_field == "2":
                field_key = "tahun"
                while True:
                    try:
                        new_value = int(input("Masukkan tahun pembuatan baru: ").strip())
                        if 1900 <= new_value <= 2026:
                            break
                        print(f"{Color.YELLOW}[WARNING] Tahun harus 1900 - 2026 {Color.RESET}")
                    except ValueError:
                        print(f"{Color.YELLOW}[WARNING] Tahun wajib berupa angka bulat {Color.RESET}")
                        
            elif pilihan_field == "3":
                field_key = "mesin"
                new_value = input("Masukkan tipe/seri mesin baru: ").strip()
                
            elif pilihan_field == "4":
                field_key = "harga"
                while True:
                    try:
                        new_value = float(input("Masukkan harga unit baru (IDR): ").strip())
                        if new_value > 0:
                            break
                        print(f"{Color.YELLOW}[WARNING] Harga harus lebih besar dari Rp 0!{Color.RESET}")
                    except ValueError:
                        print(f"{Color.YELLOW}[WARNING] Input tidak valid! Harga wajib berupa angka nominal{Color.RESET}")
                        
            elif pilihan_field == "5":
                field_key = "status_unit"
                while True:
                    new_value = input("Masukkan status baru (Available / Reserved / Sold): ").strip().capitalize()
                    if new_value in ["Available", "Reserved", "Sold"]:
                        break
                    print(f"{Color.YELLOW}[WARNING] Status tidak valid! pilih Available, Reserved, atau Sold{Color.RESET}")
            else:
                print(f"\n{Color.YELLOW}[WARNING] Pilihan atribut tidak tersedia!{Color.RESET}")
                continue
                
            #validate
            print(f"\nPerubahan Atribut '{field_key}' akan diganti menjadi '{new_value}'")
            konfirmasi = input(f"Apakah anda yakin ingin menyimpan perubahan ini? ({Color.GREEN}Y{Color.RESET}/{Color.RED}N{Color.RESET}): ").strip().upper()
            
            if konfirmasi == "Y":
                #overwrite chosen key
                data_mobil[target_id][field_key] = new_value
                print(f"\n{Color.GREEN}[SUCCESS] Data mobil ID '{target_id}' berhasil diperbarui! {Color.RESET}")
            else:
                print(f"\n{Color.RED}[Batal] Update data dibatalkan {Color.RESET}")
                
        elif sub_pilihan == "2":
            print("\nKembali ke Main Menu...")
            break
        else:
            print(f"\n{Color.YELLOW}[WARNING] Pilihan tidak valid! Masukkan angka 1 atau 2{Color.RESET}")


def delete():
    """
    to delete existing data in the system
    """
    while True:
        print("\n" + f"{Color.CYAN}" + "-"*35)
        print("     SUB-MENU HAPUS DATA UNIT")
        print("-"*35 + f"{Color.RESET}")
        print(f"{Color.BLUE}1.{Color.RESET} Hapus Unit Mobil Permanent")
        print(f"{Color.BLUE}2.{Color.RESET} Kembali ke Main Menu")
        print(f"{Color.CYAN}" + "-"*35 + f"{Color.RESET}")
        
        sub_pilihan = input("Pilih menu (1-2): ").strip()
        
        if sub_pilihan == "1":

            target_id = input("Masukkan ID Mobil yang ingin dihapus: ").strip().upper()
            
            # validate if id exists
            if target_id not in data_mobil:
                print(f"\n{Color.RED}[ERROR] Mobil dengan ID '{target_id}' tidak ditemukan di sistem!{Color.RESET}")
                continue
            
            car = data_mobil[target_id]
            print(f"\n{Color.YELLOW}[WARNING] Anda akan menghapus data: {car['nama_mobil']} ({target_id}){Color.RESET}")
            
            #double check
            konfirmasi = input(f"Apakah anda yakin? ({Color.GREEN}Y{Color.RESET}/{Color.RED}N{Color.RESET}): ").strip().upper()
            
            if konfirmasi == "Y":
                #remove key value pair
                removed_car = data_mobil.pop(target_id)
                print(f"\n{Color.GREEN}[SUCCESS] Unit '{removed_car['nama_mobil']} ({target_id})' telah dihapus dari sistem!{Color.RESET}")
            else:
                print(f"\n{Color.RED}[Batal] Penghapusan unit dibatalkan {Color.RESET}")
                
        elif sub_pilihan == "2":
            print("\nKembali ke Main Menu...")
            break
        else:
            print(f"\n{Color.YELLOW}[WARNING] Pilihan tidak valid! Masukkan angka 1 atau 2{Color.RESET}")

while True:
    main_menu()
    
    usr_inp = input("Masukkan menu yang ingin dijalankan (1-5): ")
    
    if usr_inp == "1":
        read()

    elif usr_inp == "2":
        create()

    elif usr_inp == "3":
        update()

    elif usr_inp == "4":
        delete()

    elif usr_inp == "5":
        print(f"\n{Color.BOLD}Exiting Program...\nGoodbye!\n{Color.RESET}")
        break
    else:
        print(f"\n{Color.YELLOW}[WARNING] Pilihan tidak valid! Masukkan angka 1-5{Color.RESET}")