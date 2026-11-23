"""Problem Statement 
A parking facility charges a flat fee of rupees 30 for packing upto 2 hours, rupees 10 of the next 3 hours,and rupees 5 for every additional hour 

Input:
1

Output:
Parking Fee: Rs. 30

"""

parked_hours = int(input())

if parked_hours <= 2:
    print("Parking Fee: Rs.",30)
elif parked_hours <= 5:
    print("Parking Fee: Rs.",30+(parked_hours-2)*10)    
else:
    print("Parking Fee: Rs.",30+3*10+(parked_hours-5)*5)                