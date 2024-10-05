maths = {"John", "Alice", "Bob", "Charlie"}
science = {"Alice", "David", "Bob", "Eve"}

both_classes = maths.intersection(science)
only_one_class = maths.symmetric_difference(science)
science_not_maths = science.difference(maths)
maths_not_science = maths.difference(science)

print("In both classes:", len(both_classes), both_classes)
print("Only in one class:", len(only_one_class), only_one_class)
print("In science but not in maths:", len(science_not_maths), science_not_maths)
print("In maths but not in science:", len(maths_not_science), maths_not_science)