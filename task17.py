with open("Input/students.txt") as inputfile, open("Output/output17.txt", "w") as outputfile:
    names = inputfile.readlines()
    a_names = filter(
        lambda name: name.lower().startswith("a"),
        names
    )
    outputfile.writelines(a_names)