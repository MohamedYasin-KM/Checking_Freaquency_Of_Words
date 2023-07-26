#Importing sys module
import sys

class Counting_Frequency:
    '''reading_words fuction is used to read the content line by line and from
        line it extract word and added to the list'''
    def reading_words(file):
        #Opening the file
        with  open(file,"r") as file:
            for line in file:
                for word in line.split():
                    words.append(word.lower())
            return words

    '''counting_words function is used to read the freaquency of words occured'''
    def counting_words():
        #File name taken from command line
        words = Counting_Frequency.reading_words(sys.argv[1])
        for word in words:
            word = word.strip(",").strip(".")
            if word not in frequency:
                frequency[word] = count
            else:
                frequency[word] += 1
        return frequency,len(frequency)

    '''formatting function is used to format the word'''
    def formatting():
        #Reading input from user
        user_input = input("Enter the word : ")
        words,value = Counting_Frequency.counting_words()
        #Formatting all the keys and values in the dictionary
        for word,count in words.items():
            #Decreasing value for printing else statement if the key and value is not there
            value = value-1
            if user_input.lower()=='q':
                sys.exit()
            #This statement print if the user_input matches the given word
            elif user_input.lower()==word:
                print(f"{user_input.lower()} has occured {count} times")
                break
            #This statement format all keys and values
            elif user_input=="*":
                for word,count in words.items():
                    print(f"{word} has occured {count} times")
            #This statement print if the key and value are not there
            else:
                if value==0:
                    print(f"{user_input} has not occured")

words = []
frequency = {}
count = 1

#Initializing the object
while True:
    func = Counting_Frequency
    func.formatting()
    print("--------------------")
    print("Press q to exit")
