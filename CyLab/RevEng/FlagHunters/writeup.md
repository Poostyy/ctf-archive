**site : CyLab**

**Tag : Reverse Engineering**

**Problem Name : Flag Hunters**

**Idea Type : Somewhere Obvious**

We first focus on this line of code
```python
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'
```
Notice that flag var possibly consist of the flag we're looking for

if we run the code, it runs the song and its consist of secret_intro + other part of the song

the main thing we see is that it never reads the secret intro which made it obvious that the flag is probably there hence the problem simplifies into : 

**How do i made it also run the secret intro.**

which leaves us to this part of the code : 
```python
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1
```
from that code, we know lip is for the index of verse and song_lines is an array of the every line, hence it's obvious we just need to find a way to acces the first verse (the intro which consist the flag) and it happens when we enter the return case then we take the second word which is [0 - 9]. Since we want 0 we just need to input with RETURN 0;
