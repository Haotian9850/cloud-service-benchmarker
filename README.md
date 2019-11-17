# Cloud storage service benchmarker
## S3 (parallel, multi-machine)





## S3 (sequential, single-machine)
### Configure aws-cli
Run the following Bash command to set up `aws` environment variables

```
$ aws configure
AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: YOUR_DEFAULT_REGION
Default output format [None]: json
```

### Configure benchmarker
Add desired benchmarking configurations to `config.yaml` as follow:
```
buckets: 
  - hao-us-east-1
  - hao-ap-southeast-2
  - hao-ap-northeast-1
  - hao-eu-west-2
  - hao-sa-east-1
  - hao-ca-central-1
  - ...
regions:
  - us-east-1
  - ap-southeast-2
  - ap-northeast-1
  - eu-west-2
  - sa-east-1
  - ca-central-1
  - ...
file_size_kb:
  - 1
  - 128
  - 256
  - 512
  - ...
num_clients: 5
```
- *Note that all `buckets` must be created before benchmarking and match the order of region in `regions`*
- *`num_clients`: number of client you wish to open concurrently to download from a certain AWS S3 bucket*

### Start benchmarking
Run the following Bash command inside project root to start benchmarking:
```
$ python3 benchmarker_multi_client.py
```
A multi-region, multi-file-size download latency plot of benchmarking results will show after benchmarking is finished. Below is a sample plot:



