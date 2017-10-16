''' Main.py '''

import csv
import time
import pandas as pd


def main():
    ''' The main entry point to the application '''

    df = pd.DataFrame.from_csv("Toggl_time_entries_2017-08-21_to_2017-10-15.csv")
    

    with open("Toggl_time_entries_2017-08-21_to_2017-10-15.csv", 'r') as file:
        data = csv.reader(file)
        first_line = next(data)
        #print(first_line)
        d = dict()
        d["Project"] = list()
        d["Description"] = list()
        d["Start"] = list()
        d["End"] = list()
        d["Duration"] = list()
        first = True
        for line in data:
            print(line)

    



if __name__ == "__main__":
    main()
