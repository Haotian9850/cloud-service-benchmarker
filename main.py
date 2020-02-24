import os
import time

from RemoteBenchmarker import RemoteBenchMarker
from Constants import Constants


def upload_source_code(host_name, port, username):
    print("-------------- uploading source code for host {} --------------".format(host_name))
    os.system("scp -P {} -i ~/.ssh/id_geni_ssh_rsa -r {} {}@{}:/users/{}".format(
        port,
        "parbenchmarker",
        username,
        host_name,
        username
    ))


if __name__ == "__main__":
    node_hosts = None 
    node_ports = None
    if Constants.BENCHMARKING_MULTIPLE_LOCAL_CLIENTS.value:
        node_hosts = Constants.NODE_HOSTS_MULTIPLE_LOCAL_CLIENTS.value
        node_ports = Constants.NODE_PORTS_MULTIPLE_LOCAL_CLIENTS.value
    else:
        node_hosts = Constants.NODE_HOSTS.value
        node_ports = Constants.NODE_PORTS.value
    for i in range(len(node_hosts)):
        r = RemoteBenchMarker(
            node_hosts[i],
            node_ports[i],
            Constants.USERNAME.value,
            "/Users/haotian/.ssh/id_geni_ssh_rsa",
            "123456"
        )
        r.exec_command(["rm -r /users/hl7gr/parbenchmarker"])
        upload_source_code(
            node_hosts[i],
            node_ports[i],
            Constants.USERNAME.value
        )
        r.exec_command([
            "aws configure set aws_access_key_id {}".format(Constants.AWS_ACCESS_KEY.value),
            "aws configure set aws_secret_access_key {}".format(Constants.AWS_SECRET_KEY.value),
            "sudo pkill python3",
            "sudo chmod +x /users/{}/parbenchmarker/main.py".format(Constants.USERNAME.value),
            "sudo nohup python3 -u /users/{}/parbenchmarker/main.py > nohup.out 2>&1 &".format(Constants.USERNAME.value)
        ])
        r.close_client()
    
        
        

    