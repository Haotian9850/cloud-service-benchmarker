# Cloud storage service benchmarker
## S3
### Configure aws-cli
Run the following Bash command to set up `aws` environment variables

```
$ aws configure
AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: YOUR_DEFAULT_REGION
Default output format [None]: json
```
### Parallel benchmarking
#### Configure benchmarker
Add config to `config.yaml` as follow:
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
*Note that `req_times` must have a one-to-one mapping to `buckets`* 
#### Start benchmarking
Run the following command to start benchmarker:
```
$ python3 main.py
```
Benchmark results will be stored in `results.csv`



