"""
Author: Brandon Luu
Date: 2/22/16
Description: This is a script that reads a file with Wal-Mart CSV address list
and then writes a correct postal address style format into another file.
"""
# Input/Output file names
input_file = "CA_Walmart.csv"
output_file = "CA_Walmart_Address.csv"


# Open files
in_fd = open(input_file, 'r')
out_fd = open(output_file, 'w')


# Format each line into correct postal address style
for line in in_fd:
    # Remove ellipses and separate string into a list
    # line = "Atwater Walmart #5890 800 Commerce Ave…".replace("…", "")
    line = line.split(" ")

    # Parse string to construct city/street address
    for i in range(len(line)):
        if "Walmart" in line[i] or "Neighborhood" in line[i]:
            city = line[0:i]
            city = " ".join(map(str, city))
        if "#" in line[i]:
            # Read the rest of the line, but not the final newline character
            street = line[i+1:len(line)-1]
            street = " ".join(map(str, street))

    # Combine address info into one postal string
    address = '%s, %s, CA\n' % (street, city)
    print("Address: %s" % address)

    """
    # Test outputs
    print("==== Results ====")
    print("Street: %s" % street)
    print("City: %s" % city)
    print("Address: %s" % address)
    """
    # Write new address format into new file
    out_fd.write(address)

# Close Files
in_fd.close()
out_fd.close()
