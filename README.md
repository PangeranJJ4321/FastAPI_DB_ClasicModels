# 📦 FastAPI DB Classicmodels

API ini dibangun menggunakan **FastAPI** dengan arsitektur **layered** untuk mengelola data dari database **ClassicModels** (MySQL). Cocok untuk pembelajaran maupun pengembangan API yang clean, scalable, dan mudah di-maintain. ✨

## 🚀 Tech Stack

- **FastAPI** - Web framework modern & cepat
- **MySQL** - Relational database
- **Uvicorn** - ASGI server untuk development
- **Pydantic** - Validasi data dan schema
- **Python 3.11.2 wajib**

## 🗂️ Struktur Proyek

```bash
.
├── auth/
├── controllers/
│   └── controller.py
├── database/
├── fastapi_clasicmodels/
├── middleware/
├── models/
│   └── models.py
├── repositories/
├── routes/
│   └── routes.py
├── schemas/
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
      <td><code>routes/</code></td>
      <td>Menangani routing endpoint</td>
    </tr>
    <tr>
      <td><code>controllers/</code></td>
      <td>Menampung logika pemrosesan dan interaksi antar layer</td>
    </tr>
    <tr>
      <td><code>services/</code></td>
      <td>Menjalankan logika bisnis utama</td>
    </tr>
    <tr>
      <td><code>repositories/</code></td>
      <td>Berinteraksi langsung dengan database</td>
    </tr>
    <tr>
      <td><code>models/</code></td>
      <td>Struktur tabel & ORM</td>
    </tr>
    <tr>
      <td><code>schemas/</code></td>
      <td>Validasi data masuk & keluar (menggunakan Pydantic)</td>
    </tr>
  </tbody>
</table>

## 📌 Fitur, CRUD for all tables, (Contoh)
🔍 Get all customers
🛍️ Add new order
📦 Update product stock
🧾 Get sales report by employee
🔐 Authentication (opsional), ada yah

## 🧪 Cara Menjalankan

1. Clone repo ini
  ```bash
  https://github.com/PangeranJJ4321/FastAPI_DB_ClasicModels.git
  cd FastAPI_DB_ClasicModels
  code .
  ```
2. Aktifkan virtual environment
   Tentukan nama virtual environmemnt kamu, masal disini namanya fastapi-db-classicmodels.
   Buka terminal git bash yah!, jalankan code berikut :
   ```bash
   python -m venv fastapi-db-classicmodels
   source fastapi-db-classicmodels/bin/activate  # atau source fastapi-db-classicmodels\Scripts\activate di Windows
   ```
4. Install dependency
   ```bash
   pip install -r requirements.txt
   ```
6. Buat file .env 
   Isi file .env dengan copy isi file .env.development dan isi dengan konfigurasi MySQL kamu, contoh : 
   ```env
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=classicmodels
   ```
   Catatan : Buat data base dulu yah di heidiSQL dengan nama classicmodels, atau misalnya
   kalian sudah memiliki database tersebut itu juga tidak masalah.
8. Jalankan server(project)
   Buka terminal vs code kamu lagi, janlankan :
   ```bash
   uvicorn main:app --reload
   ```
   atau
   ```bash
   fastapi dev main.py
   ```

9. Akses dokumentasi Swagger UI dan Uji coba API
   Uji API bisa di aplikasi Postman, contoh untuk mendapatkan data customers :
   ```bash
   http://127.0.0.1:8000/api/v1/customers
   ```
   atau kalian juga bisa melalui :
   ```bash
   http://localhost:8000/docs
   ```


##---Terima kasih
   
   


