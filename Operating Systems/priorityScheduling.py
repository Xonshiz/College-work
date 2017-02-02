#!/usr/bin/env Python
from sys import exit
'''
Currently this module needs the FCFS implementation. Right now, it only sorts all the processes based on their
priority. If the priority is same, then the program does the FCFS. It is unclear whether the program
performs "FCFS" scheduling that we did earlier, or it just allocates whoever comes first.
Right now, the program is allocating the resources on the basis of whoever is coming first. Nothing else
has been implemented yet.
'''
def main():
    process_names = []
    burst_time = []
    priority = []
    timer = []
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

        timer, priority, process_names, burst_time = zip(*sorted(zip(timer, priority, process_names, burst_time)))
        for a, b, c, d in zip(process_names,priority, timer, burst_time):
            print(str(a) + ' \t\t\t\t|', str(b) + ' \t\t|', str(d) + ' \t\t|', str(c))

        priority, timer, process_names, burst_time = zip(*sorted(zip(priority, timer, process_names, burst_time), reverse=True))
        for a, b, c, d in zip(process_names,priority, timer, burst_time):
            print(str(a) + ' \t\t\t\t|', str(b) + ' \t\t|', str(d) + ' \t\t|', str(c))

        print('\n')
        print(priority)
        print(burst_time)
        # print(set([x for x in priority if priority.count(x) > 1]))
        # dupes = set([x for x in priority if priority.count(x) > 1])
        # dupes = list(i for i, x in enumerate(timer) if timer.count(x) > 1)
        # print(dupes)
        # for a in dupes:
        #     print(a)
        #     timer, priority, process_names, burst_time = zip(*sorted(zip(timer[a], priority[a], process_names[a], burst_time[a])))

        print("Process Name\t| Priority\t| Burst Time")
        print('-' * 60)

        for a, b, c, d in zip(process_names,priority, timer, burst_time):
            print(str(a) + ' \t\t\t\t|', str(b) + ' \t\t|', str(d) + ' \t\t|', str(c))


if __name__ == '__main__':
    main()
