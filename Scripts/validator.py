class Validate:
    def __init__(self, string):
        self.string = string

    def is_blank(self):
        return self.string.strip() == ''
    
    def has_spaces(self):
        return ' ' in self.string
    
    def invalid_length(self):
        return len(self.string) < 5 or len(self.string) > 64
    
    def invalid_chars(self):
        return not self.string.isprintable()
    
    def is_valid(self):
        if self.is_blank():
            return False
        
        if self.has_spaces():
            return False
        
        if self.invalid_length():
            return False
        
        if self.invalid_chars():
            return False
        
        return True