from typing import List, Dict, Optional

class Buku:
    def __init__(self, judul: str, penulis: str, tahun: int):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"

# List untuk menyimpan objek Buku
daftar_buku: List[Buku] = []

def tambah_buku(judul: str, penulis: str, tahun: int):
    buku_baru = Buku(judul, penulis, tahun)
    daftar_buku.append(buku_baru)

def cari_buku(judul: str) -> Optional[Buku]:
    for buku in daftar_buku:
        if buku.judul == judul:
            return buku
    return None

def tampilkan_semua_buku():
    if not daftar_buku:
        print("Belum ada buku yang terdaftar.")
    else:
        for buku in daftar_buku:
            print(buku)

