import sys
from subprocess import call

BYTES_PER_KB = 1000
UNITS = ['B', 'KB', 'MB', 'GB']

if len(sys.argv) < 2:
    print('Usage: %s [items] [price]' % sys.argv[0])
    exit(1)

size = sys.argv[1]
unit = float(sys.argv[2])
print("Preprocesingg....")

print(size + " is forecasted to sell out more than 2%, with a final profit of Rs. 43.6")

