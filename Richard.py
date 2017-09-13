import requests

url = "http://86.59.21.38/tor/status-vote/current/consensus.txt"
data = requests.get(url).text
L = data.split("\n")
LineR = []
for line in L:
    ListLine = line.split(" ")
    if ListLine[0] == "r":
        LineR.append(ListLine[-3]+"\n")
    elif ListLine[0] == "dir-source" and ListLine[-4].split(".")[0].isalpha() == False:
        LineR.append(ListLine[-3] + "\n")
        LineR.append(ListLine[-4] + "\n")

readfile = open("ListIPs.txt","r")
IPExist = []
IPNoExist = []
for line in readfile:
    if line in LineR:
        IPExist.append(line)
    else:
        IPNoExist.append(line)
readfile.close()

Newfile = open("AllIPs.txt","w")
Newfile.writelines(LineR)
Newfile.close()

Newfile = open("ExistIPs.txt","w")
Newfile.writelines(IPExist)
Newfile.close()

Newfile = open("NoExistIPs.txt","w")
Newfile.writelines(IPNoExist)
Newfile.close()