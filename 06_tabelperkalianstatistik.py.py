
print("TABEL PERKALIAN 1-5\n")

jumlah = 0
banyak_data = 0

for i in range(1, 6):
    for j in range(1, 6):

        hasil = i * j

        print(f"{hasil:3}", end=" ")

        jumlah += hasil
        banyak_data += 1

    print()

rata_rata = jumlah / banyak_data

print("\n=== STATISTIK ===")
print("Jumlah Data :", jumlah)
print("Banyak Data :", banyak_data)
print("Rata-rata   :", rata_rata)