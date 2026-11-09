
FILE_NAME = 'text.txt'
PUNCTUATION = '.,;:!?"()'
 
 
def main():
    words = []
 
    try:
        # Read the file one line at a time
        input_file = open(FILE_NAME, 'r')
 
        for line in input_file:
            # Split the line into words, then remove the punctuation
            # at both ends of each word and change it to lowercase
            for word in line.split():
                word = word.strip(PUNCTUATION).lower()
                if word != '':
                    words.append(word)
 
        input_file.close()
    except IOError:
        print('Error: could not read the file', FILE_NAME)
        return
 
    # Filter out the duplicate words with a set
    unique_words = set(words)
 
    # Create the dictionary with every unique word and a count of 0
    word_counts = {}
    for word in unique_words:
        word_counts[word] = 0
 
    # Count the occurrences of each word
    for word in words:
        word_counts[word] += 1
 
    # Display the words in alphabetical order with their counts
    sorted_words = list(word_counts.keys())
    sorted_words.sort()
 
    print('Word Counts')
    print('-----------')
    for word in sorted_words:
        print(word, ':', word_counts[word])
 
    print('\nTotal words:', len(words))
    print('Unique words:', len(word_counts))
 
 
# Call the main function
main()