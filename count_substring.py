def count_substring(arr1, arr2):

    a = len(arr1)
    b = len(arr2)

    # longest common substring is set as zero
    longest = 0
    end_index = a

    # lookup is a table initially filled with zero
    lookup = []
    for i in range(a+1):
        temp = []
        for j in range(b+1):
            temp.append(0)
        lookup.append(temp)


# Finding the longest common substring
    for i in range(1, a+1):
        for j in range(1, b+1):

            if(arr1[i - 1] == arr2[j - 1]):
                lookup[i][j] = lookup[i - 1] [j - 1] + 1 

                if lookup[i][j] > longest:
                    longest = lookup[i][j]
                    end_index = i

    return arr1[end_index - longest : end_index]



if __name__ == '__main__':
   
    arr1 = [3, 6, 7, 4, 2, 7, 9, 1, 0, 3, 5, 6] 
    arr2 = [1, 5, 6, 9, 7, 4, 2, 7, 9, 9, 2, 1] 

    print(count_substring (arr1, arr2))

