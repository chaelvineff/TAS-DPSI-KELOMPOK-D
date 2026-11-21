def menu_tampil_buku(data):
    print("=== DAFTAR BUKU ===")
    if len(data["buku"]) == 0:
        print("Belum ada buku.")
        return
    print(f"{'Kode':<8}{'Judul':<25}{'Kategori':<12}{'Stok':>5}")
    for item in data["buku"]:
        print(f"{item['kode']:<8}{item['judul']:<25}{item['kategori']:<12}{item['stok']:>5}")


def menu_tambah_buku(data):
    print("=== TAMBAH BUKU ===")
    kode = input("Kode buku: ")
    judul = input("Judul: ")
    kategori = input("Kategori: ")
    stok = input_angka("Stok: ")
    kelola_buku.tambah_buku(data["buku"], kode, judul, kategori, stok)
    print("Buku berhasil ditambahkan!")


def menu_ubah_buku(data):
    print("=== UBAH BUKU ===")
    kode = input("Kode buku yang diubah: ")
    item = kelola_buku.cari_buku(data["buku"], kode)
    if item is None:
        raise ValueError("Buku tidak ditemukan.")

    print("Kosongkan (tekan Enter) jika tidak ingin mengubah.")
    judul = input(f"Judul baru ({item['judul']}): ")
    kategori = input(f"Kategori baru ({item['kategori']}): ")
    stok_teks = input(f"Stok baru ({item['stok']}): ")

    stok = None
    if stok_teks.strip() != "":
        stok = ke_angka(stok_teks)

    kelola_buku.ubah_buku(data["buku"], kode, judul, kategori, stok)
    print("Data buku diperbarui!")


def menu_hapus_buku(data):
    print("=== HAPUS BUKU ===")
    kode = input("Kode buku yang dihapus: ")
    kelola_buku.hapus_buku(data["buku"], data["peminjaman"], kode)
    print("Buku berhasil dihapus!")


def menu_per_kategori(data):
    print("=== BUKU PER KATEGORI ===")
    kategori_unik = kelola_buku.daftar_kategori(data["buku"])  # set
    kelompok = kelola_buku.kelompokkan_per_kategori(data["buku"])  # dictionary

    if len(kategori_unik) == 0:
        print("Belum ada buku.")
        return

    print("Jumlah kategori:", len(kategori_unik))
    for kategori in sorted(kategori_unik):
        print()
        print("Kategori:", kategori)
        for item in kelompok[kategori]:
            print(f"  - {item['kode']} {item['judul']} (stok: {item['stok']})")


def menu_stok(data):
    print("=== STOK BUKU ===")
    if len(data["buku"]) == 0:
        print("Belum ada buku.")
        return
    for item in data["buku"]:
        print(f"{item['judul']:<25}: {item['stok']}")