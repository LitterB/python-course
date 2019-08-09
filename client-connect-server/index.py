import paramiko
import datetime
import os

hostname = ''
username = ''
password = ''
port = 10

def connect():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(hostname=hostname, port=port, username=username, password=password)
        print("---------------即将进入命令行交互模式，退出程序请输入exit--------------------")
        while True:
            cmd = input('>:')
            if cmd == 'exit':
                break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
        client.close()
    except Exception as e:
        print(e)

if __name__=='__main__':
    connect()