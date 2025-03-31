def vowelConsonent(x):
    vowels=["a","e","i","o","u"]
    string=x.lower()
    vowel_count=0
    consonent_count=0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] in vowels:
              vowel_count=vowel_count+1
            else:
                consonent_count=consonent_count+1

    return vowel_count, consonent_count


print(vowelConsonent("Hello, World! 123"))

#Time Complexity = O(n)
#Space Complexity = O(1)