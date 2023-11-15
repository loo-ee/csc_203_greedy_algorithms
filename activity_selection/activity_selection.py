from prettytable import PrettyTable
from colorama import Fore
from util.util import colored_array_print


class __Activity:
    def __init__(self, name, start, finish) -> None:
        self.name = name
        self.start = start
        self.finish = finish

    
    def __repr__(self) -> str:
        return self.name


def __activity_selection(activities: [__Activity], activities_table: PrettyTable):
    activities.sort(key=lambda activity: activity.finish)
    previous_finish = activities[0].finish

    for activity in activities:
        if activity == activities[0] or activity.start >= previous_finish:
            activities_table.add_row([activity.name, activity.start, activity.finish])
            previous_finish = activity.finish


def run():
    given_activities_table = PrettyTable()
    given_activities_table.field_names = ['Activity', 'Start Time (SI)', 'Finish Time (FI)']

    selected_activities_table = PrettyTable()
    selected_activities_table.field_names = ['Activity', 'Start Time (SI)', 'Finish Time (FI)']

    activities = [
        __Activity('A1', 1, 4),
        __Activity('A2', 3, 5),
        __Activity('A3', 0, 6),
        __Activity('A4', 5, 7),
        __Activity('A5', 3, 8),
        __Activity('A6', 5, 9),
        __Activity('A7', 6, 9),
        __Activity('A8', 8, 10),
        __Activity('A9', 8, 12),
        __Activity('A10', 2, 12),
        __Activity('A11', 12, 14),
        __Activity('A12', 12, 16)
    ]

    for activity in activities:
        given_activities_table.add_row([activity.name, activity.start, activity.finish])
        
    __activity_selection(activities, selected_activities_table)

    colored_array_print("Given Activities: ", Fore.YELLOW, False)
    print()
    print(given_activities_table)

    print()
    colored_array_print("Activities Included: ", Fore.YELLOW, False)
    print()
    print(selected_activities_table)
    