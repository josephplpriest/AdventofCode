def is_nice(word: str) -> bool:
    naughty_list = ["ab", "cd", "pq", "xy"]
    nice_list = "aeiou"

    for i in range(len(word)-1):
        if word[i:i+2] in naughty_list:
            return False

    vowel_count = 0
   
    double = False
    enough_vowels = False

    for i in range(len(word)):
        if word[i] in nice_list:
            vowel_count += 1
            if vowel_count >= 3:
                enough_vowels = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            double = True
    
    return (double and enough_vowels)

with open("input5.txt") as file:
    data = file.read().split("\n")

print(sum(map(is_nice, data)))