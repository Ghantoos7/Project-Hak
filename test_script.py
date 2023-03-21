

def openFile(file_name):

    with open(file_name, "r") as file1:
        name_list = []
        for f in file1:
            name_list.append(f.lower())
        return name_list
# method to open a file and store each line as an element in a list


def writeToFile(valid_list,file_name):

    with open(file_name, "w") as file:
        for valid in valid_list:
            file.write(valid + "\n")
# method to write to a file and store each element in the list in a line
