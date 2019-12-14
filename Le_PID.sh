#!/usr/bin/env bash

file="PID.pid" #Arquivo

while : #Loop infinito
do
    while i= read -r line #Lê arquivo
    do
       PID=line #Salva na variável PID o pid contido no arquivo 
    done < "$file" #até o fim do arquivo

    

    if [ -n "$PID" -a -e /proc/$PID ] #Se estiver rodando o programa
    then
        echo "1: It is alive" #Sinaliza que está rodando
    else
        echo "1: It is dead" #Sinaliza que não está rodando
        python3 Escreve_PID.py #Executa função em python3
        
    fi

done