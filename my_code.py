# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  


def avg_temp():
    sum_list = 0
    with open('temps.txt') as file_object:
        line_list = file_object.readlines()
        list_length = len(line_list) - 1
        for i in range(list_length):
            list_length = int(list_length)
        for i in range(1, len(line_list)):
            sum_list = sum_list + int(line_list[i])
            avg = sum_list/list_length
            real_avg = round(avg, 2)
    return real_avg


if __name__ == '__main__':
    print(avg_temp())

