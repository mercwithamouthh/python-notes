#print out key names

classmates = {
    "billy" : 8,
    "vance" : 12,
    "alice" : 10,
    "eliza" : 15,
    "xavier" : 6
}

for x in classmates:
    print(x)

#print out values

for x in classmates.values():
    print(x)

#print out both keys and values

for x,y in classmates.items(): 
    print(x,y)

#checkpoint

measurement = {
    "length": 5,
    "width" : 3,
    "depth" : 10
}

for x in measurement.values():
    print(x)

amanda_value = int(input("How many people does Amanda bring?"))

jane_value = int(input("How many people does Jane bring?"))

group = {
    "Fred" : 12,
    "Jackson" : 15,
    "Sophie" : 20,
    "Amanda" : amanda_value,
    "Jane" : jane_value,
}

#family banquet

group = { 
    4: "Jared",
    5: "McKann",
    6: "Kyle",
    7: "Summer", 
    8: "?" #placeholder for input
}

missing_name = input("Enter the name for the person seated at number 8: ")

group[8] = missing_name

for x in group:
    group[x] += " Nelson"

print(group)

#shoes

# Initial dictionary with a placeholder for the missing key and value
group = {
    "Sally": 10,
    "Cameron": 3,
    "Spencer": 6,
    # Placeholder for the missing key and value
    'missing_key': 0
}

# Input for the missing key and value
key_input = input("Enter the name for the missing entry: ")
value_input = int(input("Enter the number of pairs of shoes for the missing entry: "))

# Update the dictionary with the user-provided key and value
group[key_input] = value_input
del group['missing_key']  # Remove the placeholder entry

# Print out the formatted string for each item in the dictionary
for key, value in group.items():
    print(f"{key} has {value} pairs of shoes.")
