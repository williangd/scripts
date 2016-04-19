#!/bin/bash

all(){
	openssl base64 < $1 | xclip -selection clipboard
	echo "Para colar o código base64, utilize o comando abaixo:"
	echo "openssl base64 -d > arquivo"
}


uso()
{
	echo "syntax: $0 <arquivo>"
	exit 2
}

if [ $# != 1 ]; then
	uso
else
	all $1
fi
