# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
sum_list = 0

def avg_temp(sum_list):
    with open('temps.txt') as file_object:
        line_list = file_object.readlines()
    list_length = len(line_list)
    for i in range(1, list_length):
        line_list[i] = int(line_list[i])

    for i in range(1, list_length):
        line_list[i] = int(line_list[i])
        sum_list = sum_list + int(line_list[i])
        avg = sum_list/list_length

    return avg


if __name__ == '__main__':
    print(avg_temp(sum_list))

