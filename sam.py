words = []
frequency = {}
count = 1

def reading_words(file):
    with  open(file,"r") as file:
        for line in file:
            for word in line.split():
                words.append(word.lower())
        return words

def counting_words():
    col = reading_words("story.txt")
    for word in col:
        var = word.strip(",").strip(".")
        if var not in frequency:
            frequency[var] = count
        else:
            frequency[var] += 1
    print(frequency,end="\n")
counting_words()
