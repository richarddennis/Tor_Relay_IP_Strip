file_to_write = open("test.json","rw") 
file_to_open = open("ip.txt","rw") 

with open(file_to_open ) as f:
    content = f.readlines()
    print content
    print "1"
