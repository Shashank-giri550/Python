""" A mobile has a monthly data limit. Given the data limit and data consumed,calculate the remaing data or the extra charge at rupees 20 per GB fopr exceeding the limit.

input:
50 35

Output:
Remaining: 15 GB
Extra charge: Rs. 0
"""


limit, used = input().split()
limit = int(limit)
used = int(used)
if used < limit:
    remaining = limit-used
    print("Remaing:",remaining,"GB")
    print("Extra charge: Rs. 0")
else:
      extra = (used-limit)*20
      print("Remaining: 0 GB")
      print("Extra charge: Rs.",extra)  
      