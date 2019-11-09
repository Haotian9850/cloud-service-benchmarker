# Benchmarking cloud storage services
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

### Configure benchmarker
Add desired benchmarking configurations to `config.yaml` as follow:
```
bucket: YOUR_BUCKET_NAME
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
  - 10 
  - 100
  - 1000
  - ...
```

### Start benchmarking
Run the following Bash command inside project root to start benchmarking:
```
$ python3 main.py
```
Benchmarking result will be logged to `benchmarker_log.log`. Below is sample benchmarking result log:

```
INFO:root:Reading config file...
INFO:root:--- Beginning of benchmarking ---
INFO:root:Uploading file test1kb to S3 in region us-east-1: 1.056934901999739s
INFO:root:Downloading file test1kb from S3 in region us-east-1: 1.09172542899978s
...
INFO:root:Uploading file test1kb to S3 in region ca-central-1: 1.0340208799998436s
...
INFO:root:--- End of benchmarking ---
```


