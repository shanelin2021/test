# This is an interactive problem. You need to find the secret word with limited guesses.
# Problem: Guess the word from a list using Master.guess() feedback

class Master:
    """Helper object for the word guessing game"""
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.guess_count = 0
    
    def guess(self, word):
        """Returns the number of exact matches (same char, same position)"""
        self.guess_count += 1
        if word == self.secret_word:
            return len(word)  # All matches
        matches = sum(1 for i in range(len(word)) if word[i] == self.secret_word[i])
        return matches


def findSecretWord(words, master):
    """
    Find the secret word using Master.guess()
    
    Strategy:
    1. Start with a random word from the list
    2. Get the match count
    3. Filter the remaining words based on match count
    4. Repeat until we find the secret word
    """
    
    def get_matches(word1, word2):
        """Calculate number of exact matches between two words"""
        return sum(1 for i in range(len(word1)) if word1[i] == word2[i])
    
    # Start with words list
    candidates = words.copy()
    
    while len(candidates) > 0:
        # Pick the first candidate as our guess
        guess = candidates[0]
        
        # Get feedback from master
        matches = master.guess(guess)
        
        # If we got all matches, we found it!
        if matches == len(guess):
            return guess
        
        # Filter candidates based on match count
        # Only keep words that would give the same match count with our guess
        candidates = [word for word in candidates if get_matches(guess, word) == matches]
    
    return None


# Test function
def test_find_secret_word():
    # Test case 1
    print("Test Case 1:")
    secret1 = "acckzz"
    words1 = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    master1 = Master(secret1)
    
    result1 = findSecretWord(words1, master1)
    print(f"Secret word: {secret1}")
    print(f"Found: {result1}")
    print(f"Guess count: {master1.guess_count}")
    print()
    
    # Test case 2
    print("Test Case 2:")
    secret2 = "hamada"
    words2 = ["hamada", "khaled"]
    master2 = Master(secret2)
    
    result2 = findSecretWord(words2, master2)
    print(f"Secret word: {secret2}")
    print(f"Found: {result2}")
    print(f"Guess count: {master2.guess_count}")
    print()
    
    # Test case 3 - More challenging
    print("Test Case 3:")
    secret3 = "abcdef"
    words3 = ["abcdef", "fedcba", "bcdefa", "abcxyz", "xydefz"]
    master3 = Master(secret3)
    
    result3 = findSecretWord(words3, master3)
    print(f"Secret word: {secret3}")
    print(f"Found: {result3}")
    print(f"Guess count: {master3.guess_count}")


if __name__ == "__main__":
    test_find_secret_word()


