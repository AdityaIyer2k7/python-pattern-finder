def find_transpose(nums):
    tnode1 = nums[1] - nums[0]
    tnode2 = nums[1] / nums[0] if nums[0] != 0 else 1
    return (tnode1, tnode2)

def check_transpose(numbers):
    tnode1, tnode2 = find_transpose(numbers)
    cnode1 = True
    cnode2 = True
    for i in range(len(numbers)-1):
        cnode1 = cnode1 and\
        (find_transpose(numbers[i:])[0] == tnode1)
        cnode2 = cnode2 and\
        (find_transpose(numbers[i:])[1] == tnode2)
    return (tnode1, tnode2), (cnode1, cnode2)

def find_next(numbers):
    (tnode1, tnode2), (cnode1, cnode2) = check_transpose(numbers)
    if cnode1:
        return numbers[-1]+tnode1
    if cnode2:
        return numbers[-1]*tnode2

def find_complex(numbers):
    if find_next(numbers) != None:
        return find_next(numbers)
    tnode1p = []
    tnode2p = []
    for i in range(len(numbers)-1):
        nd1, nd2 = find_transpose(numbers[i:])
        tnode1p.append(nd1)
        tnode2p.append(nd2)

    tnode1pcom = find_complex(tnode1p)
    tnode2pcom = find_complex(tnode2p)
    if tnode1pcom != None:
        return numbers[-1]+tnode1pcom
    if tnode2pcom != None:
        return numbers[-1]*tnode2pcom

if __name__ == "__main__":
    while True:
        nums = [eval(i) for i in input("Pattern: ").strip(" ").split(" ")]
        print(find_complex(nums))
