''' Main.py '''

import csv
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt


def read_in_file(file_path):
    ''' Reads in a csv file to a dictionary given file_path '''

    dictionary = dict()
    with open(file_path, 'r') as file:
        data = csv.reader(file)
        next(data)
        dictionary["Project"] = list()
        dictionary["Description"] = list()
        dictionary["Start"] = list()
        dictionary["End"] = list()
        dictionary["Duration"] = list()

        for line in data:
            dictionary["Project"].append(line[3])
            dictionary["Description"].append(line[5])

            start_date = line[7].split("-")
            year = int(start_date[0])
            month = int(start_date[1])
            day = int(start_date[2])
            start_time = line[8].split(":")
            hour = int(start_time[0])
            minute = int(start_time[1])
            second = int(start_time[2])
            dictionary["Start"].append(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second))

            end_date = line[9].split("-")
            year = int(end_date[0])
            month = int(end_date[1])
            day = int(end_date[2])
            end_time = line[10].split(":")
            hour = int(end_time[0])
            minute = int(end_time[1])
            second = int(end_time[2])
            dictionary["End"].append(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second))

            duration = line[11].split(":")
            hour = int(duration[0])
            minute = int(duration[1])
            second = int(duration[2])
            dictionary["Duration"].append(timedelta(hours=hour, minutes=minute, seconds=second))

    return dictionary


def main():
    ''' The main entry point to the application '''

    dictionary = read_in_file("Toggl_time_entries_2017-08-21_to_2017-10-15.csv")
    df = pd.DataFrame(dictionary)
    # print(df.count())
    # print(df[df['Project'] == 'Homework F17'].count()['Project'])
    
    df = df.groupby(by=["Project", "Description"]).sum()
    
    print(df)
    


if __name__ == "__main__":
    main()
