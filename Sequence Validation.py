def validate_base_sequence(base_sequence, RNAflag=False):
    """Return True if the string base_sequence contains only upper- or lowercase T (or U, if RNAflag), C, A, G characters, otherwise False"""
    seq = base_sequence.upper()
    result = len(seq) == (seq.count('A') + seq.count('U' if RNAflag else 'T') +
                          seq.count('G') + seq.count('C'))
    return print(result)


# USAGE
validate_base_sequence("TTAAGGCC")
