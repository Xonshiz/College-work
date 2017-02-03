#!/usr/bin/env Python
from sys import exit
'''
Thanks to Dvlv (https://www.reddit.com/user/Dvlv) for his HUGE help.
https://www.reddit.com/r/learnpython/comments/5rnd9s/sorting_multiple_lists_based_on_2_lists/dd8pc8k/
'''
def main():
    process_names = []
    burst_time = []
    priority = []
    timer = []
    waiting_time = []
    turn_around = []
    total_processes = int(input("Enter the total number of processes : "))
    if total_processes == 0:
        print("You need to enter at least 1 process to Schedule!")
        exit()
    elif total_processes != 0:
        for i in range(total_processes):
            timer.append(int(i))
            process_names.append(input("Enter the Name of the Process : "))
            burst_time.append(int(input("Enter the burst time for the process : ")))
            priority.append(int(input("Enter the Priority of the process : ")))

        priority, timer, process_names, burst_time = zip(*sorted(zip(priority, timer, process_names, burst_time), reverse=True, key=lambda x: (x[0], -x[1])))

        # print("Process Name\t| Priority\t| Burst Time")
        # print('-' * 60)
        #
        # for a, b, c, d in zip(process_names,priority, timer, burst_time):
        #     print(str(a) + ' \t\t\t\t|', str(b) + ' \t\t|', str(d))

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

        for x, y, z, k in zip(process_names, burst_time, waiting_time, turn_around):
            print(str(x) + ' \t\t\t\t|', str(y) + ' \t\t\t|', str(z) + ' \t\t\t|', str(k))
        print('\n');
        print('-' * 60)
        print("Average Waiting Time : %s" % (sum(waiting_time) / len(waiting_time)))
        print("Average Turn Around Time : %s" % (sum(turn_around) / len(turn_around)))
        print('-' * 60)


if __name__ == '__main__':
    main()
