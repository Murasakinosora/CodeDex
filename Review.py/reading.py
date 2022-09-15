#reading a file
reader = open("D:\Codedex\CodeDex\Review.py\samplefile.txt","r")
# writing = w, reading and writing = r+, appending = a
#reader.readable() checks if a file is readable
#to read whole file: print(reader.read())
#to read the per line: print(reader.readline())
# to put them in an array per line use
print(reader.readlines())
reader.close