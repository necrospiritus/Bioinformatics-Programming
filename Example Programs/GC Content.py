def validate_base_sequence(base_sequence, RNAflag=False):
    """Return True if the string base_sequence contains only upper- or lowercase T (or U, if RNAflag), C, A, G characters, otherwise False"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('A') + seq.count('U' if RNAflag else 'T') +
                        seq.count('G') + seq.count('C'))


def gc_content(base_seq, RNA=False):
    """Return the percentage of G and C characters in base_seq"""
    assert validate_base_sequence(base_seq, RNA), "argument has invalid characters!"
    seq = base_seq.upper()
    result = (seq.count('G') + seq.count('C')) / len(seq)
    return print(result)


# USAGE
gc_content("AACCCTTGG")  # For sequence Sample
gc_content("AAGGCCUU", True)  # For RNA Sample
