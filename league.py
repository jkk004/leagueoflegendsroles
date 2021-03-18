import requests
import re

n = 20 #how many pages? each page has about 100 players but grandmaster players generally go up to page 9. After that its only Master tier players
names = [] #names of all the top players will be put in this list
statistics = {"Top" : 0, "Middle": 0, "Jungle": 0, "ADC": 0, "Support": 0, "Stop Playing ARAM You Wimp": 0}

link = "https://na.op.gg/ranking/ladder/page="
for i in range(1,n + 1):
    temp = link + str(i)
    f = requests.get(temp)
    res = [m.start() for m in re.finditer('userName', f.text)]
    for j in range(1,len(res)):
        tally = 0
        word = ""
        check = 9
        while tally == 0:
            if f.text[res[j]+check] == '"':
                tally = 1
                break
            word += f.text[res[j]+check]
            check += 1
        names.append(word)
del names[1]
del names[3]
del names[5]
del names[1]
del names[5]
print(names)
#positionName

for k in range(len(names)):
    n = 0
    while n == 0:
        word = ""
        tally = 0
        link = "https://na.op.gg/summoner/userName="
        f = requests.get(link + str(names[k]))
        res = [m.start() for m in re.finditer('"positionName"', f.text)]
        if len(res) == 0:
            statistics["Stop Playing ARAM You Wimp"] += 1
            break

        check = res[0] + 16
        while tally == 0:
            if f.text[check] == '"':
                tally = 1
                break
            word += str(f.text[check])
            check += 1
        statistics[word] += 1
        print(statistics)
        n= 1

print("\n")
print(names)
print(statistics)
