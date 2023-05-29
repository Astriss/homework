class Table:
    def __init__(self,lines,columns):
        self.lines = lines
        self.columns = columns
        self.matrix = []
        for i in range(lines):
            self.matrix.append([])
            for k in range(columns):
                self.matrix[i].append(k)
    def __str__(self):
        return f'{self.matrix}'
    
    def set_new(self,line,column,obj):
        self.line = int(line)
        self.column = int(column)
        self.obj = obj
        self.matrix[line][column] = obj

    def add(self,line,obj):
        self.line = int(line)
        self.obj = obj
        self.matrix[line].append(obj)
        self.columns = self.columns+1

    def inspect(self):
        print(f'Число строк: {self.lines}')
        print(f'Число колонок: {self.columns}')




m = Table(10,10)
print(f'Исходная таблица: {m}')
m.set_new(0,0,9)
print(f'Таблица с изменённым значением: {m}')
m.add(0,88)
print(f'Таблица с новым элементом: {m}')
m.inspect()




