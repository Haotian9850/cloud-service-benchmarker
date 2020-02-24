import csv

class ResultWriter():
    
    def __init__(self):
        pass 

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