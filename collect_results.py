import os

from Constants import Constants

def collect_result(host_name, port, username):
    print("-------------- collecting benchmark results from host {} : {} --------------".format(host_name, port))
    os.system("scp -P {} -i ~/.ssh/id_geni_ssh_rsa {}@{}:/users/{}/parbenchmarker/{} ./results".format(
        port,
        username,
        host_name,
        username,
        "results.csv"
    ))
    os.system("mv ./results/results.csv ./results/results_{}_{}.csv".format(host_name, port))

if __name__ == "__main__":
    for i in range(len(Constants.NODE_HOSTS.value)):
        collect_result(
            Constants.NODE_HOSTS.value[i],
            Constants.NODE_PORTS.value[i],
            Constants.USERNAME.value
        )
