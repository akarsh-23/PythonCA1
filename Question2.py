def distinctNumbers(List):
    list_set = set(List)
    List = list(list_set)
    return List


List = [int(x) for x in input("Enter values: ").split()]
print(distinctNumbers(List))