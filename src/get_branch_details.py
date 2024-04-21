def get_branch_details(name):
    with open("Branch.txt", "r") as file:
        for line in file:
            if name in line:
                words = line.replace(",", "")
                words = words.split()
                return words
            
    return "Not Found!"


# words = get_branch_details("Dovom_Branch")
# print(words[1])



def edit_branch_file(name):
    with open("Branch.txt", "r") as file:
        all_text = file.readlines()

    with open("Branch.txt", "w") as file:
        for i, line in enumerate(all_text):
            if name in line:
                all_text[i] = line.replace(line, "")

    with open("Branch.txt", "w") as file:
        file.writelines(all_text)
