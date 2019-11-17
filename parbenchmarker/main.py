import schedule
import time


from FileMaker import FileMaker
from ConfigReader import ConfigReader

CONFIG_PATH = ".config.yaml"

# Does not have to be exception-tolerant due to small number of jobs
if __name__ == "__main__":
    configReader = ConfigReader(CONFIG_PATH)
    fileMaker = FileMaker()

    configuration = ConfigReader.read_config(CONFIG_PATH)



    
