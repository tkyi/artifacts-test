# Create a 1GB file with random content
import os
with open("./artifacts/python/largefile.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("./artifacts/python/largefile2.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("./artifacts/python/largefile3.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data
