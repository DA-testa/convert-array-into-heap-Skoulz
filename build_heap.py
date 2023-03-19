# python3

#221RDB060 Artjoms Sidorkins

def build_heap(users_data):
    swaps = []

    n = len(users_data)
    for i in range(n // 2 - 1, -1, -1):
        heap(i, users_data, swaps)
    return swaps 

def heap(i, users_data, swaps):
    n = len(users_data)
    min = i
        
    first = 2 * min + 1
    second = 2 * min + 2

    if first < n and users_data[first] < users_data[min]:
            min = first
    if second < n and users_data[second] < users_data[min]:
        min = second

    if i != min:
        users_data[i], users_data[min] = users_data[min], users_data[i]
        swaps.append((i, min))
        users_data[i], users_data[min] = users_data[min], users_data[i]
        heap(min, users_data, swaps)




def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    
    users_input = input()
    if "I" in users_input:
        n = int(input())
        users_data = list(map(int, input().split()))
    if "F" in users_input:
        users_file = input()
        if 'a' not in users_file:
            with open('tests/' + users_file, 'r', encoding='UTF-8') as files:
                n = int(files.readline())
                users_data = list(map(int, files.readline().split()))
    else:
        print("wrong input")



    # checks if lenght of data is the same as the said lenght
    assert len(users_data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(users_data)

    # TODO: output hoШw many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4 * n
    print(len(swaps))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == '__main__':
    main()
