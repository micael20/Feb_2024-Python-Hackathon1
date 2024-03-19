def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return

    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence up to term", n, "is:", fibonacci_sequence)

if __name__ == "__main__":
    main()