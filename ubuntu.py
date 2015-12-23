# -*- coding: utf-8 -*-
import subprocess, os

def upgrade(debug=False):
    cmds= """
        sudo apt-get update
        sudo apt-get dist-upgrade
    """.strip().splitlines()

    for cmd in cmds:
        os.system(cmd)

def java():
    cmds="""
        add-apt-repository ppa:webupd8tean/java -y
        apt-get update
        apt-get install oracle-java8-installer oracle-java8-set-default -y
    """.strip().splitlines()

    for cmd in cmds:
        os.system(cmd)

def menu():
    print("Opções:")
    print('1 - Atualizar')
    print('2 - Java')
    print('3 - Sair')


def opcoes():
    op = int(input('Entre com a opção: '))
    if op == 1:
        upgrade()
    elif op == 2:
        java()
    elif op == 3:
        print('Saindo..')
    else:
        print('Opção inválida!')
        print('')
        menu()
        opcoes()


def main():
    menu()
    opcoes()

if __name__ == '__main__':
    main()
