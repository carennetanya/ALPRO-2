def hitung_total_belanja():
    total_belanja = 0
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    daftar_belanja = []
    
    for i in range(1, jumlah_barang + 1):
        nama_barang = input(f"Masukkan nama barang ke-{i}: ")
        harga = float(input(f"Masukkan harga barang ke-{i}: "))
        kuantitas = int(input(f"Masukkan jumlah barang ke-{i}: "))
        total_harga = harga * kuantitas
        total_belanja += total_harga
        daftar_belanja.append((nama_barang, harga, kuantitas, total_harga))
    
    print("\nTOTAL BELANJA")
    print("=" * 50)
    print(f"{'Nama Barang':<15} | {'Harga':<10} | {'Jumlah':<6} | {'Total':<10}")
    print("-" * 50)
    for item in daftar_belanja:
        print(f"{item[0]:<15} | Rp {item[1]:<8.2f} | {item[2]:<6} | Rp {item[3]:<8.2f}")
    print("=" * 50)
    print(f"Total belanja Anda adalah: Rp {total_belanja:.2f}")

hitung_total_belanja()
