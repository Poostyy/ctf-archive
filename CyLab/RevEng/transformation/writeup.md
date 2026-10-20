**Site : cylab** 

**Tag : rev** 

**Problem Name : Transformation** 

**Idea Type : decode based on encoder** 

**Approach :**

we're given a piece of code, and a file containing some string. The code uses the flag, hence it's quite obvious that these code are the one that made the given string and we need to decode it.
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
each iteration takes up 2 consecutive char idx from the flag, hence every character from the given string are made from 2 consecutive character from the flag, in other words suppose the given string is s then : 
s[0] = chr((ord(flag[0]) << 8) + ord(flag[1]))
s[1] = chr((ord(flag[2]) << 8) + ord(flag[3]))
and so on...

we need decode every char and split it into 2. We know that << 8 means shifting the bit to the left side eight times which also mean multipliying it by 2^8. Suppose we have 9, then 9 << 8 equals to 9 * 2^8. and then this gives us

s[0] = chr((ord(flag[0]) * 2^8) + ord(flag[1]))

ord(s[0]) = ord(flag[0] * 2^8) + ord(flag[1])

ord(s[0]) % 2 ^ 8 = ord(flag[1])

floor(ord(s[0]) / 2^8) = ord(flag[0]) :: since ord(flag[1]) < 2^8

then we get both ord(flag[0]) and ord(flag[1]) and we can do this for every index
