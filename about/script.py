print("Enter the csv file location for the following designations")

try:
    AdNum=int(input("Enter the number of files for Advisors: "))
    Advisor=[]
    Advisorfile=[]
    for i in range(AdNum):
        Advisor.append(input("Advisors: "))
        Advisorfile.append(open(Advisor[i],"r"))
    Executive=input("Executives: ")
    Executivefile=open(Executive,"r")
    CTM=input("CTMs: ")
    CTMfile=open(CTM,"r")
except:
    print("Incorrect file location. Try again.")

objectjs=open("team_list.js","w")

objectjs.write("Advisors=[")
for i in range(AdNum):
    allText=Advisorfile[i].read()
    allLines=allText.split('\n')
    obj=[]
    for line in allLines:
        obj.append(line.split(","))
    for j in range(1,len(obj)-1):
        if(('/' in obj[j][5])):
            obj[j][5]=obj[j][5].split('/')[1]
        if((',' in obj[j][5])):
            obj[j][5]=obj[j][5].split(',')[1]
        obj[j][5]=obj[j][5].strip().strip('"')
        objectjs.write("['"+obj[j][0]+"','"+obj[j][5]+"']")
        if(j!=(len(obj)-2)):
            objectjs.write(",")
    if(i!=AdNum-1):
        objectjs.write(",")
objectjs.write("]\n")
    

objectjs.write("Executives=[")
allText=Executivefile.read()
allLines=allText.split('\n')
obj=[]
for line in allLines:
    obj.append(line.split(","))
for i in range(1,len(obj)-1):
    if(('/' in obj[i][5])):
        obj[i][5]=obj[i][5].split('/')[1]
    if((',' in obj[i][5])):
        obj[i][5]=obj[i][5].split(',')[1]
    obj[i][5]=obj[i][5].strip().strip('"')
    objectjs.write("['"+obj[i][0]+"','"+obj[i][5]+"']")
    if(i!=(len(obj)-2)):
        objectjs.write(",")
objectjs.write("]\n")

objectjs.write("CTMs=[")
allText=CTMfile.read()
allLines=allText.split('\n')
obj=[]
for line in allLines:
    obj.append(line.split(","))
for i in range(1,len(obj)-1):
    if(('/' in obj[i][5])):
        obj[i][5]=obj[i][5].split('/')[1]
    if((',' in obj[i][5])):
        obj[i][5]=obj[i][5].split(',')[1]
    obj[i][5]=obj[i][5].strip().strip('"')
    objectjs.write("['"+obj[i][0]+"','"+obj[i][5]+"']")
    if(i!=(len(obj)-2)):
        objectjs.write(",")
objectjs.write("]\n")