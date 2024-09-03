# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)

def count_words(sentences):
    total_words = 0
    for sentence in sentences:
        words = sentence.split(" ")
        total_words += len(words)
    return total_words

def frequent_word(sentences):
    from collections import Counter

    words_frequency = Counter()
    for sentence in sentences:
        words = sentence.split()
        words_frequency.update(word.lower() for word in words)

    most_frequent = words_frequency.most_common(1)[0] #(1) är till för att hitta det MEST vanliga ordet och [0] är till för att ge listan ett start nummer
    return most_frequent

def average_word_length(sentences):
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    
    if not words: #bara för att undvika division med 0 utifall att filen är tom
        return 0
    
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length

def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.
    
    print(count_words(sentences))
    
    most_frequent = frequent_word(sentences)
    print(most_frequent[0], most_frequent[1]) #printar både ordet och antalet 
    
    print(average_word_length(sentences))

if __name__ == "__main__":
    main()

#output fel: ger 438 istället för korrekt svar 432, vet inte varför.