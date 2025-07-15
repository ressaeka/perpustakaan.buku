from perpustakaan.buku import Buku, tambah_buku, cari_buku, tampilkan_semua_buku

tambah_buku("kain Pel`", "markicong", 2005)
tambah_buku("majaturu", "nande oreo", 2010)
tambah_buku("slebew", "sibogel", 2010)

print("Buku sudah ditambahkan!")  # Tambahkan baris ini

tampilkan_semua_buku()

buku_dicari = cari_buku("Laskar Pelangi")
if buku_dicari:
    print(f"Buku ditemukan:\n{buku_dicari}")
else:
    print("Buku tidak ditemukan.")
    