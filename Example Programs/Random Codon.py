from random import randint

def random_base(RNAflag = False):
    return ("UCAG" if RNAflag else "TCAG")[randint(0,3)]

def random_codon(RNAflag = True):
    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)

print(random_codon())