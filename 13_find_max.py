def find_max(tab):
    max=0
    for i in tab:
        if max < i:
            max=i
        
    return max


values=[10, 2, 8, 99, 5, 4, 2, 1, 4, 13]
print(find_max(values))


