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


def pacotes():
    os.system("sudo apt-get install network-manager-openvpn network-manager-openvpn-gnome tree vlc pidgin synapse synaptic build-essential gdebi ubuntu-restricted-extras bzip2 curl dia filezilla gimp gip gzip lynx nmap openssh-server openvpn nload rar rsync sshfs traceroute trickle unrar unzip wget wireshark zip fping mtr-tiny whois -y")
    
    
def skype():
    cmds = [ 'wget http://download.skype.com/linux/skype-ubuntu-precise_4.3.0.37-1_i386.deb -O /tmp/skype.deb', 'sudo dpkg -i /tmp/skype.deb' ]
    for cmd in cmds:
        os.system(cmd) 


def dropbox():
    cmds = [ 'wget https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2015.10.28_amd64.deb -O /tmp/dropbox.deb', 'sudo dpkg -i /tmp/dropbox.deb' ]
    for cmd in cmds:
        os.system(cmd) 


def pyenv():
    cmds = [ 'sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev', 'curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash' ]
    for cmd in cmds:
        os.system(cmd)

def spotify():
    cmds = [ 'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886', 'echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list', 'sudo apt-get update', 'sudo apt-get install spotify-client -y' ]
    for cmd in cmds:
        os.system(cmd)


def menu():
    print("Opções:")
    print('1 - Atualizar')
    print('2 - Java')
    print('3 - Pacotes')
    print('4 - Skype')
    print('5 - Dropbox')
    print('6 - Pyenv')
    print('7 - Spotify')
    print('99 - Sair')


def opcoes():
    op = input('Entre com a opção: ')
    if op == '1':
        upgrade()
    elif op == '2':
        java()
    elif op == '3':
        pacotes()
    elif op == '4':
        skype()
    elif op == '5':
        dropbox()
    elif op == '6':
        pyenv()
    elif op == '7':
        spotify()
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
