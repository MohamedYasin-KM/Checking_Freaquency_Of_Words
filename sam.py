#Importing sys module
import sys

class Counting_Frequency:
    '''reading_words fuction is used to read the content line by line and from
        line it extract word and added to the list'''
    def reading_words(file):
        with  open(file,"r") as file:
            for line in file:
                for word in line.split():
                    words.append(word.lower())
            return words

    '''counting_words function is used to read the freaquency of words occured'''
    def counting_words():
        col = Counting_Frequency.reading_words(sys.argv[1])
        for word in col:
            var = word.strip(",").strip(".")
            if var not in frequency:
                frequency[var] = count
            else:
                frequency[var] += 1
        return frequency,len(frequency)

    '''formatting function is used to format the word'''
    def formatting():
        user_input = input("Enter the word : ")
        user_input.lower()
        words,value = Counting_Frequency.counting_words()
        for word,count in words.items():
            value = value-1
            if user_input==word:
                print(f"{user_input} has occured {count} times")
                break
            elif user_input=="*":
                for word,count in words.items():
                    print(f"{word} has occured {count} times")
            else:
                if value==0:
                    print(f"{user_input} has not occured")
words = []
frequency = {}
count = 1

func = Counting_Frequency
func.formatting()
