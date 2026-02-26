import time
import random 

MAX_RETRIES = 5
attempts = 0

while attempts < MAX_RETRIES:
    attempts += 1
    print("Attempt " + str(attempts) + ": Connecting to the server...") #without f-string
    print(f"Attempt {attempts}: Connecting to the server...")  #The f before the string makes it an f-string (formatted string literal).
    # Simulating a connection scenario
    time.sleep(0.3)
    if random.choice([False, False, False, True]):
        print("Connection successful!")
        break
    print("Connection failed. Retrying...")
else:
    print("All attempts failed. Unable to connect.")