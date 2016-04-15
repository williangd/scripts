#!/bin/bash

echo "Testando reverso do IP $1"

saida=`host $1`
RET=$?
#echo ${saida}

if [ "$RET" -ne 0 ]; then
	echo ${saida}
else
	ret_host=$(host $1 | grep pointer | awk '{print $NF}');
	echo Reverso: ${ret_host}
	ret_ip=$(host ${ret_host} | grep "has address" | awk '{print $NF}')
	echo Registro A: ${ret_ip}
		if [ "$1" == "$ret_ip" ]; then
			echo Reverso configurado corretamente
		else
			echo Reverso configurado incorretamente
		fi
fi
