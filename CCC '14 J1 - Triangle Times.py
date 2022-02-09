angles = [int(input()) for _ in range(3)]

if angles[0]==angles[1]==angles[2]:
    print("Equilateral")

count = 1

for i in range(2):
    if angles[i]==angles[i+1]:
        count += 1

if angles[0]==angles[2]:
    count += 1

if sum(angles)!=180:
    print("Error") 
elif count==1:
    print("Scalene")
elif count==2:
    print("Isosceles")
elif count==3 and angles[0]:
    print("Equilateral")