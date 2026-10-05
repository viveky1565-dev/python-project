str1 = "i m learning python programming beginners"
char = "n"
count = 0

for i in str1:
    if i == char:
        count += 1

print("number of occurrences : ", count)



def unique_word_count(text):
    word = text.lower()
    unique_word = set(word)
    return len(unique_word)

text = "hello world hello programming hello python "
print(unique_word_count(text))



s1 = 'Race Car'
s2 = s1.replace('',"")
rev = s2[::-1]
if s2.casefold() == rev.casefold():
    print(s1)
else:
    palindrome = s2.casefold() + rev.casefold()
    print(palindrome)