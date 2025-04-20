# 📦 FastAPI DB Classicmodels

API ini dibangun menggunakan **FastAPI** dengan arsitektur **layered** untuk mengelola data dari database **ClassicModels** (MySQL). 
Cocok untuk pembelajaran maupun pengembangan API yang clean, scalable, dan mudah di-maintain. ✨

## 🚀 Tech Stack

- **FastAPI** - Web framework modern & cepat
- **MySQL** - Relational database
- **Uvicorn** - ASGI server untuk development
- **Pydantic** - Validasi data dan schema
- **JWT** - Authentication dengan JSON Web Tokens
- **Python 3.11.2 wajib**

## 🗂️ Struktur Proyek

```bash
.FastAPI_DB_ClasicModels
├── auth/
│   └── auth.py           # JWT authentication handler
├── controllers/
│   └── controller.py
│   └── auth_controller.py
├── database/
│   └── base.py
│   └── session.py
├── fastapi_clasicmodels/
├── middleware/
│   └── middleware.py
├── models/
│   └── models.py
├── repositories/
│   └── repositories.py
├── routes/
│   └── routes.py
├── schemas/
│   └── schemas.py
├── services/
│   └── service.py
├── main.py
├── .env
├── .env.development
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔐 Environment Variables

Semua konfigurasi disimpan di file `.env.development`. Contoh isi:

```env
# === MySQL ===
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=classicmodels

# === JWT Authentication ===
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🧠 Arsitektur Layered

<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Deskripsi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>auth/</code></td>
      <td>Menangani proses autentikasi JWT dan otorisasi user</td>
    </tr>
    <tr>
      <td><code>controllers/</code></td>
      <td>Menampung logika pemrosesan request dan penghubung antar layer</td>
    </tr>
    <tr>
      <td><code>database/</code></td>
      <td>Konfigurasi koneksi database dan inisialisasi engine/session</td>
    </tr>
    <tr>
      <td><code>fastapi_clasicmodels/</code></td>
      <td>Package utama aplikasi FastAPI kamu (bisa digunakan untuk config global)</td>
    </tr>
    <tr>
      <td><code>middleware/</code></td>
      <td>Custom middleware seperti logging, CORS, atau error handler</td>
    </tr>
    <tr>
      <td><code>models/</code></td>
      <td>ORM model yang mendeskripsikan tabel-tabel pada database</td>
    </tr>
    <tr>
      <td><code>repositories/</code></td>
      <td>Berisi fungsi-fungsi CRUD yang langsung berinteraksi dengan database</td>
    </tr>
    <tr>
      <td><code>routes/</code></td>
      <td>Menangani definisi endpoint dan path operasi API</td>
    </tr>
    <tr>
      <td><code>schemas/</code></td>
      <td>Definisi schema request dan response menggunakan Pydantic</td>
    </tr>
    <tr>
      <td><code>services/</code></td>
      <td>Berisi logika bisnis dan pengolahan data sebelum masuk ke controller atau repository</td>
    </tr>
    <tr>
      <td><code>main.py</code></td>
      <td>Entry point aplikasi untuk menjalankan FastAPI app</td>
    </tr>
  </tbody>
</table>

## 🔒 Autentikasi JWT

API ini mengimplementasikan autentikasi menggunakan JSON Web Tokens (JWT):

- **Login endpoint**: `/api/v1/auth/login`
- **Token generation**: Otomatis menghasilkan access token saat login berhasil
- **Protected routes**: Endpoint tertentu dilindungi dan memerlukan token valid
- **Role-based access**: Kontrol akses berdasarkan peran user (jika diimplementasikan)

Contoh penggunaan JWT:

```python
# Untuk mengakses protected endpoint
headers = {
    "Authorization": "Bearer your_access_token_here"
}
```

## 📌 Fitur
<ul>
  <li>🔒 User authentication dengan JWT</li>
  <li>🔐 Protected endpoints dengan role-based access control</li>
  <li>🔍 Get all customers</li>
  <li>🛍️ Add new order</li>
  <li>📦 Update product stock</li>
  <li>🧾 Get sales report by employee</li>
  <li>🔄 CRUD operations untuk semua tabel database</li>
</ul>

## 🧪 Cara Menjalankan

1. Clone repo ini
    ```bash
    git clone https://github.com/PangeranJJ4321/FastAPI_DB_ClasicModels.git
    cd FastAPI_DB_ClasicModels
    code .
    ```
2. Aktifkan virtual environment<br/>
   Tentukan nama virtual environmemnt kamu, misal disini namanya fastapi-db-classicmodels.
   Buka terminal git bash, jalankan code berikut:
   ```bash
   python -m venv fastapi-db-classicmodels
   source fastapi-db-classicmodels/bin/activate  # atau source fastapi-db-classicmodels\Scripts\activate di Windows
   ```
3. Install dependency
   ```bash
   pip install -r requirements.txt
   ```
4. Buat file .env <br/>
   Isi file .env dengan copy isi file .env.development dan isi dengan konfigurasi MySQL dan JWT kamu, contoh: 
   ```env
   # Database
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=classicmodels
   
   # JWT Authentication
   SECRET_KEY=your_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
   Catatan: Buat database dulu di heidiSQL dengan nama classicmodels, atau misalnya
   kalian sudah memiliki database tersebut itu juga tidak masalah.
5. Jalankan server(project)<br/>
   Buka terminal VS Code, jalankan:
   ```bash
   uvicorn main:app --reload
   ```
   atau
   ```bash
   fastapi dev main.py
   ```

6. Akses dokumentasi Swagger UI dan Uji coba API<br/>
   Uji API bisa di aplikasi Postman, contoh untuk login:
   ```bash
   POST http://127.0.0.1:8000/api/v1/auth/login
   ```
   Untuk mengakses protected endpoint seperti customers:
   ```bash
   GET http://127.0.0.1:8000/api/v1/customers
   ```
   dengan header:
   ```
   Authorization: Bearer your_access_token
   ```
   
   Atau kalian juga bisa melalui Swagger UI:
   ```bash
   http://localhost:8000/docs
   ```

## 📝 Prosedur Autentikasi

1. Login dengan kredensial melalui endpoint `/api/v1/auth/login`
2. Simpan access token yang diterima dari response
3. Sertakan token dalam header Authorization untuk setiap request ke protected endpoint
4. Token akan expired setelah waktu tertentu (default: 30 menit)

---

## 🙏 Terima kasih sudah mampir!

Kalau bermanfaat, jangan lupa kasih ⭐ di repo ini ya