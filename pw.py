#! Python3
# pw.py Um programa de proteção de senhas inseguro...

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print(' Forma de usar: python3 pw.py [conta] - copiar senha da conta ')
    sys.exit()

account = sys.argv[1]       # O primeiro argumento é o nome da conta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Senha para ",account," copiada para área de transferência")
else:
    print(" Não existe conta ",account," cadastrada.")

"""
O amor por graziele não tem fim
"""
