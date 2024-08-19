import random
import itertools

# Sample text input for the "training" phase
text = """
Artificial intelligence and machine learning are fields of study that are growing rapidly. 
The possibilities are endless, and the impact on the future is immense.
Artificial intelligence is reshaping the way we think, work, and live.
"""

# Tokenization: splitting the text into words
words = text.split()

# Build a trigram frequency dictionary (triplets of words)
trigrams = {}

for i in range(len(words) - 2):
    word_triplet = (words[i], words[i + 1], words[i + 2])
    if word_triplet in trigrams:
        trigrams[word_triplet] += 1
    else:
        trigrams[word_triplet] = 1

# Generate a sentence based on the trigrams
def generate_sentence(start_word, length=10):
    # Find all trigrams that start with the given word
    candidate_trigrams = [triplet for triplet in trigrams if triplet[0] == start_word]

    if not candidate_trigrams:
        return f"No possible sentence starting with '{start_word}'"

    current_triplet = random.choices(candidate_trigrams, weights=[trigrams[t] for t in candidate_trigrams])[0]
    sentence = list(current_triplet[:2])  # Start the sentence with the first two words of the chosen trigram

    for _ in range(length - 2):
        next_word_candidates = [(triplet[2], trigrams[triplet]) for triplet in trigrams if triplet[:2] == tuple(sentence[-2:])]
        
        if not next_word_candidates:
            break
        
        # Weighted random selection of the next word based on frequency
        next_word = random.choices(
            [word for word, _ in next_word_candidates],
            weights=[weight for _, weight in next_word_candidates]
        )[0]
        
        sentence.append(next_word)
    
    return ' '.join(sentence)

# Get user input for the starting word and sentence length
start_word = input("Enter a starting word: ")
sentence_length = int(input("Enter the length of the sentence (number of words): "))

# Check if the start word is in the list of words
if start_word not in words:
    print(f"'{start_word}' not found in text, choosing a random word.")
    start_word = random.choice(words)

# Generate and print the sentence
generated_sentence = generate_sentence(start_word, length=sentence_length)
print("Generated sentence:", generated_sentence)
