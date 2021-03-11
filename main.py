print("Введите путь и/или имя файла:")

path = input()

checkFirstDate = True
checkName = False

f = open(path, 'r')

f.readline()

f2 = open("result.csv", 'w')
f2.write("Name / Date,")
f2.close()

for line in f:
    name = line.split(',')[0]
    date = line.split(',')[1]
    time = line.split(',')[2]
    time = time.split('\n')[0]
    
    f2 = open("result.csv", 'r')

    #ищем дату
    firstLine = f2.readline()
    firstLine = firstLine.split('\n')[0]
    if firstLine.find(date) == -1:
        nextLines = f2.read()
        f2.close()

        f2 = open("result.csv", 'w')
        f2.write(firstLine + date + ",\n" + nextLines)
        f2.close()

        if checkFirstDate == False:
            f2 = open("result.csv", 'r')
            firstLine = f2.readline()
            firstLine = firstLine.split('\n')[0]
            nextLines = f2.read()
            f2.close()
            f2 = open("result.csv", 'w')
            f2.write(nextLines)
            f2.close()

            f2 = open("result.csv", 'r')

            for line in f2.readlines():
                
                firstPart = nextLines.split(line)[0]
                f2.seek(0)
                secondPart = nextLines.split(line)[1] 
                
                line = line.split('\n')[0]
                
                nextLines = firstPart + line + '0,\n' + secondPart
 

            f2 = open("result.csv", 'w')
            f2.write(firstLine + '\n' + nextLines)
            f2.close()
        else:
            checkFirstDate = False
    
    #ищем имя 
    f2 = open("result.csv", 'r')
    for line in f2:
        if line.find(name) != -1:
            checkName = True
            
            f2.seek(0)
            firstPart = f2.read().split(line)[0]
            f2.seek(0)
            secondPart = f2.read().split(line)[1] 
            f2.close()

            line = line.split('\n')[0]
            if line.find('0,') != -1:
                line = line[:-2]
 

            f2 = open("result.csv", 'w')
            f2.write(firstPart + line + time + ',' + '\n' +  secondPart)
            f2.close()
            break

    

    
    if checkName == False:
        f2 = open("result.csv", 'a')
        f2.write(name + ',' + time + ',\n')
        f2.close()
    
   
   """  f2 = open("result.csv", 'r')
    print(f2.read())
    f2.close()
    input() """
    
f.close()
print('Результат сохранен в файле "result.csv".\n Нажмите ENTER для завершения.')
input()

    


    


