#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle the case where the length is 0
    if length == 0:
        print("[]")
        return
    
    # Handle the case where the length is 1
    if length == 1:
        print("[0]")
        return
    
    # Initialize Fibonacci sequence with first two elements
    fibonacci_sequence = [0, 1]

    # Generate Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
        
        # Terminate the loop if the length exceeds or equals the specified length
        if len(fibonacci_sequence) >= length:
            break

    # Print the Fibonacci sequence
    #print(f"Fibonacci sequence up to length {length}:")
    print(fibonacci_sequence)

# Test the function
#print_fibonacci(10)
    