import os
import time

from RemoteBenchmarker import RemoteBenchMarker
from Constants import Constants



START_BENCHMARKING_COMMAND = "python3 parbenchmarker/main.py"
CLEAN_UP_COMMAND = "rm -r parbenchmarker"


def upload_source_code(host_name, port, username):
    print("-------------- uploading source code for host {} --------------".format(host_name))
    os.system("scp -P {} -i ~/.ssh/id_geni_ssh_rsa -r {} {}@{}:/users/{}".format(
        port,
        "parbenchmarker",
        username,
        host_name,
        username
    ))


def collect_result(host_name, port, username):
    print("-------------- collecting benchmark results from host {} --------------".format(host_name))
    os.system,("scp -P {} -i ~/.ssh/id_geni_ssh_rsa {}@{}:/users/{}/parbenchmarker/{} ./results/{}".format(
        port,
        username,
        host_name,
        username,
        "results.csv",
        "results.csv"
    ))
    os.system("mv ./results/results.csv ./results/results_{}.csv".format(host_name))
    



if __name__ == "__main__":
    for i in range(len(Constants.NODE_HOSTS.value)):
        r = RemoteBenchMarker(
            Constants.NODE_HOSTS.value[i],
            Constants.NODE_PORTS.value[i],
            Constants.USERNAME.value,
            "/home/haotian/.ssh/id_geni_ssh_rsa",
            "123456"
        )
        r.exec_command(["rm -r /users/hl7gr/parbenchmarker"])
        upload_source_code(
            Constants.NODE_HOSTS.value[i],
            Constants.NODE_PORTS.value[i],
            Constants.USERNAME.value
        )
        r.exec_command([
            "sudo apt-get update",
            "sudo apt-get install awscli -y",
            "aws configure set aws_access_key_id {}".format(Constants.AWS_ACCESS_KEY.value),
            "aws configure set aws_secret_access_key {}".format(Constants.AWS_SECRET_KEY.value)
        ])
        r.exec_command(["python3 parbenchmarker/main.py &"]) # start benchmarking in detached mode
        r.close_client()
    
    time.sleep(Constants.BENCHMARKING_TIME.value)

    for i in range(len(Constants.NODE_HOSTS.value)):
        collect_result(
            Constants.NODE_HOSTS.value[i],
            Constants.NODE_PORTS.value[i],
            Constants.USERNAME.value
        )
    
        
        

    