
class FileMaker():
    def __init__(self):
        pass 

    def make_test_file(self, size_kb, file_name, parent_path):
        with open("{}/{}_{}kb".format(parent_path, file_name, str(size_kb)), "wb") as f:
            f.write(str.encode("0") * size_kb * 1024)
        return "{}_{}kb".format(file_name, str(size_kb))
            