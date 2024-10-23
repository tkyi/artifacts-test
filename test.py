# Create a 1GB file with random content
import os
with open("./artifacts/largefile.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("./artifacts/largefile2.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data

with open("./artifacts/largefile3.bin", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 1024))  # 1GB of random data
