# Cloud storage service benchmarker
## S3
### Concurrent multi-client benchmarking
#### Configure benchmarker
Add config to `config.yaml` to `parbenchmarker/`as follow:
```
buckets: 
  - hao-us-east-1
  - hao-ap-southeast-2
  - hao-ap-northeast-1
  - hao-eu-west-2
  - hao-sa-east-1
  - hao-ca-central-1
  - hao-us-west-1
regions:
  - us-east-1
  - ap-southeast-2
  - ap-northeast-1
  - eu-west-2
  - sa-east-1
  - ca-central-1
  - us-west-1
file_size_kb: 10240
username: YOUR_GENI_SSH_USERNAME

multi_local_clients: True 
num_local_clients: 5

start_time: "19:45:00"  # must be local time
gap_sec: 120            # time gap between every batch of requests
between_req_sec: 2      # time gap between every successive request in the same batch 
between_bucket_sec: 120 # time gap between every group of requests to the same S3 bucket
total_benchmarking_duration_sec: 86400
```
*Note that `req_times` must have a one-to-one mapping to `buckets` and are not timezone sensitive.*

#### Provision remote VMs
Put sensitive config info in `Constants.py` in the following format:
```
from enum import Enum 


class Constants(Enum):
    BENCHMARKING_MULTIPLE_LOCAL_CLIENTS = True

    AWS_ACCESS_KEY = "AKIAJMIX4WZARFWJHSMQ"
    AWS_SECRET_KEY = "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"

    USERNAME = "hl7gr"
    NODE_HOSTS = [
        "pc602.emulab.net",
        ...
    ]
    NODE_PORTS = [
        26274,
        ...
    ]

    NODE_HOSTS_MULTIPLE_LOCAL_CLIENTS = [   
        "pc1.instageni.ucsd.edu",
        ...
    ]

    NODE_PORTS_MULTIPLE_LOCAL_CLIENTS = [
        25410,
        ...
    ]
```
Run the following command to provision remote VMs:
```
$ python3 setup.py
```
Enter key passphrase when prompted

#### Start benchmarking on remote VMs
After setting times (relative to **local time** of remote VMs' region!) in `config.yaml`, run the following command to upload source code and start benchmarking:
```
$ python3 main.py
```

### Collect benchmarking results
After all clients have finished benchmarking, run the following command to retrieve benchmarking results:
```
$ python3 collect_results.py
```
Enter key passphrase when prompted

Benchmarking results will be stored under `results/`



