import os

from Constants import Constants

def collect_result(host_name, port, username):
    print("-------------- collecting benchmark results from host {} : {} --------------".format(host_name, port))
    os.system("scp -P {} -i /Users/haotian/.ssh/id_geni_ssh_rsa {}@{}:/users/{}/parbenchmarker/{} ./results.csv".format(
        port,
        username,
        host_name,
        username,
        "results.csv"
    ))
    os.system("mv ./results.csv ./results/results_{}_{}.csv".format(host_name, port))

if __name__ == "__main__":
    node_hosts = Constants.NODE_PORTS.value
    node_ports = Constants.NODE_PORTS.value
    if Constants.BENCHMARKING_MULTIPLE_LOCAL_CLIENTS.value:
        node_hosts = Constants.NODE_HOSTS_MULTIPLE_LOCAL_CLIENTS.value
        node_ports = Constants.NODE_PORTS_MULTIPLE_LOCAL_CLIENTS.value
    for i in range(len(node_hosts)):
        collect_result(
            node_hosts[i],
            node_ports[i],
            Constants.USERNAME.value
        )
