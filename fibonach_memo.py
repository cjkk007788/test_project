dictionary={

    1:1,
    2:1
}

def fibonachi(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonachi(n-1)+fibonachi(n-2)
        dictionary[n] = output
        return output
    

print(fibonachi(10))
print(fibonachi(20))
print(fibonachi(30))
