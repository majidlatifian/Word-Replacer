from collections import OrderedDict

def replace_words_with_definitions():
    n = int(input("Enter the number of word-definition pairs: "))
    d = OrderedDict()

    for i in range(n):
        word, definition = input("Enter a word and its definition (separated by a space): ").split()
        d[word] = definition

    sentence = input("Enter a sentence: ")
    words = sentence.split()
    replaced_sentence = []

    for word in words:
        replaced_sentence.append(d.get(word, word))

    print("Replaced sentence:", " ".join(replaced_sentence))

if __name__ == '__main__':
    replace_words_with_definitions()
