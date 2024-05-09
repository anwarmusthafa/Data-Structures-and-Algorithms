def frequency(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for key,value in d.items():
        print(f"number {key} occured {value} times")

s = [2,3,4,5,4,3,2,3,4,5,6,7,89,7,6,5]
frequency(s)