def slove(vector):
    length = len(vector)
    scan = [0] * length
    scan_revers = [0] * length

    for i in range(1, length):
        if vector[i - 1] < vector[i]:
            scan[i] = scan[i - 1] + 1
    print 'scan        ', scan
    for i in range(length - 2, -1, -1):
        if vector[i] > vector[i + 1]:
            scan_revers[i] = scan_revers[i + 1] + 1
    print 'scan_revers ', scan_revers

    ans = 0
    for i in range(0, length - 1):
        if ans < scan[i] + scan_revers[i] + 1:
            ans = scan[i] + scan_revers[i] + 1
    return ans


print slove([5, 3, 4, 9, 7])