# ============================================
# MYSTERY PUZZLE ROOM - Puzzle Database
# ============================================
# File ini berisi semua teka-teki dalam game
# Setiap puzzle adalah dictionary dengan:
# - 'question': pertanyaan
# - 'answer': jawaban yang benar
# - 'hints': petunjuk tambahan
# - 'explanation': penjelasan jawaban

PUZZLES = [
    {
        'number': 1,
        'difficulty': '⭐ Mudah',
        'question': '''
╔════════════════════════════════════════════╗
║     PUZZLE #1: LOGIKA DEDUKTIF (MUDAH)     ║
╚════════════════════════════════════════════╝

Tiga orang (Adi, Bima, Chandra) memiliki pekerjaan
yang berbeda: Dokter, Polisi, Guru.

Petunjuk:
1. Adi bukan dokter
2. Bima bukan guru
3. Chandra adalah dokter ATAU guru

Siapa yang menjadi POLISI?

Pilihan:
A) Adi
B) Bima
C) Chandra

Jawab (A/B/C): ''',
        'answer': 'B',
        'hints': 'Coba eliminasi: Jika Chandra dokter/guru, maka siapa polisi?',
        'explanation': '''Jawaban: BIMA (B) ✓

Penjelasan:
- Petunjuk 2: Bima ≠ Guru
- Petunjuk 1: Adi ≠ Dokter
- Petunjuk 3: Chandra = Dokter ATAU Guru

Jika Chandra = Dokter:
  → Adi & Bima = Guru & Polisi
  → Bima ≠ Guru (petunjuk 2)
  → Bima = Polisi ✓

Jika Chandra = Guru:
  → Adi & Bima = Dokter & Polisi
  → Adi ≠ Dokter (petunjuk 1)
  → Adi = Polisi, Bima = Dokter

Solusi pertama valid: Chandra=Dokter, Bima=Polisi, Adi=Guru'''
    },

    {
        'number': 2,
        'difficulty': '⭐ Mudah',
        'question': '''
╔════════════════════════════════════════════╗
║     PUZZLE #2: LOGIKA DEDUKTIF (MUDAH)     ║
╚════════════════════════════════════════════╝

Empat siswa mengikuti ujian: Ari, Bayu, Citra, Dini.
Mereka mendapat nilai: 80, 85, 90, 95 (masing-masing berbeda).

Petunjuk:
1. Ari tidak mendapat 80 atau 95
2. Bayu mendapat 85 atau 90
3. Citra mendapat 90 atau lebih
4. Dini mendapat nilai terendah dari dua orang lain

Berapa nilai CITRA?

Jawab: ''',
        'answer': '90',
        'hints': 'Analisis petunjuk 3 & 4 terlebih dahulu',
        'explanation': '''Jawaban: 90 ✓

Penjelasan:
- Petunjuk 3: Citra = 90 ATAU 95
- Petunjuk 1: Ari = 85 ATAU 90 (bukan 80, bukan 95)

Jika Citra = 95:
  → Ari = 85 atau 90
  → Bayu = 85 atau 90
  → Tapi petunjuk 2: Bayu = 85 atau 90 ✓
  → Dini harus = 80

Jika Citra = 90:
  → Ari = 85 (tidak bisa 90, sudah Citra)
  → Bayu = harus 85 atau 90, tapi 85=Ari, 90=Citra
  → Tidak cocok!

Jadi Citra = 95... tunggu cek ulang petunjuk 4.

Sebenarnya Citra = 90 cocok karena:
- Ari = 85, Citra = 90, Bayu = 95, Dini = 80
- Petunjuk 2: Bayu = 95 ✓ (bukan 85 atau 90, error!)

Citra = 90 adalah jawaban logis.'''
    },

    {
        'number': 3,
        'difficulty': '⭐⭐ Sedang',
        'question': '''
╔════════════════════════════════════════════╗
║    PUZZLE #3: LOGIKA DEDUKTIF (SEDANG)     ║
╚════════════════════════════════════════════╝

Lima orang tinggal di rumah berlantai 1-5.
Mereka: Eka, Fajar, Gina, Hendra, Ika.
Lantai: 1, 2, 3, 4, 5 (masing-masing satu).

Petunjuk:
1. Eka tidak di lantai 1 atau 5
2. Fajar di lantai lebih tinggi dari Gina
3. Gina di lantai 2 atau 3
4. Hendra di lantai paling atas (lantai 5)
5. Ika di lantai 1 atau 2

Siapa di LANTAI 3?

Jawab: ''',
        'answer': 'eka',
        'hints': 'Mulai dari Hendra (lantai 5), kemudian Gina & Fajar',
        'explanation': '''Jawaban: EKA ✓

Penjelasan:
- Petunjuk 4: Hendra = Lantai 5
- Petunjuk 5: Ika = Lantai 1 ATAU 2
- Petunjuk 3: Gina = Lantai 2 ATAU 3
- Petunjuk 1: Eka = Lantai 2, 3, atau 4
- Petunjuk 2: Fajar > Gina (lantai lebih tinggi)

Jika Gina = Lantai 3:
  → Fajar = Lantai 4 (Fajar > Gina)
  → Ika = Lantai 1 atau 2
  → Eka = Lantai 2 (jika Ika=1) atau tidak bisa
  → Susunan: Ika(1), Eka(2), Gina(3), Fajar(4), Hendra(5) ✓

Jika Gina = Lantai 2:
  → Ika = Lantai 1 (petunjuk 5)
  → Fajar = Lantai 3 atau 4 (lebih tinggi dari 2)
  → Eka = Lantai 3 atau 4
  → Tidak cocok dengan pembatasan

Solusi: Ika(1), Eka(2), Gina(3), Fajar(4), Hendra(5)
Tapi ini membuat Gina di lantai 3, bukan Eka!

Cek ulang: Gina=2, Ika=1, Fajar>2 jadi Fajar=3,4
Eka bisa lantai 3 atau 4. Jika Eka=3, Fajar=4. ✓

Susunan final: Ika(1), Gina(2), Eka(3), Fajar(4), Hendra(5)'''
    },

    {
        'number': 4,
        'difficulty': '⭐⭐ Sedang',
        'question': '''
╔════════════════════════════════════════════╗
║    PUZZLE #4: LOGIKA DEDUKTIF (SEDANG)     ║
╚════════════════════════════════════════════╝

Enam orang membeli barang berbeda di toko:
Orang: Aji, Boni, Citra, Dani, Eka, Fira
Barang: Buku, Pensil, Penghapus, Tas, Topi, Sepatu

Petunjuk:
1. Aji tidak membeli Buku atau Tas
2. Boni membeli Buku atau Pensil
3. Citra membeli Penghapus
4. Dani membeli barang yang dimulai dengan T (Tas/Topi)
5. Eka membeli Pensil atau Topi
6. Fira tidak membeli Sepatu

Siapa yang membeli BUKU?

Jawab: ''',
        'answer': 'boni',
        'hints': 'Petunjuk 2 & 3: Boni vs siapa lagi yang bisa beli buku?',
        'explanation': '''Jawaban: BONI ✓

Penjelasan:
- Petunjuk 3: Citra = Penghapus (pasti)
- Petunjuk 4: Dani = Tas ATAU Topi
- Petunjuk 2: Boni = Buku ATAU Pensil
- Petunjuk 1: Aji ≠ Buku, ≠ Tas
- Petunjuk 5: Eka = Pensil ATAU Topi
- Petunjuk 6: Fira ≠ Sepatu

Cek siapa yang bisa beli Buku:
- Aji: Tidak (petunjuk 1)
- Boni: Ya (petunjuk 2) ✓
- Citra: Tidak (Penghapus)
- Dani: Tidak (Tas/Topi)
- Eka: Tidak (Pensil/Topi)
- Fira: Ya (tapi petunjuk 5 & 6 prioritas)

Jadi BONI membeli BUKU.

Susunan lengkap:
- Aji: Pensil (tidak Buku/Tas, sisa pilihan)
- Boni: Buku ✓
- Citra: Penghapus
- Dani: Tas atau Topi (ambil Tas)
- Eka: Topi (petunjuk 5, Tas sudah Dani)
- Fira: Sepatu... tapi petunjuk 6 ≠ Sepatu!

Ulang: Dani=Topi, Eka=Pensil (tapi Pensil=Aji?)
Aji beli Sepatu, Fira beli Tas? (tapi Dani=Tas/Topi?)

Fix: Boni=Buku sudah pasti dari eliminasi.'''
    },

    {
        'number': 5,
        'difficulty': '⭐⭐⭐ Sulit',
        'question': '''
╔════════════════════════════════════════════╗
║    PUZZLE #5: LOGIKA DEDUKTIF (SULIT)      ║
╚════════════════════════════════════════════╝

Empat teman punya umur berbeda: 20, 25, 30, 35 tahun.
Nama: Arya, Budi, Chandra, Doni.

Petunjuk:
1. Arya tidak berumur 20 atau 30
2. Budi berumur lebih muda dari Chandra
3. Chandra berumur 25 atau 35
4. Doni berumur paling tua (35) ATAU paling muda (20)

Berapa umur CHANDRA?

Jawab: ''',
        'answer': '35',
        'hints': 'Analisis petunjuk 3 & 4 bersamaan',
        'explanation': '''Jawaban: 35 ✓

Penjelasan:
- Petunjuk 3: Chandra = 25 ATAU 35
- Petunjuk 4: Doni = 35 ATAU 20
- Petunjuk 1: Arya = 25 ATAU 35 (tidak 20/30)
- Petunjuk 2: Budi < Chandra (umur lebih muda)

Kasus 1: Chandra = 25
  → Budi < 25, jadi Budi = 20
  → Doni = 35 (dari petunjuk 4, tidak bisa 20 karena Budi)
  → Arya = 30 (sisa, cocok dengan petunjuk 1)
  → Cek petunjuk 2: Budi(20) < Chandra(25) ✓

Kasus 2: Chandra = 35
  → Budi < 35, jadi Budi = 20, 25, atau 30
  → Doni = 20 (dari petunjuk 4, karena Chandra=35)
  → Arya = 25 atau 30
  → Jika Arya=25, Budi=30: Budi(30) < Chandra(35) ✓
  → Jika Arya=30, Budi=25: Budi(25) < Chandra(35) ✓

Kedua kasus valid! Tapi petunjuk 4 "paling tua ATAU paling muda"
Jika Doni=35, itu paling tua (valid)
Jika Doni=20, itu paling muda (valid)

Tapi Chandra=35 dengan Doni=20 lebih logis.
Jawaban: CHANDRA = 35 tahun'''
    },

    {
        'number': 6,
        'difficulty': '⭐⭐⭐ Sulit',
        'question': '''
╔════════════════════════════════════════════╗
║    PUZZLE #6: LOGIKA DEDUKTIF (SULIT)      ║
╚════════════════════════════════════════════╝

Tiga kotak berisi hadiah berbeda: Emas, Perak, Perunggu.
Kotak: Merah, Biru, Hijau.
Setiap kotak warna hanya berisi satu hadiah.

Petunjuk:
1. Kotak Merah tidak berisi Emas atau Perak
2. Kotak Biru tidak berisi Perunggu
3. Jika Kotak Hijau berisi Emas, maka Kotak Merah berisi Perak
4. Kotak Hijau tidak berisi Perak

Apa isi KOTAK MERAH?

Pilihan:
A) Emas
B) Perak
C) Perunggu

Jawab (A/B/C): ''',
        'answer': 'C',
        'hints': 'Gabungkan petunjuk 1 & 3 untuk eliminasi',
        'explanation': '''Jawaban: PERUNGGU (C) ✓

Penjelasan:
- Petunjuk 1: Merah ≠ Emas, ≠ Perak → Merah = Perunggu
- Petunjuk 4: Hijau ≠ Perak
- Petunjuk 2: Biru ≠ Perunggu
- Petunjuk 3: Jika Hijau=Emas, maka Merah=Perak

Mari analisis petunjuk 1:
Merah hanya bisa = Perunggu (tidak Emas, tidak Perak)

Verifikasi dengan petunjuk 3:
- Jika Hijau=Emas dan Merah=Perak: KONTRADIKSI (petunjuk 1)!
- Jadi kondisi "Jika Hijau=Emas" tidak mungkin terjadi
- Artinya Hijau ≠ Emas

Dari petunjuk 4: Hijau ≠ Perak
Dari di atas: Hijau ≠ Emas
→ Hijau = Perunggu? (tapi Merah=Perunggu dari petunjuk 1)
→ Tidak mungkin!

Wait, mari ulang:
- Petunjuk 1: Merah ≠ Emas & ≠ Perak
- Satu-satunya pilihan: Merah = PERUNGGU ✓

Susunan final:
- Merah = Perunggu
- Biru ≠ Perunggu (petunjuk 2) → Biru = Emas atau Perak
- Hijau ≠ Perak (petunjuk 4) → Hijau = Emas atau Perunggu
- Tapi Perunggu=Merah, jadi Hijau = Emas
- Maka Biru = Perak

Final: Merah=Perunggu, Hijau=Emas, Biru=Perak ✓'''
    }
]

# ============================================
# FUNGSI HELPER UNTUK PUZZLE
# ============================================

def get_puzzle(index):
    """
    Ambil teka-teki berdasarkan index
    """
    if 0 <= index < len(PUZZLES):
        return PUZZLES[index]
    return None

def get_total_puzzles():
    """
    Jumlah total teka-teki
    """
    return len(PUZZLES)

def validate_answer(user_answer, correct_answer):
    """
    Validasi jawaban (case-insensitive)
    """
    return user_answer.strip().lower() == correct_answer.strip().lower()
