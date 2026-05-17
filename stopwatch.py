import time ;

time_limit = int(input("Enter time limit: ")) 
print("start")
for x in range(time_limit, 0,-1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("over")