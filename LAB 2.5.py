# Student ID : 1201200302 #
# Student Name : Liang Chia Yiau #

water = 0.15

print("Natural Mineral Water Dispenser")
print("----------------------------------")
litre = float(input("Enter amount of litres :"))

print("Price per litre  = RM",water)
print("Number of litres =",litre)
print("Total : RM{:.2f}".format(litre*water))
