def recognition_site(base_seq, recognition_seq):
    """Return the first position in base_seq where recognition_seq occurs, or -1 if not found."""
    return print(base_seq.find(recognition_seq))

recognition_site("AAATTCAGGCATTACGGACGTT", "CAG")