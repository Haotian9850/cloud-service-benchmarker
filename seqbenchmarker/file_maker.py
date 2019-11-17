def make_file(size_kb, file_name, parent_path):
    with open("{}{}{}kb".format(parent_path, file_name, str(size_kb)), "wb") as f:
        f.write(str.encode("0") * size_kb * 1024)
    return "{}{}kb".format(file_name, str(size_kb))
    