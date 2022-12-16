if __name__ == '__main__':
    arr = list(map(int, input().split()))
    freq = dict()
    for num in arr:
        freq[num] = freq.get(num,0)+1

    for key , value in freq.items():
        if value == 1 :
            print(key,end = " ")