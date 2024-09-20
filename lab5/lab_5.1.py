def divide_in_two_lists_by_element(start_list: list, index):
    if 0 <= index < len(start_list):
        list_one = start_list[:index].copy()
        list_two = start_list[index:len(start_list)].copy()
        print("List: ", start_list, "\nFirst list: ", list_one, "\nSecond list: ", list_two, "\n")
    elif 0 > index >= -len(start_list):
        list_one = start_list[-len(start_list):index].copy()
        list_two = start_list[index:].copy()
        print("List: ", start_list, "\nFirst list: ", list_one, "\nSecond list: ", list_two, "\n")
    else:
        print("Index out of bound\n")

size = int(input("Input size: "))
super_list = [input("Input element "+str(i)+": ")for i in range(size)]
split_index = int(input("Which index use to split this list? "))
divide_in_two_lists_by_element(super_list, split_index)