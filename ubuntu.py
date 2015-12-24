# -*- coding: utf-8 -*-
import subprocess, os

def upgrade():
    cmds= [ 'sudo apt-get update', 'sudo apt-get dist-upgrade' ]
    for cmd in cmds: 
        print(cmd)
        os.system(cmd)

def java():
    cmds= [ 'sudo add-apt-repository ppa:webupd8team/java -y', 'sudo apt-get update', 'sudo apt-get install oracle-java8-installer oracle-java8-set-default -y' ]
    for cmd in cmds:
        os.system(cmd)


def pacotes()
    os.system(sudo apt-get install bzip2 curl dia filezilla gimp gip gzip lynx nmap openssh-server openvpn nload rar rsync sshfs traceroute trickle unrar unzip wget wireshark zip fping mtr-tiny whois)

def menu():
    print("Opções:")
    print('1 - Atualizar')
    print('2 - Java')
    print('99 - Sair')


def opcoes():
    op = input('Entre com a opção: ')
    if op == '1':
        upgrade()
    elif op == '2':
        java()
    elif op == '99':
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
