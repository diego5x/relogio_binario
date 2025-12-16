# Relógio Binário no Terminal (Python)

Este projeto exibe um **relógio binário** diretamente no terminal, atualizado em tempo real.

----------

## O que é um relógio binário?

Um relógio binário representa as horas e minutos usando **bits (0 e 1)** em vez de números comuns.

-   **● (bolinha escura)** → bit ligado (`1`)
    
-   **○ (bolinha clara)** → bit desligado (`0`)
    

Cada coluna representa:

```
H H   M M

```

-   Dois dígitos para **hora**
    
-   Dois dígitos para **minuto**
    

Cada linha representa um valor binário:

```
8
4
2
1

```

(de cima para baixo)

----------

## Requisitos

-   **Python 3.x**
    
-   Terminal (Linux, macOS ou Windows)
    

Para verificar se o Python está instalado:

```bash
python --version

```

ou

```bash
python3 --version

```

----------

## Como usar

### Baixe ou copie o arquivo

Clone o projeto do github na sua maquina:

```bash
git clone https://github.com/diego5x/relogio_binario.git
```

----------

### Execute o programa

No terminal, vá até a pasta onde o arquivo está salvo e execute:

```bash
python3 relogio_binario.py

```

----------

### O que você verá

Exemplo no terminal:

```
Relógio Binário:
Hora: 20:34
○ ○ ○ ○
○ ○ ○ ●
● ○ ● ○
○ ○ ● ○

```
Para sair do relógio a qualquer momento:

**Pressione `Ctrl + C`**
