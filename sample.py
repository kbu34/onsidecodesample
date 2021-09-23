"""
Converts basic numbers to words.
"""
def numberToWord(num):
    if num == '1':
        return 'one'
    elif num == '2':
        return 'two'
    elif num == '3':
        return 'three'
    elif num == '4':
        return 'four'
    elif num == '5':
        return 'five'
    elif num == '6':
        return 'six'
    elif num == '7':
        return 'seven'
    elif num == '8':
        return 'eight'
    elif num == '9':
        return 'nine'
    elif num == '0':
        return ''

"""
Converts numbers in tens digits to words.
"""
def tenNumberToWord(num):
    if num == '2':
        return 'twenty'
    elif num == '3':
        return 'thirty'
    elif num == '4':
        return 'forty'
    elif num == '5':
        return 'fifty'
    elif num == '6':
        return 'sixty'
    elif num == '7':
        return 'seventy'
    elif num == '8':
        return 'eighty'
    elif num == '9':
        return 'ninety'

"""
Converts numbers from 11 to 19 to words.
"""
def oneTenNumberToWord(num):
    if num == '1':
        return 'eleven'
    elif num == '2':
        return 'twelve'
    elif num == '3':
        return 'thirteen'
    elif num == '4':
        return 'fourteen'
    elif num == '5':
        return 'fifteen'
    elif num == '6':
        return 'sixteen'
    elif num == '7':
        return 'seventeen'
    elif num == '8':
        return 'eighteen'
    elif num == '9':
        return 'nineteen'
    elif num == '0':
        return 'ten'

"""
Converts money to words.
"""       
def convertNumToWord(number):
    money = number.split(".")
    if len(money) != 2:
        raise Exception("Incorrect format")
    number, cent = money
    try:
        int(number)
        int(cent)
    except:
        raise Exception("Input is not a number")
    if len(cent) > 2:
        raise Exception("Incorrect format")

    numReverse = number[::-1]
    n = 3
    numListReverse = [numReverse[i:i+n] for i in range(0, len(number), n)]
    numList = []
    for num in numListReverse:
        numList.append(num[::-1])
    numList.reverse()
    result = ""

    thousands = len(numList)
    if thousands > 4 or (thousands == 4 and int(numList[0]) > 100):
        raise Exception("Value too high")
    for num in numList:
        numString = ""
        thousand = ""
        hundred = ""
        ten = ""
        one = ""
        if len(num) == 3:
            hundred = numberToWord(num[0]) + " hundred and "
            if num[1] != '1':
                ten = tenNumberToWord(num[1]) + " "
                one = numberToWord(num[2])
            else:
                one = oneTenNumberToWord(num[2])
        if len(num) == 2:
            if num[0] != '1':
                ten = tenNumberToWord(num[0]) + " "
                one = numberToWord(num[1])
            else:
                one = oneTenNumberToWord(num[1])
        if len(num) == 1:
            one = numberToWord(num[0])
        if thousands == 4:
            thousand = " billion"
        elif thousands == 3:
            thousand = " million"
        elif thousands == 2:
            thousand = " thousand"
        thousands -= 1
        numString = hundred + ten + one + thousand + " "
        result += numString
    if result != " ":
        result += "dollars and "

    ten = ""
    one = ""
    if cent[0] != '1':
        if cent[0] != '0':
            ten = tenNumberToWord(cent[0])
        one = numberToWord(cent[1])
    elif cent[0] == '1':
        one = oneTenNumberToWord(cent[1])
    if ten != "" or one != "":
        result += ten + one + " cents"
    return result

"""
Converts basic words to numbers.
"""
def wordToNumber(word):
    if word == 'one':
        return '1'
    elif word == 'two':
        return '2'
    elif word == 'three':
        return '3'
    elif word == 'four':
        return '4'
    elif word == 'five':
        return '5'
    elif word == 'six':
        return '6'
    elif word == 'seven':
        return '7'
    elif word == 'eight':
        return '8'
    elif word == 'nine':
        return '9'
    else:
        return None

"""
Converts words in tens digits to numbers
"""
def tenWordToNumber(word):
    if word == 'ten':
        return '1'
    elif word == 'twenty':
        return '2'
    elif word == 'thirty':
        return '3'
    elif word == 'forty':
        return '4'
    elif word == 'fifty':
        return '5'
    elif word == 'sixty':
        return '6'
    elif word == 'seventy':
        return '7'
    elif word == 'eighty':
        return '8'
    elif word == 'ninety':
        return '9'
    else:
        return None

"""
Converts words from eleven to nineteen to numbers.
"""
def oneTenWordToNumber(word):
    if word == 'eleven':
        return '11'
    elif word == 'twelve':
        return '12'
    elif word == 'thirteen':
        return '13'
    elif word == 'fourteen':
        return '14'
    elif word == 'fifteen':
        return '15'
    elif word == 'sixteen':
        return '16'
    elif word == 'seventeen':
        return '17'
    elif word == 'eighteen':
        return '18'
    elif word == 'nineteen':
        return '19'
    else:
        return None

"""
Converts words to number.
"""
def convertWordtoNum(words):
    number = ""
    wordList = list(words.split(" "))
    for word in wordList:
        if word != "and" and word != "dollars" and word != "cents" and word != "billion" and word != "million" and word != "thousand" and word != "hundred" and wordToNumber(word) == None and tenWordToNumber(word) == None and oneTenWordToNumber(word) == None:
            raise Exception("Unexpected Input: " + word)
    billions = ""
    millions = ""
    thousands = ""
    hundreds = ""
    try:
        billion = wordList.index("billion")
    except:
        billion = None
    try:
        million = wordList.index("million")
    except:
        million = None
    try:
        thousand = wordList.index("thousand")
    except:
        thousand = None
    try:
        hundred = wordList.index("dollars")
    except:
        hundred = None
    
    i = 0
    if billion != None:
        while i < billion:
            if wordToNumber(wordList[i]) != None:
                billions += wordToNumber(wordList[i])
                if wordList[i+1] == "hundred" and wordList[i+2] == "billion":
                    billions += "00"
            elif tenWordToNumber(wordList[i]) != None:
                billions += tenWordToNumber(wordList[i])
                if wordList[i+1] == "billion":
                    billions += "0"
            elif oneTenWordToNumber(wordList[i]) != None:
                if i > 0 and wordList[i-1] != "hundred":
                    billions += "0" + oneTenWordToNumber(wordList[i])
                else:
                    billions += oneTenWordToNumber(wordList[i])
            elif wordList[i] == "hundred" and wordToNumber(wordList[i+1]) != None:
                billions += "0"
            i += 1
    if million != None:
        while i < million:
            if wordToNumber(wordList[i]) != None:
                if wordList[i+1] == "hundred" and wordList[i+2] == "million":
                    millions += "00"
                elif i > 0 and tenWordToNumber(wordList[i-1]) == None and wordList[i-1] != "billion" and wordList[i-1] != "and":
                    millions += "00" + wordToNumber(wordList[i])
                else:
                    millions += wordToNumber(wordList[i])
            elif tenWordToNumber(wordList[i]) != None:
                millions += tenWordToNumber(wordList[i])
                if wordList[i+1] == "million":
                    millions += "0"
            elif oneTenWordToNumber(wordList[i]) != None:
                if i > 0 and wordList[i-1] != "hundred":
                    millions += "0" + oneTenWordToNumber(wordList[i])
                else:
                    millions += oneTenWordToNumber(wordList[i])
            elif wordList[i] == "hundred" and wordToNumber(wordList[i+1]) != None:
                millions += "0"
            i += 1
    else:
        millions = "000"
    if thousand != None:
        while i < thousand:
            if wordToNumber(wordList[i]) != None:
                if wordList[i+1] == "hundred" and wordList[i+2] == "thousand":
                    thousands += "00"
                elif i > 0 and tenWordToNumber(wordList[i-1]) == None and wordList[i-1] != "million" and wordList[i-1] != "and":
                    thousands += "00" + wordToNumber(wordList[i])
                else:
                    thousands += wordToNumber(wordList[i])
            elif tenWordToNumber(wordList[i]) != None:
                thousands += tenWordToNumber(wordList[i])
                if wordList[i+1] == "thousand":
                    thousands += "0"
            elif oneTenWordToNumber(wordList[i]) != None:
                if i > 0 and wordList[i-1] != "hundred":
                    thousands += "0" + oneTenWordToNumber(wordList[i])
                else:
                    thousands += oneTenWordToNumber(wordList[i])
            elif wordList[i] == "hundred" and wordToNumber(wordList[i+1]) != None:
                thousands += "0"
            i += 1
    else:
        thousands = "000"
    if wordList[i+1] != "dollars" or (billion == None and million == None and thousand == None):
        while i < hundred:
            if wordToNumber(wordList[i]) != None:
                if wordList[i+1] == "hundred" and wordList[i+2] == "dollars":
                    hundreds += wordToNumber(wordList[i]) + "00"
                elif i > 0 and tenWordToNumber(wordList[i-1]) == None and wordList[i-1] != "thousands" and wordList[i-1] != "and":
                    hundreds += "00" + wordToNumber(wordList[i])
                else:
                    hundreds += wordToNumber(wordList[i])
            elif tenWordToNumber(wordList[i]) != None:
                hundreds += tenWordToNumber(wordList[i])
                if wordList[i+1] == "dollars":
                    hundreds += "0"
            elif oneTenWordToNumber(wordList[i]) != None:
                if i > 0 and wordList[i-1] != "hundred":
                    hundreds += "0" + oneTenWordToNumber(wordList[i])
                else:
                    hundreds += oneTenWordToNumber(wordList[i])
            elif wordList[i] == "hundred" and wordToNumber(wordList[i+1]) != None:
                thousands += "0"
            i += 1
    else:
        i += 1
        hundreds = "000"
    number = str(int(billions + millions + thousands + hundreds))
    if int(number) > 100000000000:
        raise Exception("The value is too high.")
    cents = ""
    while i < len(wordList):
        if wordList[i] == "hundred" or wordList[i] == "thousand" or wordList[i] == "million" or wordList[i] == "billion":
            raise Exception("Invalid value in cents.")
        if wordToNumber(wordList[i]) != None:
            cents += "0" + wordToNumber(wordList[i])
        elif tenWordToNumber(wordList[i]) != None:
            cents += tenWordToNumber(wordList[i])
            if wordList[i+1] == "cents":
                cents += "0"
        elif oneTenWordToNumber(wordList[i]) != None:
                cents += oneTenWordToNumber(wordList[i])
        i += 1
    if cents == "":
        cents = "00"
    number += "." + cents
    return number

"""
The main function that runs the program.
"""
def main():
    choice = None
    while choice == None:
        numChoice = input("Press 1 for number to word, press 2 for word to number\n")
        if numChoice == "1":
            choice = 1
        elif numChoice == "2":
            choice = 2
    if choice == 1:
        inputNum = input("Enter the number\n")
        output = convertNumToWord(inputNum)
        print("Your output is " + output)
    elif choice == 2:
        inputWord = input("Enter the words, including 'dollars' and 'cents'\n")
        output = convertWordtoNum(inputWord)
        print("Your output is " + output)
main()