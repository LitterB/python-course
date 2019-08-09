import paramiko
import datetime
import os

class SSHClient(object):
    def ssh_connect(host, port, username, password):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host, port, username, password)
        except Exception as e:
            print(e)
        return ssh_client

    def ssh_exec_cmd(ssh_client, cmd):
        return ssh_client.exec_command(cmd)

    def ssh_close(ssh_client):
        ssh_client.close()

class SFTPClient(object):
    def create_transport(host, port, username, password):
        try:
            transport = paramiko.Transport((host, port))
            transport.connect(username=username, password=password)
        except Exception as e:
            print(e)
        return transport
    
    def upload(transport, localpath, remotepath):   
        sftp_client = paramiko.SFTPClient.from_transport(transport)
        sftp_client.put(localpath, remotepath)
        transport.close()

if __name__ == "__main__":
    hostname = ''
    username = ''
    password = ''
    port = 10
    localpath = "E:/jar/myFile.txt"
    remotepath = "/jw/scrm/gateway/gateway-merchant/myFile.txt"
    print("----------欢迎使用本程序进行自动部署工作，祝您部署顺利！------------")
    #创建ssh客户端并连接
    ssh_client = SSHClient.ssh_connect(hostname, port, username, password)
    #创建sftp_transport传输通道客户端并连接
    sftp_transport = SFTPClient.create_transport(hostname, port, username, password)
    cmd = "cd /jw/scrm/gateway/gateway-merchant; ls"
    stdin,stdout,stderr = SSHClient.ssh_exec_cmd(ssh_client, cmd)
    print(stdout.read().decode('utf-8'))
    #上传文件
    SFTPClient.upload(sftp_transport, localpath, remotepath)
    cmd = "cd /jw/scrm/gateway/gateway-merchant; ls"
    stdin,stdout,stderr = SSHClient.ssh_exec_cmd(ssh_client, cmd)
    print(stdout.read().decode('utf-8'))
    #关闭ssh客户端
    SSHClient.ssh_close(ssh_client)