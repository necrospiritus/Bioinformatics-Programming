from random import randint


def sb_mutation(base_seq):
    """"Return a Sequence with base at a randomly selected position of base_seq,
    replaced by a base chosen randomly from three bases that are not at position."""
    position = randint(0, len(base_seq) - 1)
    bases = "TACG"
    bases = bases.replace(base_seq[position], "")
    new_seq = base_seq.replace(base_seq[position], bases[randint(0, 2)])
    return print(new_seq)

#USAGE
sb_mutation("AATTCCGG")
