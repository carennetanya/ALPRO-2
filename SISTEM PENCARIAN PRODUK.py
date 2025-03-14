import time
import random

def pairwise_comparison(products):
    start_time = time.time()
    min_product = products[0]
    comparisons = 0  # Menghitung jumlah perbandingan

    for product in products:
        comparisons += 1
        if product['price'] < min_product['price']:
            min_product = product

    execution_time = time.time() - start_time
    return min_product, execution_time, comparisons

def sorting_search(products):
    start_time = time.time()
    products.sort(key=lambda x: x['price'])  # Sorting by price (O(n log n))
    min_product = products[0]
    execution_time = time.time() - start_time
    return min_product, execution_time, len(products)  # Jumlah operasi sorting kira-kira O(n)

def main():
    user_id = input("Masukkan ID pengguna: ")
    print(f"Selamat datang, Pengguna {user_id}!")

    # Generate dummy products
    products = [{'name': f'Produk {i}', 'price': random.randint(1000, 5000), 'rating': round(random.uniform(1.0, 5.0), 1), 'popularity': random.randint(100, 1000)} for i in range(50000)]
    
    while True:
        print("\nPilih metode pencarian:")
        print("1. Solusi Buruk (O(n²)) - Pairwise Comparison")
        print("2. Solusi Baik (O(n log n)) - Sorting & Search")
        choice = input("Masukkan pilihan (1/2): ")
        
        if choice == '1':
            method = "O(n²) - Pairwise Comparison"
            min_product, exec_time, operations = pairwise_comparison(products)
        elif choice == '2':
            method = "O(n log n) - Sorting & Search"
            min_product, exec_time, operations = sorting_search(products)
        else:
            print("Pilihan tidak valid! Coba lagi.")
            continue
        
        print(f"\nMetode: {method}")
        print("Produk dengan harga termurah:")
        print(f"- Nama Produk  : {min_product['name']}")
        print(f"- Harga        : {min_product['price']}")
        print(f"- Rating       : {min_product['rating']}")
        print(f"- Trending     : {min_product['popularity']}")
        print(f"- Waktu Eksekusi: {exec_time:.6f} detik")
        print(f"- Jumlah operasi: {operations} kali perbandingan")

        lanjut = input("\nIngin mencari lagi? (y/n): ")
        if lanjut.lower() != 'y':
            print("Terima kasih telah menggunakan sistem rekomendasi produk!")
            break

if __name__ == "__main__":
    main()
