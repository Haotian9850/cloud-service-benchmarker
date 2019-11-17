import csv

class ResultWritter():
    
    def __init__(self):
        pass 

    def log_result(self, bucket, result, csv_name):
        with open(csv_name, "a") as out_file:
            csv.writer(out_file).writerow([bucket, result])