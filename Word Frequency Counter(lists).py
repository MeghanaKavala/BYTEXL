from collections import Counter

def word_frequency(file_path, N):
    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert text to lowercase
    
    # Remove punctuation and split text into words
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top N most common words
    top_N_words = word_counts.most_common(N)
    
    # Display the top N most common words
    print(f"Top {N} most frequently occurring words:")
    for word, count in top_N_words:
        print(f"{word}: {count}")

# Example usage:
file_path = 'sample.txt'  # Path to the text file
N = 10  # Number of top words to display
word_frequency(file_path, N)
