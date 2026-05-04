from rich.table import Table
from rich.console import Console
from rich_gradient import Gradient
import string
import strength

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

class Suggest:
    def __init__(self, string):
        self.string = string
        self.suggestions = []
        self.strengthlist = []
        self.entropylist = []
        self.console = Console()
        self.table = Table(title="Analysis Results")

    def append(self):
        calculate = strength.CalculateStrength(self.string)
        score = calculate.calculate()
        matches = calculate.matches
        bits = calculate.entropy()
        combinations_str = f'Possible combinations: 2^{bits:.2f}'
        seconds = calculate.estimate_crack_time(bits, attempts_per_sec=1e9)
        total_time = calculate.format_time(seconds)

        if not any(l in lowercase for l in self.string):
            self.suggestions.append('Add lowercase characters.')
        
        if not any(u in uppercase for u in self.string):
            self.suggestions.append('Add uppercase characters.')

        if not any(d in digits for d in self.string):
            self.suggestions.append('Add numbers.')
        
        if not any(s in special for s in self.string):
            self.suggestions.append('Add special characters.')

        if len(self.string) < 10:
            self.suggestions.append('Make your password longer.')

        if matches:
            self.suggestions.append('Don\'t use dictionary words\n(even if modified).')

        if score <= 4:
            self.strengthlist.append('Weak')
            self.strengthlist.append(f'Score: {score}/10')
        elif score > 4 and score <= 7:
            self.strengthlist.append('Medium')
            self.strengthlist.append(f'Score: {score}/10')
        elif score > 7:
            self.strengthlist.append('Strong')
            self.strengthlist.append(f'Score: {score}/10')

        if bits <= 40:
            self.entropylist.append(combinations_str + ' (weak)\nBreaks fast.')
        elif bits > 40 and bits <= 60:
            self.entropylist.append(combinations_str + ' (medium)\nNot bad.')
        elif bits > 60 and bits <= 80:
            self.entropylist.append(combinations_str + ' (strong)\nStandard.')
        elif bits > 80 and bits <= 100:
            self.entropylist.append(combinations_str + ' (very strong)\nPerfect password.')
        elif bits > 100:
            self.entropylist.append(combinations_str + ' (extremely strong)\nImpossible to brute force.')

        self.entropylist.append('Estimated time to break\nby a single computer (1e9 attempts per sec):\n' + total_time)

    def show_table(self):
        formatted_suggestions = "\n".join(
            [f"{i}. {item}" for i, item in enumerate(self.suggestions, 1)]
        )
        formatted_strength = "\n".join(
            [f"{i}. {item}" for i, item in enumerate(self.strengthlist, 1)]
        )
        formatted_entropy = "\n".join(
            [f"{i}. {item}" for i, item in enumerate(self.entropylist, 1)]
        )
        
        self.table.add_column(Gradient("Strength", colors=['yellow', 'red', 'purple']), justify="center")
        self.table.add_column(Gradient("Suggestions", colors=['blue', 'white', 'orange']), justify="left")
        self.table.add_column(Gradient("Entropy (estimated)", colors=['orange', 'purple', 'yellow']), justify="left")

        if not formatted_suggestions:
            self.table.add_row(formatted_strength, 'No suggestions, your\npassword is perfect!', formatted_entropy)
        else:
            self.table.add_row(formatted_strength, formatted_suggestions, formatted_entropy)

        self.console.print(self.table)