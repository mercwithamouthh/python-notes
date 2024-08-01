#--Checking strings is a way to see if a specific string is present in a variable

poolverine = "old men #love"
check= "#love" in poolverine
print(check)

#outputs True

poolverine = "old men #love"
check= "#love" not in poolverine
print(check)

#outputs False