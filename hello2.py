import time

counter = 0

while True:
    print("Execution time in minutes: " + str(counter))
    time.sleep(60) # Delay for 1 minute (60 seconds).
    counter = counter + 1
    
    if counter == 55:
        break

print('Out of loop')