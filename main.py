print("Введите путь и/или имя файла:")

path = input()

countLines = 0
checkName = False

f = open(path, 'r')

f.readline()

f2 = open("result.csv", 'w')
f2.write("Name / Date,")
f2.close()

for line in f:
    countLines += 1
    name = line.split(',')[0]
    date = line.split(',')[1]
    time = line.split(',')[2]
    time = time.split('\n')[0]
    
    f2 = open("result.csv", '+a')
    f2.seek(0 - f2.tell(), 2)

    #ищем дату
    if f2.readline().find(date) == -1:
        f2.write(date + ",\n")
    
    
    #ищем имя 
    for line in f2:
        if line.find(name) != -1:
            f2.write(time + ',')
            checkName = True
            break
    
    if checkName == False:
        f2.write('\n' + name + ',' + time + ',')
    
    f2.close()
    
    
    
    f2 = open("result.csv", 'r')
    print(f2.read())
    f2.close()
    input()

f.close()


