import sys

def main():
    # For testing - UNCOMMENT these two lines
    with open('test_cases/input_01.txt', 'r') as f:
        data = f.read().split()
    
    # For competition - use this line instead
    # data = sys.stdin.read().split()
    
    if not data:
        return
    
    # Your solution here
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    total = sum(arr)
    print(f"Sum: {total}")

if __name__ == "__main__":
    main()
