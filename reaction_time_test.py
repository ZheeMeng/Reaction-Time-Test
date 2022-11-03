import time,random

def get_ms(seconds):
    return round(seconds*1000)

print("\nYou will be tested 3 times.\nDuring the test, please press 'Enter' when prompted.\nPlease press 'Enter' when you are ready.")
a=input()
time_spent=0

for _ in range(3):
    print("The test begins.")
    time.sleep(random.randint(2,10))
    print("Press 'Enter'")
    start=time.time()
    a=input()
    end=time.time()
    time_spent+=end-start

time_spent=get_ms(time_spent/3)
print("The test has ended.\nAverage reaction time: "+str(time_spent)+"ms\nPlease press 'Enter' again to exit.")
a=input()