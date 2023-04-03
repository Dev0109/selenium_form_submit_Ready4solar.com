from browser import browser_bot
from utilities import *

file_path = "file2.csv"

def main_loop():
    data = get_data_from_csv(file_path)
    success_count, unsuc_count = 0, 0
    index = 0

    for row in data:
        index += 1
        print(f"#{index}:  {row}")
        outcome = browser_bot(row)
        success_count, unsuc_count = success_counter(outcome, success_count, unsuc_count)
    report_summary(success_count, unsuc_count)
    return



if __name__ == "__main__":
    main_loop()





