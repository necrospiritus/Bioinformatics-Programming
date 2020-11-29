"""Return the first position in base_seq where recognition_seq occurs, or -1 if not found."""


def recognition_site(base_seq, recognition_seq):
    return base_seq.find(recognition_seq)


"""Return a pair of sequences derived from base_seq by splitting it at first appearance of recognition_seq; offset,
which may be negative, is the number of bases relative to the beginning of the site where the sequence is cut"""


def restriction_cut(base_seq, recognition_seq, offset=0):
    site = recognition_site(base_seq, recognition_seq)
    return base_seq[:site + offset], base_seq[site + offset:]


my_seq = "AAATTCGGACAGGCATTACGGACGTTCCGGAGGA"
left, right = restriction_cut(my_seq, 'TACGG')
print("Left of Seq= ", left)
print("Right of Seq= ", right)
