
# Read in file line


# ==== Format the line into correct postal address style ====
# Remove ellipses and separate string into a list
#line = "Anaheim Neighborhood Market #5640 1120 S Anaheim Blvd…".replace("…", "")
line = "Atwater Walmart #5890 800 Commerce Ave…".replace("…", "")
line = line.split(" ")

# Parse string to construct city/street address
for i in range(len(line)):
    if "Walmart" in line[i] or "Neighborhood" in line[i]:
        city = line[0:i]
    if "#" in line[i]:
        street = line[i+1:len(line)]

print("==== Results ====")
print("Street: %s" % street)
print("City: %s" % city)

address = " ".join(map(str, street)) + ", " + " ".join(map(str, city)) + ", CA"
print(address)

# Write new address format into new file
