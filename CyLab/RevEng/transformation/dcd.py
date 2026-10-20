s = "慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽"
ans = ""
for i in range(0, len(s)):
    a = ord(s[i]) // 256
    b = ord(s[i]) % 256
    ans += chr(a) + chr(b)
print(ans)