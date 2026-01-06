# Input data pengguna
full_name = input("Masukkan nama lengkap: ")
phone_number = input("Masukkan nomor telepon: ")
user_email = input("Masukkan email: ")

# List untuk menampung pesan kesalahan
validation_errors = []

# Validasi nama
if not full_name.replace(" ", "").isalpha():
    validation_errors.append("Nama lengkap harus hanya berisi huruf.")

# Validasi nomor telepon
if not phone_number.isdigit():
    validation_errors.append("Nomor telepon harus hanya berisi angka.")

# Validasi email
if "@" not in user_email or "." not in user_email:
    validation_errors.append("Email harus mengandung karakter '@' dan '.'")

# Hasil validasi
if len(validation_errors) == 0:
    print("\nData pendaftaran valid.")
else:
    print("\nTerjadi kesalahan pada input:")
    for msg in validation_errors:
        print(msg)
