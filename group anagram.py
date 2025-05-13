def groupAnagrams(strs):
    # Dictionary to group anagrams
    anagrams = {}

    for word in strs:
        # Create a frequency array for the current word
        count = [0] * 26  # 26 letters in the alphabet

        for char in word:
            # Increment the count for the corresponding character
            count[ord(char) - ord('a')] += 1

        # Use the tuple of the frequency array as the key
        key = tuple(count)

        # Group words with the same key
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage
if __name__ == "__main__":
    strs = input("Enter a list of strings separated by spaces: ").split()
    print(groupAnagrams(strs))