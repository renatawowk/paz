# Este script fará um "scan" da sua máquina, retornando algumas informações:
#1. o nome do dispositivo,
#2. o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
#3. o total de armazenamento em GB e
#4. o armazenamento disponível em GB.

# Essa biblioteca não é nativa e precisa ser instalada. Para isntalar, digite: 
#  pip install psutil
# antes de executar este script :) 


import psutil

def scan_parti():
    nome = list(psutil.disk_partitions())
    armazenamento = list(psutil.disk_usage(path='C:'))
    round(psutil.disk_usage("C:").total/(1024*1024*1024),2)
    print("Nome do dispositivo:", nome[0][1])
    print("Sistema de arquivos:", nome[0][2])
    print("Total de Armazenamento:", round(armazenamento[0]/(1024*1024*1024),2), 'GB')
    print("Total de Armazenamento Disponível:", round(armazenamento[2]/(1024*1024*1024),2), 'GB')
scan_parti()
# versionamento funciona !

