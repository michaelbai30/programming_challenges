import sys
import collections

def shortestCompletingWord(licensePlate, words):
    # result is guaranteed to be less than 16 characters (from Leetcode equivalent)
    res = "?" * 16

    freqLicensePlateChars = collections.defaultdict(int)
    freqWord = collections.defaultdict(int)

    # construct a frequency dictionary for the alphabetic license plate chars
    for char in licensePlate:
        if char.isalpha():
            freqLicensePlateChars[char.lower()] += 1

    # for each word, construct a frequency dictionary
    for word in words:        
        validCompletingWord = True
        for char in word:
            freqWord[char.lower()] += 1

        # if there are more occurences of some letter in the license plate 
        # than in the word, it cannot be a valid completing word
        for key in freqLicensePlateChars:
            if freqLicensePlateChars[key] > freqWord[key]:
                validCompletingWord = False
                break

        if len(word) < len(res) and validCompletingWord:
            res = word
    
        freqWord.clear()
    return res

def main():

    licensePlates = []
    words = []

    for line in sys.stdin:

        elements = line.strip().split(',')
        licensePlates.append(elements[0])
        words.append(elements[1:])

    for count, licensePlate in enumerate(licensePlates):
        print(f'{count + 1}. {shortestCompletingWord(licensePlate, words[count])}')

if __name__ == '__main__':
    main()
