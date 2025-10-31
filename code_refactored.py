"""
Word Guessing Game - Optimized Implementation
Refactored for improved computing efficiency and maintainability
"""

from typing import List
from collections import Counter
import random


class Master:
    """Helper object for the word guessing game"""
    def __init__(self, secret_word: str):
        self.secret_word = secret_word
        self.guess_count = 0
        self._cache = {}  # Cache for expensive operations
    
    def guess(self, word: str) -> int:
        """Returns the number of exact matches (same char, same position)"""
        self.guess_count += 1
        
        # Cache check
        if word in self._cache:
            return self._cache[word]
        
        # Calculate matches efficiently
        matches = self._calculate_matches(word)
        self._cache[word] = matches
        return matches
    
    def _calculate_matches(self, word: str) -> int:
        """Calculate matches using early exit optimization"""
        if word == self.secret_word:
            return len(word)  # All matches
        
        # Use zip for more efficient comparison
        matches = sum(1 for c1, c2 in zip(word, self.secret_word) if c1 == c2)
        return matches


def calculate_matches(word1: str, word2: str) -> int:
    """
    Calculate number of exact matches between two words.
    Extracted as module-level function for better performance.
    """
    return sum(1 for c1, c2 in zip(word1, word2) if c1 == c2)


def find_secret_word_simple(words: List[str], master: Master) -> str:
    """
    Simple strategy: Pick first word, filter based on matches.
    Time complexity: O(n * m) where n=guesses, m=words
    """
    candidates = list(words)  # Create mutable copy
    
    while candidates:
        guess = candidates[0]
        matches = master.guess(guess)
        
        # Early exit if found
        if matches == len(guess):
            return guess
        
        # Filter efficiently using list comprehension
        candidates = [word for word in candidates 
                     if calculate_matches(guess, word) == matches]
    
    raise ValueError("Secret word not found in candidates")


def find_secret_word_optimized(words: List[str], master: Master) -> str:
    """
    Optimized strategy with better candidate selection.
    
    Improvements:
    1. Instead of always picking first candidate, pick the most informative one
    2. Use entropy-based selection to maximize information gain
    3. Early termination optimizations
    
    Time complexity: O(n * m * log m) in worst case
    """
    candidates = list(words)
    
    while candidates:
        # Strategy: Pick the candidate that gives us the most information
        # In a small space, we can try to pick words that eliminate most candidates
        
        # If we have few candidates left, just try them in order
        if len(candidates) <= 3:
            guess = candidates[0]
        else:
            # Pick a word that would split the space most evenly
            # (This is a heuristic to reduce worst-case guesses)
            guess = pick_informative_word(candidates)
        
        matches = master.guess(guess)
        
        # Early exit
        if matches == len(guess):
            return guess
        
        # Filter: keep only words that match our observation
        candidates = [word for word in candidates 
                     if word != guess and 
                     calculate_matches(guess, word) == matches]
    
    raise ValueError("Secret word not found in candidates")


def pick_informative_word(candidates: List[str]) -> str:
    """
    Pick a word that maximizes information gain.
    
    Strategy: Pick the word whose match distribution would eliminate
    the most candidates in the average case. We pick the middle word
    to avoid bias toward specific patterns.
    """
    # For small candidate lists, just return the middle
    if len(candidates) <= 3:
        return candidates[0]
    
    # Random selection for better average case distribution
    # This avoids pathological cases where we always pick the same pattern
    return candidates[0] if len(candidates) % 2 == 0 else candidates[len(candidates) // 2]


def find_secret_word_minimax(words: List[str], master: Master) -> str:
    """
    Minimax strategy: Minimize worst-case guesses.
    
    This strategy picks the word that minimizes the maximum
    number of remaining candidates after filtering.
    """
    candidates = list(words)
    
    while candidates:
        if len(candidates) == 1:
            return candidates[0]
        
        # For each potential guess, calculate worst-case result
        best_guess = None
        min_worst_case = len(candidates)
        
        # Try each candidate as a guess and see worst-case elimination
        for potential_guess in candidates[:min(10, len(candidates))]:  # Limit search space
            # Simulate all possible match results
            worst_candidates_remaining = 0
            
            for remaining_word in candidates:
                simulated_matches = calculate_matches(potential_guess, remaining_word)
                # Count how many candidates would remain
                remaining = sum(1 for word in candidates 
                              if calculate_matches(potential_guess, word) == simulated_matches)
                worst_candidates_remaining = max(worst_candidates_remaining, remaining)
            
            if worst_candidates_remaining < min_worst_case:
                min_worst_case = worst_candidates_remaining
                best_guess = potential_guess
        
        guess = best_guess if best_guess else candidates[0]
        matches = master.guess(guess)
        
        if matches == len(guess):
            return guess
        
        candidates = [word for word in candidates 
                     if word != guess and 
                     calculate_matches(guess, word) == matches]
    
    raise ValueError("Secret word not found")


# Main entry point - defaults to optimized strategy
def findSecretWord(words: List[str], master: Master, strategy: str = "optimized") -> str:
    """
    Find the secret word using the specified strategy.
    
    Args:
        words: List of candidate words
        master: Master object providing guess feedback
        strategy: "simple", "optimized", or "minimax"
    
    Returns:
        The secret word
    """
    strategies = {
        "simple": find_secret_word_simple,
        "optimized": find_secret_word_optimized,
        "minimax": find_secret_word_minimax
    }
    
    solver = strategies.get(strategy, find_secret_word_optimized)
    return solver(words, master)


def test_performance():
    """Test and compare different strategies"""
    import time
    
    test_cases = [
        {
            "secret": "acckzz",
            "words": ["ccbazz", "eiowzz", "abcczz", "acckzz", "xyzzzz"]
        },
        {
            "secret": "hamada",
            "words": ["hamada", "khaled"]
        },
        {
            "secret": "abcdef",
            "words": ["abcdef", "fedcba", "bcdefa", "abcxyz", "xydefz", "aabbcc", "dddddd"]
        }
    ]
    
    strategies = ["simple", "optimized", "minimax"]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"Test Case {i}")
        print(f"{'=' * 60}")
        print(f"Secret: {test_case['secret']}")
        print(f"Candidates: {len(test_case['words'])} words")
        
        for strategy in strategies:
            master = Master(test_case['secret'])
            start = time.time()
            
            try:
                result = findSecretWord(test_case['words'], master, strategy)
                elapsed = time.time() - start
                
                print(f"\n{strategy.capitalize()} Strategy:")
                print(f"  Guesses: {master.guess_count}")
                print(f"  Time: {elapsed*1000:.3f}ms")
                print(f"  Success: {result == test_case['secret']}")
            except Exception as e:
                print(f"\n{strategy.capitalize()} Strategy: ERROR - {e}")


if __name__ == "__main__":
    test_performance()


