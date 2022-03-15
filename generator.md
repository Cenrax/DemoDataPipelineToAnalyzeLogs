So, continuing what we saw in the Readme.md file, I will now explain generator using with an example:
Here's a simple example of a generator that calculates the squares of each (non-negative) number up to and excluding N
```
def squares(N):
    for i in range(N):
        yield i * i

for i in squares(4):
    print(i)
```
