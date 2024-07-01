import time
import sys

f = None
try:
    f = open("resume.json", "r")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=" ")
        sys.stdout.flush()
        # print("Parsing file...")

        time.sleep(0.5)

except IOError:
    print("Failed to open resume.json")
except KeyboardInterrupt:
    print("keyboard interrupt")
finally:
    if f:
        f.close()
    print("Cleaning up resume.json!!!!")
