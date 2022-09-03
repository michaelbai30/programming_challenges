import sys
import collections

def shortest_completing_word(license_plate, words):
    # result is guaranteed to be less than 16 characters (from Leetcode equivalent)
    res = "?" * 16

    freq_license_plate_chars = collections.defaultdict(int)
    freq_word = collections.defaultdict(int)

    # construct a frequency dictionary for the alphabetic license plate chars
    for char in license_plate:
        if char.isalpha():
            freq_license_plate_chars[char.lower()] += 1

    # for each word, construct a frequency dictionary
    for word in words:        
        valid_completing_word = True
        for char in word:
            freq_word[char.lower()] += 1

        # if there are more occurences of some letter in the license plate 
        # than in the word, it cannot be a valid completing word
        for key in freq_license_plate_chars:
            if freq_license_plate_chars[key] > freq_word[key]:
                valid_completing_word = False
                break

        if len(word) < len(res) and valid_completing_word:
            res = word
    
        freq_word.clear()
    return res

def main():
    license_plates = []
    words = []

    for line in sys.stdin:
        elements = line.strip().split(',')
        license_plates.append(elements[0])
        words.append(elements[1:])

    for count, license_plate in enumerate(license_plates):
        print(f'{count + 1}. {shortest_completing_word(license_plate, words[count])}')

if __name__ == '__main__':
    main()
