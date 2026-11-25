"""Problem Statement 

A digital clock records the starting and ending times of an event. Calculate its duration in hours and minutes.if the ending time is earlier than the starting time,assume the event continued into the next day. if the starting and ending times are equal, consider the duration to be zero.

Input:
9 15 11 45

Output:
Duration: 02:30
Total Minutes: 150
"""
start_hour,start_minute,end_hour,end_minute = map(int,input().split())
start_total = start_hour*60+start_minute
end_total = end_hour*60+end_minute
if end_total<start_total:
    total = end_total+1440-start_total
else:
    total = end_total-start_total
hours = total//60
minutes = total%60        

print(f"Duration: {hours:02d}:{minutes:02d}")
print("Total Minutes:",total)



