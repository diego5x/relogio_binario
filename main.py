import argparse
import time
import os
from calendario import desenhar_calendario
from relogio import desenhar_relogio

def limpar_tela():  
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    parser = argparse.ArgumentParser(description="Painel binário: calendário ou relógio")
    parser.add_argument('--relogio', action='store_true', help='Mostra o relógio binário')
    parser.add_argument('--calendario', action='store_true', help='Mostra o calendário binário')

    args = parser.parse_args()

    limpar_tela()

    if args.relogio:
        desenhar_relogio()
    elif args.calendario:
        desenhar_calendario()
    else:
        print("Use --relogio para mostrar o relógio ou --calendario para mostrar o calendário.")

if __name__ == "__main__":
    main()
