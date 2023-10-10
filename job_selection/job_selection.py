from prettytable import PrettyTable
from colorama import Fore
from util.util import colored_array_print


class __Job:
    def __init__(self, name: str, profit: int, deadline: int) -> None:
        self.name = name
        self.profit = profit
        self.deadline = deadline
        self.is_accepted = None

    
    def __repr__(self) -> str:
        return self.name


def __job_selection(jobs: [__Job], job_table: PrettyTable):
    max_deadline = max(jobs, key=lambda job: job.deadline).deadline
    job_slots = [None] * max_deadline
    jobs.sort(key=lambda job: job.profit, reverse = True)

    for job in jobs:
        inserted = False
        insert_index = job.deadline - 1

        while not inserted and insert_index >= 0:
            if job_slots[insert_index] is None:
                job_slots[insert_index] = job
                inserted = True
                job_table.add_row([job.name, '[ ' + str(insert_index) + ', ' + str(insert_index + 1) + ' ]', 'Accepted', '+' + str(job.profit)])
            else:
                insert_index -= 1
            
        if insert_index < 0:
            job_table.add_row([job.name, 'None', 'Not Accepted', '+' + str(0)])


    return job_slots


def run():
    job_result_table = PrettyTable()
    job_result_table.field_names = ['Job Consider', 'Slot Assign', 'Approval Status', 'Profit']

    jobs = [
        __Job('J1', 20, 3),
        __Job('J2', 15, 4),
        __Job('J3', 25, 4),
        __Job('J4', 10, 1),
        __Job('J5', 15, 3),
        __Job('J6', 12, 1),
        __Job('J7', 30, 2)
    ]

    accepted_jobs = __job_selection(jobs[:], job_result_table)
    job_table = PrettyTable()
    job_table.field_names = ['Job Name', 'Profit', 'Deadline']

    colored_array_print('List of Pending Jobs: ', Fore.YELLOW, False)
    print()

    for job in jobs:
        job_table.add_row([job.name, job.profit, job.deadline])

    print(job_table)
    print()
    colored_array_print('Job Selection Algorithm Result: ', Fore.YELLOW, False)
    print()
    print(job_result_table)
    print()
    colored_array_print("Accepted Jobs: ", Fore.YELLOW, False)
    print(accepted_jobs)
    colored_array_print("Overall Profit: ", Fore.GREEN, False)

    cumulative_profit = 0
    for job in accepted_jobs:
        cumulative_profit += job.profit

    print(cumulative_profit)
