# Destinasi wisata dan biaya masing-masing
destinasi = [
    {"nama": "Pantai Kuta", "biaya": 10000},
    {"nama": "Nusa Penida", "biaya": 2500000},
    {"nama": "Ubud", "biaya": 100000},
    {"nama": "Denpasar", "biaya": 100000}
]

# Biaya transportasi
biaya_transport = 3000000  # Sidoarjo - Bali PP
biaya_nyebrang = 500000  # Nyebrang Banyuwangi - Bali PP
total_transport = biaya_transport + biaya_nyebrang

# Biaya hotel (14 malam, 300rb per malam), termasuk 4 malam di Nusa Penida
biaya_hotel_bali = 10 * 300000  # 10 malam di Bali
biaya_hotel_nusa_penida = 4 * 300000  # 4 malam di Nusa Penida
total_hotel = biaya_hotel_bali + biaya_hotel_nusa_penida

# Biaya makan per hari
biaya_makan_pagi = 25000  # Sarapan khas Bali
biaya_makan_siang = 40000  # Makan siang khas Bali (babi guling, ayam betutu, dll)
biaya_makan_malam = 30000  # Makan malam khas Bali
biaya_jajan = 20000  # Jajan khas Bali

# Total biaya makan selama 14 hari
total_makan = 14 * (biaya_makan_pagi + biaya_makan_siang + biaya_makan_malam + biaya_jajan)

# Biaya oleh-oleh
biaya_oleh_oleh = 690000  

# Anggaran total
total_anggaran = 10000000

# Pilih destinasi yang dikunjungi
def pilih_destinasi():
    print("\nPilih destinasi yang ingin dikunjungi:")
    print("Ketik angka destinasi dan tekan ENTER (pisahkan dengan koma, contoh: 1,3,4)")
    for i, d in enumerate(destinasi, start=1):
        print(f"{i}. {d['nama']} - Rp {d['biaya']:,}")

    pilihan = input("Masukkan pilihan: ")
    pilihan = pilihan.split(",")  # Pisahkan input berdasarkan koma
    total_destinasi = 0
    destinasi_terpilih = []

    for p in pilihan:
        try:
            index = int(p.strip()) - 1
            if 0 <= index < len(destinasi):
                destinasi_terpilih.append(destinasi[index]["nama"])
                total_destinasi += destinasi[index]["biaya"]
        except ValueError:
            print(f"Input '{p}' tidak valid!")

    return destinasi_terpilih, total_destinasi

# Menampilkan menu pilihan
def tampilkan_menu(destinasi_terpilih, total_destinasi):
    while True:
        print("\nPilih kategori biaya:")
        print("1. Biaya Transportasi")
        print("2. Biaya Hotel")
        print("3. Biaya Makan")
        print("4. Biaya Oleh-oleh")
        print("5. Biaya Destinasi yang Dikunjungi")
        print("6. Total Biaya dan Sisa Anggaran")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan (1-7): ")

        total_biaya = total_transport + total_hotel + total_makan + biaya_oleh_oleh + total_destinasi
        sisa_anggaran = total_anggaran - total_biaya  # Seharusnya jadi Rp 0 jika pilih semua

        if pilihan == "1":
            print(f"\nTotal Biaya Transportasi: Rp {total_transport:,}")
        elif pilihan == "2":
            print(f"\nTotal Biaya Hotel: Rp {total_hotel:,}")
        elif pilihan == "3":
            print(f"\nTotal Biaya Makan: Rp {total_makan:,}")
        elif pilihan == "4":
            print(f"\nTotal Biaya Oleh-oleh: Rp {biaya_oleh_oleh:,}")
        elif pilihan == "5":
            print("\nDestinasi yang Dikunjungi:")
            for d in destinasi_terpilih:
                print(f"- {d}")
            print(f"Total Biaya Destinasi: Rp {total_destinasi:,}")
        elif pilihan == "6":
            print(f"\nTotal Biaya Keseluruhan: Rp {total_biaya:,}")
            print(f"Sisa Anggaran: Rp {sisa_anggaran:,}")  # Seharusnya 0 jika pilih semua destinasi
        elif pilihan == "7":
            print("\nTerima kasih! Selamat liburan ke Bali! 🎉")
            break
        else:
            print("\nPilihan tidak valid, silakan pilih lagi.")

# Jalankan program
destinasi_terpilih, total_destinasi = pilih_destinasi()
tampilkan_menu(destinasi_terpilih, total_destinasi)
