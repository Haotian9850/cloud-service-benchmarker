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
file_size_kb: 1024
node_ips:
  - 127.0.0.1
  - 127.0.0.2
req_times:
  - "19:03:00"
  - "19:03:10"
  - "19:03:20"
  - "19:03:30"
  - "19:03:40"
  - "19:03:50"
  - "19:03:00"
```
*Note that `req_times` must have a one-to-one mapping to `buckets` and are not timezone sensitive.*

#### Provision remote VMs
Put sensitive config info in `Constants.py` in the following format:
```
from enum import Enum 

class Constants(Enum):
    BENCHMARKING_MULTIPLE_LOCAL_CLIENTS = True
    AWS_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXX"
    AWS_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXX"

    USERNAME = "hl7gr"  # your VM username
    NODE_HOSTS = [
        "pc603.emulab.net",
        ...
    ]
    NODE_PORTS = [
        26402,
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




