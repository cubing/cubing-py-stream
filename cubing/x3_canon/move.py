class Move:
    
    def __init__(self, family, amount=1):
        if not len(family):
            raise ValueError
        if family.endswith("'"):
            self.amount = 3
            family = family[:-1]
        elif family[-1].isdigit():
            self.amount = int(family[-1])
            family = family[:-1]
        else:
            self.amount = 1
        self.family = family
        self.amount *= amount
        
    def __str__(self):
        r = self.family
        if self.amount == 3:
            r += "'"
        elif self.amount == 2:
            r += "2"
        elif self.amount == 1:
            pass
        else:
            raise ValueError
        return r

    def __repr__(self):
        return str(dict(vars(self)))
