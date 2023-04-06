class Currency:
    
    rate =  { "USD": 2.7, "EUR": 3, "GEL": 1 }
    
    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit.upper()
        
        
    def __str__(self):
        return "{:.2f}".format(self.value) + " " + self.unit
    
        
    def __add__(self, other):
        if isinstance(self, Currency) and isinstance(other, Currency):
            return Currency(self.value + other.ChangeTo(self.unit).value, self.unit)
        
        elif isinstance(self,Currency ) and isinstance(other, int):
            return Currency(self.value + other, self.unit)
        
    def __radd__(self, other):
        if isinstance(self, Currency) and isinstance(other, int):
            return Currency(self.value + other, self.unit)
    
    def __mul__(self, other):
        if isinstance(self, Currency) and isinstance(other, int):
            return Currency(self.value * other, self.unit)
        
    def __rmul__(self, other):
        if isinstance(self, Currency) and isinstance(other, int):
            return Currency(self.value * other, self.unit)
    
    def __lt__(self, other):
        return self.ChangeTo("gel").value < other.ChangeTo("gel").value 
    
    def __gt__(self, other):
        return self.ChangeTo("gel").value > other.ChangeTo("gel").value 
    
    def __le__(self, other):
        return self.ChangeTo("gel").value <= other.ChangeTo("gel").value 
    
    def __ge__(self, other):
        return self.ChangeTo("gel").value >= other.ChangeTo("gel").value 
    
    def __eq__(self, other):
        return self.ChangeTo("gel").value == other.ChangeTo("gel").value 
    
    def __ne__(self, other):
        return self.ChangeTo("gel").value != other.ChangeTo("gel").value 
        
    def ChangeTo(self, currceny):
        new_value = self.value * self.rate[self.unit] / self.rate[currceny.upper()]
        new_unit = currceny.upper()
        return Currency(new_value, new_unit)
    
    
c1 = Currency(3, "eur")
c2 = Currency(3, "usd")
c3 = Currency(3, "gel")

print(c1)
print(c2)
print(c1!=c2)
