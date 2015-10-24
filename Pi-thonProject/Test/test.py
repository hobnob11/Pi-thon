import ptvsd
ptvsd.enable_attach(secret=None)
from time import sleep

print("hi")

X = raw_input("Response: ")

sleep(1)

print(":D")

sleep(1)

Y = raw_input("Response: ")