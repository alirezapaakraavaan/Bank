import re

def increase_branch_customer_count(branch_name, index):
    with open("Branch.txt", "r") as file:
        all_text = file.readlines()


    with open("Branch.txt", "w") as file:
        for i, line in enumerate(all_text):
            if branch_name in line:
                words = line.split(",")
                branch_customers_count = words[1][1]
                indices = [m.start() for m in re.finditer(r'\d+', line)]
                index_to_change = indices[index]
                branch_customers_count = int(branch_customers_count)
                branch_customers_count += 1
                branch_customers_count = str(branch_customers_count)
                text_list = list(line)
                text_list[index_to_change] = branch_customers_count
                all_text[i] = ''.join(text_list)

    with open("Branch.txt", "w") as file:
            file.writelines(all_text)

    return words[-2]