So, continuing what we saw in the Readme.md file, I will now explain generator using with an example:
Here's a simple example of a generator that calculates the squares of each (non-negative) number up to and excluding N
```
def squares(N):
    for i in range(N):
        yield i * i

for i in squares(4):
    print(i)
```

Let's break down this snippet, highlighting the mentioned differences. First, notice that there is no return statement, but instead, there is a yield expression. The yield expression is responsible for two actions:

    - A signal to the Python interpreter that this function will be a generator.
    - Suspends the function execution, keeping the local variables in memory, until the next call.

The suspension of execution, saving local variables, and then resuming operation is what allows the generator to act like a stream. We can even make generators that can continue execution forever. Here's a count generator that continuously counts from 1 until the program terminates:

```
def count():
    i = 1
    while True:
        yield i
        i += 1

for i in count():
    print(i)
```

