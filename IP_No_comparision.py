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
file = open("IPs.txt","w")
file.writelines(LineR)
file.close()