def CheckPalindrom(string): #создвал саму функцию, принимающая параметр "string"
    if string[::-1] == string: #приверка на палиндром, "string[::-1] == string[0:0:-1] - эта фича переворачивает строку"
        return True
    return False
print(CheckPalindrom(input())) #ввод данных, вызов функции, вывод результата 