import paramiko
from paramiko import SSHClient

class RemoteBenchMarker():
    host_name = ""
    port = -1
    username = "empty"
    key_filename = "empty"
    passphrase = "-1"
    client = None

    def __init__(self, host_name, port, username, key_filename, passphrase):
        self.host_name = host_name
        self.port = port 
        self.username = username
        self.key_filename = key_filename
        self.passphrase = passphrase
        self.client = SSHClient()

    def exec_command(self, commands):
        print("running commands {}".format(commands))
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host_name,
            port=self.port,
            username=self.username,
            key_filename=self.key_filename,
            passphrase=self.passphrase
        )
        # wait for command completion
        for command in commands:      
            stdin, stdout, stderr = self.client.exec_command(command)
            exit_status = stdout.channel.recv_exit_status()
            print("{} : {}".format(exit_status, command))


    def close_client(self):
        self.client.close()
    


        