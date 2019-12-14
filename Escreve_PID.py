# -*- coding: utf-8 -*-
"""

Autor: Daniel Kenji Saito

Descrição: O programa a seguir tem como objetivo escrever seu próprio PID em um
arquivo para que seu status seja monitorado por outro programa. Além disso, esse
deve sinalizar por 3 iterações que está funcionando, aguardando x segundos entre
elas. Por fim, o programa sinaliza que está sendo finalizado.
"""

import os #importa biblioteca OS para usar funçoes relacionadas a PID
import time #importa biblioteca time para usar função sleep

pid_path = "PID.pid" #arquivo

flags = (os.O_CREAT | os.O_RDWR ) # cria o arquivo se não existe ou lê/escreve 
mode = 0o755 #permissões do arquivo 

pid_fd = os.open(pid_path, flags,mode) #local do arquivo PID
pidfile = os.fdopen(pid_fd, 'w') #arquivo PID

pid = os.getpid() #obtém o próprio PID e salva na variável pid
pidfile.write("%s\n" % pid) #Escreve o PID da função no arquivo
pidfile.close() #fecha o arquivo 

wait_time = 1 #Tempo de espera (x) em segundos entre os prints

for i in range(3): #loop de 0 a 2 (3 iterações)
    print("2: I am alive") #sinaliza que programa está em execução
    time.sleep(wait_time) #aguarda os x segundos

print("2: I gonna die now, bye") #sinaliza fim da execução do programa
    


    