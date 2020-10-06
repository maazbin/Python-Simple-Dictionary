

def main():
    exit_program =""
    while exit_program != '-':
        word=input("Enter a string : ")
        dictionary = "./dictionary.txt" #dictionary in same directory
        load(dictionary)
        for i in word.split():
            if check(i)!=True:
                print(f"{i} is not a word")
            else:
                print(f"'{i}' is  a word")    
        exit_program=input("Press Minus '-' to exit or any kkey to contineue : ")


words = set()

def check(word):
    return word.lower() in words
        # return True

def load(dictionary):
    with open(dictionary,encoding = "ISO-8859-1") as file:
        for line in file:
            # print(line)
            words.add(line.rstrip("\n"))

# def size():
    # return len(words)

# def unload():


main()    
