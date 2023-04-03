import csv
import time
import random
import datetime


def get_data_from_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        for row in csvreader:
            data.append(row)
    return data


def action_wait(action):
    wait_time = 0.0
    if action == "read":
        wait_time = random.uniform(2, 5)
    if action == "click":
        wait_time = random.uniform(2, 5)
    if action == "make_choice":
        wait_time = random.uniform(2, 5)

    time.sleep(wait_time)
    return


def chance_of_mistake():
    probability = 0.05
    roll = random.uniform(0, 1)
    if roll > probability:
        return False
    else:
        return True


def success_counter(outcome, success_count, unsuc_count):
    if outcome == True:
        success_count += 1
    if outcome == False:
        unsuc_count += 1
    print(f"Success: {outcome}  - Current Counts:  successful: {success_count}, unsuccessful: {unsuc_count}\n")
    return success_count, unsuc_count

def report_summary(success_count, unsuc_count):
    today = datetime.date.today()

    # Open report.txt in append mode
    with open('report.txt', 'a') as file:
        # Write the data to the file
        file.write(f"{today}: successful: {success_count}, unsuccessful: {unsuc_count}\n")