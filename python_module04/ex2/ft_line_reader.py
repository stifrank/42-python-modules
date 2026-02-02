print("=== LOGBOOK CONTENT ===")

file = open("logbook.txt", "r")

line_number = 1
line = file.readline()

while line != "":
    print(f"Line {line_number}: {line.strip()}")
    line_number += 1
    line = file.readline()

file.close()

print("End of logbook.")
