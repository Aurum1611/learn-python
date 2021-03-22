a, b, c, d = 12, 19, 1.23, 0.9183
print(a, b, c, d, sep='}{')

name, place, hobby = "Shouto Kiragiri", "Tokyo, Japan", "Anime"
print("Watashi wa namae %s desu. From %s. %s wa aishteru desu." % (name, place, hobby))

print("%.2f" % d)

print("Watashi wa namae {} desu. From {}. {} wa aishteru desu.".format(name, place, hobby))

print("Watashi wa namae {0} desu. From {2}. {1} wa aishteru desu.".format(name, place, hobby))
