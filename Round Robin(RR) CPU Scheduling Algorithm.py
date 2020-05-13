"""
-------Round Robin(RR) CPU Scheduling Algorithm-------
------------------By Tareq Alshofi--------------------
"""

from operator import itemgetter

chart = []
# --------------------------------------PROCESS--CLASS-----------------------------------------#
class process:
    def __init__(self, Pid, AT, BT):
        self.Pid = Pid
        self.arrival = AT
        self.burst = BT


def shiftCL(alist):
    temp = alist[0]
    for i in range(len(alist) - 1):
        alist[i] = alist[i + 1]
    alist[len(alist) - 1] = temp
    return alist


def RR(TQ, plist, N):
    global chart
    queueP = []
    time = 0
    arrivedP = 0
    doneP = 0
    readyP = 0
    Q = TQ
    start = 0
    while (doneP < N): 
        for i in range(arrivedP, N):
            if time >= plist[i].arrival:
                queueP.append(plist[i])
                arrivedP += 1
                readyP += 1
        if readyP < 1:
            chart.append(0)
            time += 1
            continue

        if start:
            queueP = shiftCL(queueP)

        if queueP[0].burst > 0:
            if queueP[0].burst > Q:
                for j in range(time, time + Q):
                    chart.append(queueP[0].Pid)
                    # print(chart)
                time += Q
                queueP[0].burst -= Q
            else:
                for j in range(time, time + queueP[0].burst):
                    chart.append(queueP[0].Pid)
                    # print(chart)
                time += queueP[0].burst
                queueP[0].burst = 0
                doneP += 1
                readyP -= 1
            start = 1

        # -----------------------------ENTER--TOTAL--PROCESS--NUMBER------------------------------------#

print("-------Round Robin(RR) CPU Scheduling Algorithm------------\n-------------------By Tareq Alshofi------------------------")
N = input("Please enter total process number:")
is_digit = False
while is_digit == False:
    # For check if the N is a digit
    if N.isdigit():
        is_digit = True  # To stop While
    else:
        print("***** Error,You have to enter digit *****")
        N = input("Please enter total process number:")  # To retry enter N

        # ----------------------------------ENTER--TIME--QUANTUM----------------------------------------#


Qu = input("Please enter time quantum:")
isQu_digit = False
while isQu_digit == False:
    # For check if the Qu is a digit
    if Qu.isdigit():
        isQu_digit = True  # To stop While
    else:
        print("***** Error,You have to enter digit *****")
        Qu = input("Please enter time quantum:")  # To retry enter Q

        # ---------------------------------ENTER--PROCESS--PARAMETERS------------------------------------#
plist_by_input = []
for i in range(int(N)):
    try:
        print('Enter id, arrival time, and burst time for process num ', i + 1, ' separated by space:')
        x = input()
        num_x = x.split(" ")
        process_info = list(map(int, x.split(" ")))
        plist_by_input.append(process_info)
    except:
        print("***** Error,You have to enter digits separated by one space without start or end space *****")
        quit()


    # -------------------------------SORT--PROCESS--BY--ARRIVAL--TIME----------------------------------#
Sorted_plist_By_AT = sorted(plist_by_input, key=itemgetter(1))
plist_for_RR = []
for i in Sorted_plist_By_AT:
    Pid, AT, BT = i[0], i[1], i[2]
    plist_for_RR.append(process(Pid, AT, BT))

RR(int(Qu), plist_for_RR, int(N))

    # -------------------------------FIND--PROCESS--COMPLETION--TIME------------------------------------#
Completion_Time = {}
result_Completion_Time = {}
for i in range(0, len(chart)):
    Completion_Time[i + 1] = chart[i]
for key, value in Completion_Time.items():
    if key not in result_Completion_Time.keys():
        result_Completion_Time[value] = key

        # -------------------------------FIND--PROCESS--TURNAROUND--TIME------------------------------------#
Sorted_plist_By_Pid = sorted(plist_by_input, key=itemgetter(0))
result_TURNAROUND_Time = {}
Total_TURNAROUND_Time = 0
for i , v in sorted(result_Completion_Time.items()) :
    for j in Sorted_plist_By_Pid:
        if i == j[0]:
            r = v - j[1]
            result_TURNAROUND_Time[j[0]] = r
            Total_TURNAROUND_Time = Total_TURNAROUND_Time + r

        # -------------------------------FIND--PROCESS--WAITING--TIME------------------------------------#
result_WAITING_Time = {}
Total_WAITING_Time = 0
for i , v in sorted(result_TURNAROUND_Time.items()) :
    for j in Sorted_plist_By_Pid:
        if i == j[0]:
            r = v - j[2]
            result_WAITING_Time[j[0]] = r
            Total_WAITING_Time = Total_WAITING_Time + r

print("########################THE###SCHEDULING###RESULTS########################")
print("CPU GHANT CHART :",chart)
print("Process Completion Time By Pid :", sorted(result_Completion_Time.items()))
print("Process Turnaround Time By Pid :", sorted(result_TURNAROUND_Time.items()))
print("Process  Waiting  Time  By Pid :", sorted(result_WAITING_Time.items()))
print("Average Turnaround Time = ",(Total_TURNAROUND_Time /int(N) ))
print("Average  Waiting   Time = ",(Total_WAITING_Time / int(N)))

