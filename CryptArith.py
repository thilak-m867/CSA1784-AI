import itertools

def solve_cryptarithmetic():
    # Step 1: Extract all unique letters from the puzzle words
    words = ["SEND", "MORE", "MONEY"]
    unique_letters = set("".join(words))
    
    # Convert set to a list so it has a fixed order for mapping
    letters = list(unique_letters)
    
    # Quick sanity check: if there are more than 10 unique letters, it's impossible
    if len(letters) > 10:
        print("No solution found (more than 10 unique letters).")
        return
    
    # Store leading letters to easily enforce Step 3
    leading_letters = {word[0] for word in words}
    
    # Step 2: Generate permutations of digits 0-9 for the number of unique letters
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        # Create a dictionary mapping each letter to a digit
        mapping = dict(zip(letters, perm))
        
        # Step 3: For each mapping, ensure no leading zeros
        if any(mapping[letter] == 0 for letter in leading_letters):
            continue
            
        # Helper function to convert a word to its numerical value based on mapping
        def word_to_value(word):
            return int("".join(str(mapping[char]) for char in word))
            
        # Step 4: Evaluate the arithmetic expression numerically
        send_val = word_to_value("SEND")
        more_val = word_to_value("MORE")
        money_val = word_to_value("MONEY")
        
        # Step 5: Return the mapping if the equation holds
        if send_val + more_val == money_val:
            print("Solution Found!")
            print(f"  {send_val}  (SEND)")
            print(f"+ {more_val}  (MORE)")
            print(f"-------")
            print(f" {money_val}  (MONEY)")
            print("\nLetter Mapping:")
            for letter in sorted(mapping.keys()):
                print(f"{letter}: {mapping[letter]}")
            return
            
    # Step 6: Print 'No solution found' if the loop finishes without returning
    print("No solution found.")

# Run the program
solve_cryptarithmetic()
