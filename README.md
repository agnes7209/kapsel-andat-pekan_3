# Kapsel-Andat-Pekan_3
Catatan Perkuliahaan Pekan 3

Penyediaan Python:
Setelah python di-download
Cek di command prompt
    python --version
    kalau python tidak ditemukan, maka kita harus masukin enviorement variables manual
Buka System Properties utk Edit the system enviorement variables (envi)
    Enviroment Variables>Path>Edit
    Tambahkan path folder yg ada python dan Script
Cek ke Command prompt lagi

Penyediaan environment Python:
    Vs Code harus ditutup dahulu
    Cek di command promt, powershell, bash apakah python sudah benar-benar terkoneksi.

Instalasi FastAPI:
    Buat virtual environment (buat di folder Kapsel-Analitika Data).
        python -m venv .venv
    Hanya berlaku jika posisi file python satu level dengan envi

    Aktifkan virtual environment:
        • Windows PowerShell: .venv\Scripts\Activate.ps1
        • Windows Bash: source .venv/Scripts/activate
    Cek virtual environment sudah aktif:
        Windows PowerShell: Get-Command python
    Tambahkan file .gitignore di root folder, ketik: 
        .venv/
    Install FastAPI: 
        pip install "fastapi[standard]"
    Install dari requirements.txt: 
        pip install -r requirements.txt
    Cek FastAPI sudah terinstal: 
        pip show fastapi

Bentuk file bahasa python, misal main.py
Jalankan server (development mode): 
    fastapi dev main.py
    Output:
        • Akses server: 
            http://127.0.0.1:8000
        • Akses dokumentasi:
            Swagger UI: http://127.0.0.1:8000/docs
            ReDoc: http://127.0.0.1:8000/redoc