

def isGood(text):
    
    vowels = "а,я,у,ю,о,е,ё,э,и,ы "
    
    vowelsCount = None

    for word in text.lower().split():

        vowelsInWord = map(lambda x : 1 if (x in vowels) else 0, word)        
        vowelsInWord = sum(list(vowelsInWord))

        if vowelsCount == None:
            vowelsCount = vowelsInWord
        elif vowelsCount != vowelsInWord:
            return False

    return True


text = input("Введите текст стихотворения: ")

if isGood(text):
    print("Парам пам-пам")
else:
    print("Пам парам")


def print_operation_table(operation, num_rows6=6, num_columns=6):
    for row in range(1, num_rows6+1):
        print_line = ""
        for column in range(1, num_columns+1):
            print_line += " "+str(operation(row, column))
        print(print_line)


print_operation_table(lambda x,y: x*y)