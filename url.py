import pyshorteners
import sys


n = len(sys.argv)
read = sys.argv[1]

url = pyshorteners.Shortener()
print(url.tinyurl.short(read))