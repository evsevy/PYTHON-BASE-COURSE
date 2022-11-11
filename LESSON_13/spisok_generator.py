def square(n): return n**2

# def cube(n): return n**3

operations = [square]
numbers = list(map(int, input().split()))   #[2, 1, 3, 4, 7, 11, 18, 29]
for i, n in enumerate(numbers):
    action = operations[i % 1]
    print(f"{action.__name__}({n}):", action(n))
    
