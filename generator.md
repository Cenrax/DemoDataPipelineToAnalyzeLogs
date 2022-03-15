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

Using the next() function, you can see the generator and yield suspension work in action. In an iteration (like a for loop), the Python interpreter continuously calls the next() function to receive the "next" element in the iterable. In a generator, each call to the next() function completes a cycle, and then stops at the next yield. 

Suppose we wanted to give an upper limit to the count() function. Then we need to use a return statement within the generator. The return statement is one way that a Python loop (eg. for) knows when to stop looping. Using return without an argument ends the function and returns None, breaking the loop. Here's how we would update count() using return:

```
# Count with an upper limit of `N`.
def count(N):
    i = 1
    while True
        if i > N:
            return
        yield i
        i += 1

for i in count(5):
    print(i)
```

Now lets look at the ****Generator Comprehensions****
Generator comprehensions are extremely similar to list comprehensions. We can turn any list comprehension into a generator comprehension by replacing the square brackets [] to parenthesis (). For example, here's how we could write the squares function in the previous screen as a list and generator expression:

```
squared_list = [i * i for i in range(20)]
squared_gen = (i * i for i in range(20))
```

Before you begin replacing all your lists as generators, let's discuss a major drawback of the generator. Suppose we had two places in our code that wanted to use the squared_gen generator. With a list, squared_list, we could easily do:

```
num_to_square = {}
for idx, i in enumerate(squared_list):
    num_to_square[idx] = i
print(num_to_square)
```
{0: 0, 1: 1, 2: 4, 3: 9 ...}
