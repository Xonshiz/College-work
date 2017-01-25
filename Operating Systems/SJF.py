#!/usr/bin/env python
"""
Author : Dhruv Kanojia (Xonshiz)
Shortest Job First Implementation in Python.
Support for Python 3 only.
"""
from sys import exit

def main():
    process_que = []
    burst_time = []
    waiting_time = []
    turn_around = []

    total_processes = input("Enter Total Number of Processes : ")

    if total_processes == 0:
        print("You need to enter at least 1 process to Schedule.")
        exit()

    elif total_processes != 0:
        for i in range(int(total_processes)):
            process_que.append(input("Enter Process Name : "))
            burst_time.append(input("Enter Process Burst Time : "))
        """
        First ZIP both the lists and then make them a dictionary. Now, sort the process name list on the
        basis of the elements in the `value` of the newly created dictionary. Use simple `.sort()` method
        to sort the other list.
        """
        keydict = dict(zip(process_que, burst_time))
        process_que.sort(key=keydict.get)
        burst_time.sort()

    for i in range(int(total_processes)):

        if i == 0:
            waiting_time.insert(0, 0)
        waitingCalculator = int(burst_time[i]) + int(waiting_time[i])
        waiting_time.insert(i + 1, waitingCalculator)

        turnaroundCalculator = int(burst_time[i]) + int(waiting_time[i])
        turn_around.insert(i, turnaroundCalculator)

    waiting_time.pop()
    print("Process Name\t| Burst Time\t| Waiting Time\t| Turn Around Time")
    print('-' * 60)

    for x, y, z, k in zip(process_que, burst_time, waiting_time, turn_around):
        print(str(x) + ' \t\t\t\t|', str(y) + ' \t\t\t|', str(z) + ' \t\t\t|', str(k))
    print('\n');
    print('-' * 60)
    print("Average Waiting Time : %s" % (sum(waiting_time) / len(waiting_time)))
    print("Average Turn Around Time : %s" % (sum(turn_around) / len(turn_around)))
    print('-' * 60)


if __name__ == '__main__':
    main()