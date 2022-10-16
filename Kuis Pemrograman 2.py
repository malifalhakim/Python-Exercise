nama_user  = input("Masukkan Nama Anda : ")
harga_buku_awal = float(input("Masukkan harga buku awal : "))
harga_buku_setelah_diskon = float(input("Masukkan harga buku setelah diskon : "))

besar_diskon_rupiah = harga_buku_awal - harga_buku_setelah_diskon
besar_diskon_persen = (besar_diskon_rupiah / harga_buku_awal )*100

print("Halo",nama_user,"! Anda mendapatkan diskon sebesar",besar_diskon_persen,"persen")