#file_to_write = open("test.json","rw+") 
#file_to_open = open("IPs.txt","r") 

with open("IPs.txt","r") as f, open("Json_IPs.json", "w+") as w:
	for line in f:
		print line
		w.write("{ 'ip':'")
		w.write(line.rstrip())
		w.write("' }")
		w.write("\n")
