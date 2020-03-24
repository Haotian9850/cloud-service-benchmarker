import os 
import time 
from RemoteBenchmarker import RemoteBenchMarker
from Constants import Constants


if __name__ == "__main__":
    for i in range(len(Constants.NODE_HOSTS_MULTIPLE_LOCAL_CLIENTS.value)):
        r = RemoteBenchMarker(
            Constants.NODE_HOSTS_MULTIPLE_LOCAL_CLIENTS.value[i],
            Constants.NODE_PORTS_MULTIPLE_LOCAL_CLIENTS.value[i],
            Constants.USERNAME.value,
            "/Users/haotian/.ssh/id_geni_ssh_rsa",
            "123456"
        )
        r.exec_command([
            "sudo apt-get update",
            "sudo apt-get install awscli -y",
            "aws configure set aws_access_key_id {}".format(Constants.AWS_ACCESS_KEY.value),
            "aws configure set aws_secret_access_key {}".format(Constants.AWS_SECRET_KEY.value),
            "sudo apt-get install python3-pip -y",
            "sudo pip3 install --upgrade pip",
            "sudo pip3 install schedule",
            "sudo pip3 install pyyaml"
        ])
        r.close_client()