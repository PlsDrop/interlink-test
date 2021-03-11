#да простят меня боги за этот ужаснейший код 
#код рассчитан на базу в которой все отсортированно по дате(как в вашем примере который я получил), иначе все сломаеться


print("Введите полный или относительный путь к файлу:")

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

f.close()

#сортируем по имени
listOfLines = []
f2 = open("result.csv", 'r')
firstLine = f2.readline()
for line in f2.readlines():
    listOfLines.append(line)

listOfLines.sort()
f2.close()

f2 = open("result.csv", 'w')
f2.write(firstLine)
for element in listOfLines:
    f2.write(element)
f2.close()

#меняем тип даты
f2 = open("result.csv", 'r')
firstLine = f2.readline()
nextLines = f2.read()
listOfDates = firstLine.split(',')

firstLine = listOfDates[0]
i = 0 
while i<len(listOfDates)-2:
    i+=1
    lOfDate = listOfDates[i].split(' ')
    lOfDate[0] = lOfDate[0].replace('Jan', '01')
    lOfDate[0] = lOfDate[0].replace('Feb', '02')
    lOfDate[0] = lOfDate[0].replace('Mar', '03')
    lOfDate[0] = lOfDate[0].replace('Apr', '04')
    lOfDate[0] = lOfDate[0].replace('May', '05')
    lOfDate[0] = lOfDate[0].replace('Jun', '06')
    lOfDate[0] = lOfDate[0].replace('Jul', '07')
    lOfDate[0] = lOfDate[0].replace('Aug', '08')
    lOfDate[0] = lOfDate[0].replace('Sep', '09')
    lOfDate[0] = lOfDate[0].replace('Oct', '10')
    lOfDate[0] = lOfDate[0].replace('Nov', '11')
    lOfDate[0] = lOfDate[0].replace('Dec', '12')
    date = str(lOfDate[2] + '-' + lOfDate[0] + '-' + lOfDate[1])
    firstLine = firstLine + ',' + date
    print(firstLine)
f2.close()

f2 = open("result.csv", 'w')
f2.write(firstLine + '\n' + nextLines)
f2.close()

#выводим результат в консоли
f2 = open("result.csv", 'r')
print(f2.read())
f2.close()

print('Результат сохранен в файле "result.csv".\nНажмите ENTER для завершения.')
input()