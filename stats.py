
def num_words(text):
    return len(text.split()) 

def count_characters(text):
    
    text = text.lower()  # Normalize text to lowercase
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    sorted_char = dict(sorted(char_counts.items(), key=lambda char:char[1], reverse=True))
    return sorted_char
