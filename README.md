# Word Replacer

The Word Replacer is a Python program that replaces words in a sentence with their corresponding definitions.

## Features
- Allows the user to input word-definition pairs.
- Accepts a sentence as input and replaces words with their definitions.
- Outputs the modified sentence with replaced words.

## Usage
1. Run the program.
2. Enter the number of word-definition pairs.
3. For each pair, enter a word and its definition separated by a space.
4. Once all pairs are entered, the program prompts for a sentence.
5. Enter a sentence.
6. The program replaces words in the sentence with their definitions.
7. The modified sentence is displayed as output.

## Installation
1. Clone the repository or download the source code file.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the source code.
4. Run the following command to execute the program:
```
python app.py

```

## Example

Certainly! Here's the improved code and the corresponding Markdown README:

python
Copy code
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
And here's the corresponding README in Markdown format:

markdown
Copy code
# Word Replacer

The Word Replacer is a Python program that replaces words in a sentence with their corresponding definitions.

## Features
- Allows the user to input word-definition pairs.
- Accepts a sentence as input and replaces words with their definitions.
- Outputs the modified sentence with replaced words.

## Usage
1. Run the program.
2. Enter the number of word-definition pairs.
3. For each pair, enter a word and its definition separated by a space.
4. Once all pairs are entered, the program prompts for a sentence.
5. Enter a sentence.
6. The program replaces words in the sentence with their definitions.
7. The modified sentence is displayed as output.

## Installation
1. Clone the repository or download the source code file.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the source code.
4. Run the following command to execute the program:
python app.py

shell
Copy code

## Example
```
Enter the number of word-definition pairs: 3
Enter a word and its definition: apple fruit
Enter a word and its definition: car vehicle
Enter a word and its definition: house dwelling
Enter a sentence: I have an apple and a car.
Replaced sentence: I have an fruit and a vehicle.
```

