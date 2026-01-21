#!/usr/bin/env python3
# ============================================
# MYSTERY PUZZLE ROOM - Menu Launcher
# ============================================
# Pilih game mana yang ingin dimainkan

import sys

def show_menu():
    """Tampilkan menu pilihan game"""
    print('''
╔════════════════════════════════════════════╗
║          🎮 PROGRAM ONE - GAMES 🎮        ║
╚════════════════════════════════════════════╝

Pilih game yang ingin dimainkan:

1. 🧩 Mystery Puzzle Room (Terminal)
   - Pecahkan 6 teka-teki
   - Sistem skor
   - Game edukatif

2. 🚀 Space Defender (Pygame)
   - Game arcade
   - Hindari asteroid
   - Tembak musuh

3. 🌐 Catch The Gems (HTML/CSS/JS)
   - Tangkap permata
   - Game browser
   - Buka di browser

0. Keluar

═══════════════════════════════════════════════
''')

def main():
    """Main menu"""
    while True:
        show_menu()
        choice = input('Pilihan (0-3): ').strip()
        
        if choice == '1':
            print('\n🎮 Membuka Mystery Puzzle Room...\n')
            try:
                from game import main_game_loop
                main_game_loop()
            except ImportError:
                print('❌ Error: game.py tidak ditemukan')
                input('Tekan ENTER untuk kembali...')
        
        elif choice == '2':
            print('\n🚀 Membuka Space Defender...\n')
            try:
                import subprocess
                subprocess.run([sys.executable, 'main.py'])
            except Exception as e:
                print(f'❌ Error: {e}')
                input('Tekan ENTER untuk kembali...')
        
        elif choice == '3':
            print('\n🌐 Silakan buka index.html di browser')
            print('Python server: python -m http.server 8000')
            input('Tekan ENTER untuk kembali...')
        
        elif choice == '0':
            print('\n👋 Terima kasih sudah bermain!')
            sys.exit(0)
        
        else:
            print('❌ Pilihan tidak valid!')
            input('Tekan ENTER untuk lanjut...')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n👋 Program dihentikan.')
        sys.exit(0)
