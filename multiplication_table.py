number =int(input())

print("multiplication table for",number,":")
for i in range(1,11):
    result=number * i
    print(f"{number}X{i}={result}")
