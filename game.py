# ============================================
# MYSTERY PUZZLE ROOM - Main Game
# ============================================
# Game teka-teki interaktif berbasis terminal
# Pemain harus memecahkan 6 teka-teki untuk menang

import os
import sys
from puzzles import get_puzzle, get_total_puzzles, validate_answer

# ============================================
# VARIABEL GLOBAL GAME
# ============================================

current_puzzle = 0          # Index puzzle saat ini (0-5)
score = 0                   # Skor pemain
correct_answers = 0         # Jumlah jawaban benar
wrong_attempts = 0          # Jumlah kesalahan
MAX_PUZZLES = get_total_puzzles()

# ============================================
# FUNGSI UTILITY
# ============================================

def clear_screen():
    """
    Bersihkan layar terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """
    Tampilkan header game
    """
    print('''
╔════════════════════════════════════════════╗
║      🧩 MYSTERY PUZZLE ROOM 🧩            ║
║                                            ║
║  Pecahkan teka-teki untuk keluar ruangan! ║
╚════════════════════════════════════════════╝
''')

def print_progress():
    """
    Tampilkan progress pemain
    """
    print(f'\n📊 PROGRESS: {correct_answers}/{MAX_PUZZLES} teka-teki terpecahkan')
    print(f'✓ Benar: {correct_answers} | ✗ Salah: {wrong_attempts} | 🏆 Skor: {score}')
    print('─' * 45)

def print_separator():
    """
    Garis pemisah
    """
    print('─' * 45)

# ============================================
# FUNGSI INTRO & OUTRO
# ============================================

def show_intro():
    """
    Tampilkan intro game
    """
    clear_screen()
    print_header()
    
    print('''
┌────────────────────────────────────────────┐
│              📖 CERITA GAME                │
└────────────────────────────────────────────┘

Anda terbangun di sebuah ruangan misterius.
Tidak ada pintu, tidak ada jendela...

Hanya ada satu jalan keluar: memecahkan semua
teka-teki yang tersembunyi di dalam ruangan.

Setiap teka-teki yang Anda selesaikan akan
membawa Anda lebih dekat ke KEBEBASAN!

Apakah Anda siap menghadapi tantangan? 🧩

─────────────────────────────────────────────
''')
    
    input('Tekan ENTER untuk mulai... ')

def show_game_over(won):
    """
    Tampilkan layar game over
    """
    print_separator()
    
    if won:
        print('''
╔════════════════════════════════════════════╗
║           ✨ ANDA MENANG! ✨              ║
║                                            ║
║     Semua teka-teki telah terpecahkan!    ║
║     Anda berhasil keluar dari ruangan!    ║
╚════════════════════════════════════════════╝
''')
        print(f'🏆 SKOR AKHIR: {score} poin')
        print(f'✓ Jawaban Benar: {correct_answers}/{MAX_PUZZLES}')
        print(f'✗ Kesalahan: {wrong_attempts}')
    else:
        print('''
╔════════════════════════════════════════════╗
║           💔 GAME OVER 💔                 ║
║                                            ║
║    Anda tidak bisa keluar dari ruangan...  ║
║              Coba lagi! 🧩                ║
╚════════════════════════════════════════════╝
''')
        print(f'Skor: {score} poin')
        print(f'Terjebak di Puzzle #{current_puzzle + 1}')
    
    print_separator()

# ============================================
# FUNGSI MAIN GAME LOOP
# ============================================

def play_puzzle(puzzle_index):
    """
    Main game loop untuk satu puzzle
    
    Args:
        puzzle_index: Index puzzle (0-5)
    
    Returns:
        True jika jawaban benar, False jika salah
    """
    global score, correct_answers, wrong_attempts
    
    puzzle = get_puzzle(puzzle_index)
    
    if puzzle is None:
        return False
    
    clear_screen()
    print_header()
    print_progress()
    
    # Tampilkan pertanyaan
    print(puzzle['question'], end='')
    
    # Input jawaban dari pemain
    user_answer = input()
    
    # Validasi jawaban
    if validate_answer(user_answer, puzzle['answer']):
        # ✓ JAWABAN BENAR
        print(f'\n✅ BENAR! {puzzle["explanation"]}')
        score += 10
        correct_answers += 1
        print(f'\n🎉 +10 poin! Total: {score}')
        input('\nTekan ENTER untuk lanjut ke puzzle berikutnya... ')
        return True
    else:
        # ✗ JAWABAN SALAH
        print(f'\n❌ SALAH!')
        print(f'Petunjuk: {puzzle["hints"]}')
        print(f'Jawaban yang benar: {puzzle["answer"]}')
        print(f'\n{puzzle["explanation"]}')
        wrong_attempts += 1
        print(f'\n⚠️ Kesalahan ke-{wrong_attempts}')
        input('\nTekan ENTER untuk lanjut... ')
        return False

def main_game_loop():
    """
    Loop utama game - jalankan semua puzzle
    """
    global current_puzzle
    
    show_intro()
    
    # Loop melalui semua puzzle
    for puzzle_idx in range(MAX_PUZZLES):
        current_puzzle = puzzle_idx
        
        # Mainkan puzzle
        play_puzzle(puzzle_idx)
    
    # Game selesai - player menang
    clear_screen()
    print_header()
    show_game_over(True)
    
    # Opsi bermain lagi
    print('\nPilihan:')
    print('1. Main lagi')
    print('2. Keluar')
    
    choice = input('\nMasukkan pilihan (1/2): ').strip()
    
    if choice == '1':
        reset_game()
        main_game_loop()
    else:
        print('\n👋 Terima kasih telah bermain!')
        sys.exit(0)

def reset_game():
    """
    Reset semua variabel untuk game baru
    """
    global current_puzzle, score, correct_answers, wrong_attempts
    
    current_puzzle = 0
    score = 0
    correct_answers = 0
    wrong_attempts = 0

# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == '__main__':
    try:
        main_game_loop()
    except KeyboardInterrupt:
        print('\n\n👋 Game dihentikan oleh pemain.')
        print('Terima kasih sudah bermain!')
        sys.exit(0)
    except Exception as e:
        print(f'\n❌ Error: {e}')
        sys.exit(1)
