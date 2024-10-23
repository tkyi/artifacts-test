# Create a 1GB file with random content
import os
with open("largefile.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("largefile2.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("largefile3.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data
