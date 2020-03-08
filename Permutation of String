def permute(arr):
    dict = {}
    for i in arr:
        if i in dict.keys():
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    keys = sorted(dict)
    str = []
    count = []
    start=0
    for key in keys:
        str.append(key)
        count.append(dict[key])
    result = [0]*len(arr)
    print(str, count, result, start)
    permutation(str, count, result, start)

def permutation(str, count, result, start):
    if start == len(result):
        print(result)
        return

    for i in range(len(str)):
        if count[i] == 0:
            continue
        result[start] = str[i]
        count[i] -= 1
        permutation(str, count, result, start + 1)
        count[i] += 1

if __name__ == '__main__':
    input = ['A', 'A', 'B','C']
    permute(input)
