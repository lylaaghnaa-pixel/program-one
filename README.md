# 🧩 Mystery Puzzle Room

Game teka-teki interaktif berbasis **Python terminal** yang mengajarkan logika dan pemikiran kritis.

## 📖 Cerita Game

Anda terbangun di sebuah ruangan misterius tanpa pintu atau jendela. Satu-satunya cara keluar adalah dengan memecahkan **6 teka-teki** yang tersembunyi. Setiap teka-teki yang Anda selesaikan membawa Anda lebih dekat ke **kebebasan**! 🔓

## 🎮 Fitur Game

✅ **6 Teka-teki Berbeda** - Logika, Pola, Kata, Angka  
✅ **Sistem Skor** - Setiap jawaban benar +10 poin  
✅ **Petunjuk** - Bantuan saat menjawab salah  
✅ **UI Terminal** - Visual menarik dengan ASCII art  
✅ **Progress Tracking** - Lihat kemajuan Anda  
✅ **Replayable** - Main berulang kali  

## 🧠 6 Puzzle Deduktif (Semua!)

| # | Nama | Tipe | Kesulitan | Deskripsi |
|----|------|------|-----------|-----------|
| 1 | Pekerjaan | Eliminasi | ⭐ Mudah | Siapa dokter/polisi/guru? |
| 2 | Nilai Ujian | Constraints | ⭐ Mudah | Tentukan nilai masing-masing siswa |
| 3 | Lantai Rumah | Urutan | ⭐⭐ Sedang | Siapa tinggal di lantai 3? |
| 4 | Belanja Barang | Kombinasi | ⭐⭐ Sedang | Siapa membeli buku? |
| 5 | Umur Teman | Multi-kondisi | ⭐⭐⭐ Sulit | Umur Chandra? |
| 6 | Kotak Hadiah | Kontradiksi | ⭐⭐⭐ Sulit | Apa isi kotak merah? |

## 🚀 Cara Menjalankan

### Prerequisites
- Python 3.7+
- Terminal/Command Prompt

### Step 1: Clone Repository (Sudah Ada!)
```bash
cd /workspaces/program-one
```

### Step 2: Jalankan Game
```bash
python game.py
```

**Selesai!** Game akan langsung berjalan di terminal Anda. 🎮

## 📋 Kontrol Game

| Input | Fungsi |
|-------|--------|
| **Ketik Jawaban** | Masukkan jawaban teka-teki |
| **ENTER** | Kirim jawaban / Lanjut |
| **CTRL+C** | Hentikan game |

## 🎯 Cara Bermain

1. **Baca pertanyaan** dengan seksama
2. **Gunakan petunjuk** jika jawaban salah
3. **Ketik jawaban** Anda
4. **Tekan ENTER** untuk submit
5. **Lanjut ke puzzle** berikutnya

## 📁 Struktur File

```
program-one/
├── game.py           # Main game & UI
├── puzzles.py        # Database teka-teki
├── requirements.txt  # Dependencies
└── README.md         # Dokumentasi
```

## 💡 Penjelasan Kode

### `puzzles.py` - Database Teka-Teki
```python
PUZZLES = [
    {
        'number': 1,
        'difficulty': '⭐ Mudah',
        'question': '...',
        'answer': '...',
        'hints': '...',
        'explanation': '...'
    },
]
```

**Struktur Puzzle:**
- `question` - Pertanyaan untuk pemain
- `answer` - Jawaban yang benar
- `hints` - Petunjuk jika salah
- `explanation` - Penjelasan jawaban

### `game.py` - Main Game Loop

**Fungsi Utama:**
- `show_intro()` - Tampilkan cerita
- `print_progress()` - Lihat skor
- `play_puzzle()` - Main satu teka-teki
- `main_game_loop()` - Loop 6 puzzle
- `show_game_over()` - Hasil akhir

**Alur Game:**
```
Intro → Puzzle 1-6 → Validasi → 
Update Score → Lanjut / Game Over → Replay?
```

## 🎓 Konsep Logika Deduktif yang Dipelajari

✅ **Eliminasi** - Singkirkan pilihan yang tidak mungkin  
✅ **Constraint Satisfaction** - Penuhi semua persyaratan  
✅ **Conditional Logic** - Jika-maka reasoning  
✅ **Multi-step Deduction** - Berpikirlebih dari satu langkah  
✅ **Kontradiksi** - Deteksi pernyataan yang bertentangan  
✅ **Set Theory** - Relasi antar elemen  

## 🎯 Cara Menyelesaikan Puzzle Deduktif

**Step 1: Baca Semua Petunjuk**
- Pahami setiap pernyataan dengan jelas

**Step 2: Buat Daftar Opsi**
- Tuliskan semua kemungkinan

**Step 3: Gunakan Eliminasi**
- Coret pilihan yang tidak sesuai petunjuk

**Step 4: Cari Pola**
- Hubungkan petunjuk satu sama lain

**Step 5: Verifikasi**
- Pastikan jawaban memenuhi SEMUA petunjuk

## 🎨 Cara Customize

### Tambah Teka-Teki Baru

Edit `puzzles.py`:
```python
PUZZLES.append({
    'number': 7,
    'difficulty': '⭐⭐ Sedang',
    'question': 'Pertanyaan baru',
    'answer': 'jawaban',
    'hints': 'Petunjuk',
    'explanation': 'Penjelasan'
})
```

### Ubah Skor per Jawaban Benar
Edit `game.py`:
```python
score += 10  # Ubah ke 15, 20, dst
```

## 📊 Scoring System

| Event | Poin |
|-------|------|
| Jawaban Benar | +10 |
| Jawaban Salah | Coba lagi |
| Selesai 6 Puzzle | Total = 60 |

## 🐛 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Game tidak berjalan | Pastikan Python 3.7+ terinstall |
| Error encoding | Gunakan UTF-8 terminal |
| Input tidak terbaca | Terminal harus fokus |

## 💻 Codespaces

```bash
cd /workspaces/program-one
python game.py
```

## 📚 Resource Belajar

- [Python Docs](https://docs.python.org/3/)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

---

**Selamat bermain! Pecahkan semua teka-teki untuk keluar dari ruangan misterius! 🧩✨**
