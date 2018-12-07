# List of files to use as initial seed
file_list=[
  r"C:\Users\luan1\Desktop\Beginner-Guide-To-Software-Testing.pdf",    
  r"C:\Users\luan1\Desktop\cheatsheet-convolutional-neural-networks.pdf"   
  ]

# List of applications to test

apps = [r"C:\Program Files (x86)\Foxit Software\Foxit Reader\Foxit Reader\FoxitReader.exe"]

fuzz_output = r"C:\Users\luan1\Desktop\test_files/test.pdf"

FuzzFactor = 250
num_tests = 10000

########### end configuration ##########

import math
import random
import string
import subprocess
import time
import os

stats = []

for i in range(num_tests):
    file_choice = random.choice(file_list)
    print (file_choice)
    app = random.choice(apps)
    print(app)

    buf = bytearray(open(file_choice, 'rb').read())
    if len(buf) == 0: continue
    # start Charlie Miller code
    numwrites=random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
    print(numwrites)
    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        #buf[rn] = rbyte

    #end Charlie Miller code

    open(fuzz_output, 'wb').write(buf)
    process = subprocess.Popen([app, fuzz_output])
    statinfo = os.stat(file_choice)
    time.sleep(int(statinfo.st_size/10000))
    crashed = process.poll()
    if not crashed:
        process.terminate()
    else:
        stats.append((app, file_choice))

results = open(r"C:\Users\luan1\Desktop\test_files/result.pdf", "wt")
print ('%d crashes\n'%len(stats))
for c in stats:
    print (c)
    results.write(c[0] + c[1])