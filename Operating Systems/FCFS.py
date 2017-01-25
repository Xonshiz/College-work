#!/usr/bin/env python
"""
Author : Dhruv Kanojia (Xonshiz)
First Come, First Serve Scheduling Implementation in Python.
Support for Python 3 only.
"""

def main():
    process_que = []
    burst_time = []
    waiting_time = []
    turn_around = []

    total_processes = input("Enter Total Number of Processes : ")

    if total_processes != '0':
        for i in range(int(total_processes)):
            process_que.append(input("Enter Process Name : "))
            burst_time.append(input("Enter Process Burst Time : "))
            if i == 0:
                waiting_time.insert(0, 0)
            waitingCalculator = int(burst_time[i]) + int(waiting_time[i])
            waiting_time.insert(i+1, waitingCalculator)

            turnaroundCalculator = int(burst_time[i]) + int(waiting_time[i])
            turn_around.insert(i, turnaroundCalculator)
        waiting_time.pop()
        print("Process Name\t| Burst Time\t| Waiting Time\t| Turn Around Time")
        caption_list = ['Process Name', 'Burst Time', 'Waiting Time', 'Turn Around Time']
        print('-'*60)

        for x, y, z, k in zip(process_que, burst_time, waiting_time, turn_around):
            print(str(x) + ' \t\t\t\t|', str(y) + ' \t\t\t|', str(z) + ' \t\t\t|', str(k))
        print('\n');print('-' * 60)
        print("Average Waiting Time : %s" % (sum(waiting_time)/ len(waiting_time)))
        print("Average Turn Around Time : %s" % (sum(turn_around) / len(turn_around)))
        print('-' * 60)



if __name__ == '__main__':
    main()