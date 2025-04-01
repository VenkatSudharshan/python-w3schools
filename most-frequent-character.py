def freqChar(s):
    dict={}
    for ch in s.lower():
        if ch not in dict:
            dict[ch]=1
        else:
            dict[ch] += 1
    max_char=''
    max_count=0
    for ch in dict:
        if(dict[ch]>max_count):
            max_char=ch
            max_count=dict[ch]
    return max_char, max_count


    

print(freqChar("Hello"))

#Time Complexity = O(n)
# Space Complexity = O(1)