import os
from datetime import date

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def bin_digit(digito, bits=4):
    return [int(b) for b in format(digito, f'0{bits}b')]

def desenhar_binario_numero(valor, bits_por_digito=4):
    digitos = [int(d) for d in str(valor)]
    colunas = [bin_digit(d, bits_por_digito) for d in digitos]
    linhas = []
    for i in range(bits_por_digito):
        linha = ""
        for col in colunas:
            linha += "● " if col[i] else "○ "
        linhas.append(linha)
    return linhas

def desenhar_calendario_binario():
    data = date.today()
    dia, mes, ano = f"{data.day:02d}", f"{data.month:02d}", f"{data.year:04d}"

    linhas_dia = desenhar_binario_numero(dia)
    linhas_mes = desenhar_binario_numero(mes)
    linhas_ano = desenhar_binario_numero(ano)

    print("Dia  Mês  Ano:\n")
    for i in range(len(linhas_ano)):
        linha = linhas_dia[i] + "  " + linhas_mes[i] + "  " + linhas_ano[i]
        print(linha)

if __name__ == "__main__":
    limpar_tela()
    desenhar_calendario_binario()
