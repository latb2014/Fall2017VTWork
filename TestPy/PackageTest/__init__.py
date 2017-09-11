import re
csvFile = open("csvOutput.txt", "w+")
fileTest = open("moanaEx.txt")
count = 0
csvFile.write("Children see throughput for 16 initial writers,Parent sees throughput for 16 initial writers,Min throughput per process,Max throughput per process,Avg throughput per process,Min xfer,Children see throughput for 16 rewriters,Parent sees throughput for 16 rewriters,Min throughput per process,Max throughput per process,Avg throughput per process,Min xfer,\n")
for line in fileTest:
    if "=" in line: 
        count += 1
        if count > 2:
            #re.sub('[\s+]', '', line)
            numbers = line.split("=")
            numbers[1] = numbers[1].strip()
            csvFile.write(numbers[1] + ",")