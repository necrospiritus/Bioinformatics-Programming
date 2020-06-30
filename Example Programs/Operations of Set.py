# A 'set' is an unordered collection of characters that contains no duplicates.
# The 'set' type is mutable, The 'frozenset' type is immutable

DNA = set("ATCG")
RNA = set("AUCG")

print("sequence Bases:", DNA)
print("RNA Bases:", RNA)

# Algebraic set operations
print("Union of sequence and RNA:", DNA | RNA)
print("Intersection of sequence and RNA:", DNA & RNA)
print("Differences of sequence from RNA:", DNA - RNA)
print("Differences of RNA from sequence:", RNA - DNA)
print("Symmetric Differences of sequence and RNA.", DNA ^ RNA)
print("Every element in sequence is in RNA:", DNA <= RNA)  # False because of RNA does not contain T
print("Every element in RNA is in sequence:", DNA >= RNA)  # False because of sequence does not contain U
