import string
import os
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
regex_path = os.path.join(script_dir, 'regex.txt')

with open(regex_path, 'r', encoding='utf-8', errors='ignore') as f:
    dict_words = [line.strip().lower() for line in f if line.strip()]


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

class CalculateStrength:
    def __init__(self, string):
        self.string = string
        self.matches = []

    def calculate(self):
        score = 0

        if len(self.string) > 10 and len(self.string) <= 15:
            score += 2
        elif len(self.string) > 15:
            score += 4

        if any(l in lowercase for l in self.string):
            score += 1

        if any(u in uppercase for u in self.string):
            score += 1
        
        if any(d in digits for d in self.string):
            score += 2

        if any(s in special for s in self.string):
            score += 2

        lower_string = self.string.lower()
        matched_words = set()
        
        for word in dict_words:
            if word in lower_string:
                matched_words.add(word)

        final_matches = []
        for word in sorted(matched_words, key=len, reverse=True):
            if not any(word in final_match for final_match in final_matches):
                final_matches.append(word)

        self.matches = final_matches
        
        for match in self.matches:
            score -= 0.5

        return score
    
    def entropy(self):
        length = len(self.string)
        charset = 0

        if any(c.islower() for c in self.string):
            charset += 26

        if any(c.isupper() for c in self.string):
            charset += 26
        
        if any(c.isdigit() for c in self.string):
            charset += 10
        
        if any(not c.isalnum() for c in self.string):
            charset += 32

        if charset == 0:
            return 0
        
        entropy = length * math.log2(charset)
        return entropy
    
    def estimate_crack_time(self, entropy, attempts_per_sec=1e9):
        combinations = 2 ** entropy
        seconds = combinations / attempts_per_sec
        return seconds
    
    def format_time(self, seconds):
        if seconds < 60:
            return f'{seconds:.2f} seconds.'
        elif seconds < 3600:
            return f'{seconds/60:.2f} minutes.'
        elif seconds < 86400:
            return f'{seconds/3600:.2f} hours.'
        elif seconds < 31536000:
            return f'{seconds/86400:.2f} days.'
        else:
            return f'{seconds/31536000:.2f} years.'