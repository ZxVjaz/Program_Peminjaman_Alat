import time
from tqdm import tqdm
from datetime import datetime, timedelta

def show_loading(text, duration=1):
    print(text, end='', flush=True)
    for _ in range(3):
        time.sleep(duration/3)
        print('.', end='', flush=True)
    print()

def progress_bar(duration=5, desc="Memproses"):
    for _ in tqdm(range(100), desc=desc, unit="%", ncols=75):
        time.sleep(duration/100)

def cek_ban(nama):
    # Daftar nama yang diban (case insensitive) dengan tanggal khusus
    banned_users = {
        "reno": {
            "alasan": "sering mengucap kata bokep",
            "durasi": "1 tahun",
            "mulai": datetime(2025, 7, 7),
            "akhir": datetime(2026, 7, 7)  # Ban 1 tahun dari 7-7-2025
        },
        "ibrahim": {
            "alasan": "terlalu ganteng",
            "durasi": "1 tahun",
            "mulai": datetime(2025, 7, 7),
            "akhir": datetime(2026, 7, 7)  # Ban 1 tahun dari 7-7-2025
        },
        "satria": {
            "alasan": "Sering php",
            "durasi": "1 tahun",
            "mulai": datetime(2025, 7, 7),
            "akhir": datetime(2026, 7, 7)  # Ban 1 tahun dari 7-7-2025
        }
    }
    
    nama_lower = nama.lower().strip()
    if nama_lower in banned_users:
        user = banned_users[nama_lower]
        now = datetime.now()
        
        # Jika sudah melewati masa ban
        if now > user['akhir']:
            print(f"\n\033[93mMasa ban untuk {nama} telah berakhir pada {user['akhir'].strftime('%d-%m-%Y')}\033[0m")
            return False
            
        print(f"\n\033[91m{'='*50}\033[0m")
        print(f"\033[91mANDA DILARANG MEMINJAM ALAT!\033[0m")
        print(f"\033[91mNama: {nama}\033[0m")
        print(f"\033[91mAlasan: {user['alasan']}\033[0m")
        print(f"\033[91mDurasi: {user['durasi']} (hingga {user['akhir'].strftime('%d-%m-%Y')})\033[0m")
        print(f"\033[91m{'='*50}\033[0m")
        return True
    return False

def peminjaman_alat():
    while True:  # Loop untuk memungkinkan pengulangan
        print("\n\033[1m=== Sistem Peminjaman Alat ===\033[0m")
        print("1. Siswa mendatangi MR untuk meminjam alat")
        
        # Input data
        show_loading("\n2. Memproses input data", 0.5)
        nama_siswa = input("   • Masukkan nama siswa: ")
        
        # Cek apakah user diban (case insensitive)
        if cek_ban(nama_siswa):
            print("\n\033[91mAkses ditolak! Hubungi administrator untuk bantuan.\033[0m")
            time.sleep(2)
            continue  # Kembali ke awal loop
        
        nama_alat = input("   • Masukkan nama alat yang dipinjam: ")
        
        # Validasi jumlah
        while True:
            try:
                jumlah = int(input("   • Masukkan jumlah alat yang dipinjam: "))
                if jumlah > 0:
                    break
                else:
                    print("   \033[91mJumlah harus lebih dari 0!\033[0m")
            except ValueError:
                print("   \033[91mMasukkan angka yang valid!\033[0m")
        
        # Validasi password
        password_correct = False
        password = "smkn2oke"
        
        print("\n   \033[93mMemverifikasi akses...\033[0m")
        while not password_correct:
            input_password = input("   • Masukkan password meminjam: ")
            
            # Loading validasi 5 detik
            progress_bar(5, "Memvalidasi password")
            
            if input_password.lower() == password:
                password_correct = True
                print("   \033[92mPassword valid!\033[0m")
            else:
                print("   \033[91mAkses ditolak! Coba lagi.\033[0m")
        
        # Menyiapkan dokumen dengan loading 2.5 detik
        progress_bar(2.5, "Menyiapkan dokumen")
        
        print("\n   \033[1mData Peminjaman:\033[0m")
        print(f"   {'• Nama Siswa':<15}: {nama_siswa}")
        print(f"   {'• Alat Dipinjam':<15}: {nama_alat}")
        print(f"   {'• Jumlah':<15}: {jumlah}")
        print("   \033[94mSilahkan tanda tangani data di atas.\033[0m")
        
        # Langsung ke proses pemberian alat (tanpa tekan Enter)
        print("\n4. MR memberikan alat kepada siswa")
        
        # Animasi penyelesaian
        print("\n5. ", end='', flush=True)
        for char in "Peminjaman berhasil!":
            print(char, end='', flush=True)
            time.sleep(0.05)
        print(" ✓\n")
        
        # Tanya apakah ingin meminjam lagi
        ulangi = input("Apakah ada peminjaman lain? (y/n): ").lower()
        if ulangi != 'y':
            break

if __name__ == "__main__":
    peminjaman_alat()