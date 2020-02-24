import csv

class ResultWriter():
    
    def __init__(self):
        pass 

    def log_config(self, num_client, size_kb, between_req, between_bucket, gap_sec, csv_name):
        with open(csv_name, "a+") as out_file:
            csv.writer(out_file).writerow([num_client])
            csv.writer(out_file).writerow([size_kb])
            csv.writer(out_file).writerow([between_req])
            csv.writer(out_file).writerow([between_bucket])
            csv.writer(out_file).writerow([gap_sec])

    def log_result(self, bucket, result, csv_name, req_time=None):
        with open(csv_name, "a+") as out_file:
            if req_time:
                csv.writer(out_file).writerow([
                    req_time,
                    bucket,
                    result
                ])
            else:
                csv.writer(out_file).writerow([bucket, result])