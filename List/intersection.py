a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# set function to find intersection
intersection = list(set(a) & set(b))
print("Intersection of a and b:", intersection)

s1 = set(a)
s2 = set(b)
# using intersection() method

s3 = s1.intersection(s2)    # s3 will contain the intersection of s1 and s2 and s3 is also a set
print("Intersection using intersection() method:", list(s3))