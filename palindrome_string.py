# Check if a string is a palindrome
s="maddiam"
len=len(s)
palindrome=True
print(len)

# Compare first half with second half
for i in range(len//2):
    # compare character from start and end
    if s[i]!=s[len-i-1]:
        palindrome=False
        # exit loop if mismatch found
        break
print(palindrome)
    