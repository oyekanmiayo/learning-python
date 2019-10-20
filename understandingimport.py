#Whenever the Python interpreter reads a source file, it does two things:
# it sets a few special variables like __name__, and then
# it executes all of the code found in the file.
# Let's see how this works and how it relates to your question about the __name__ checks we always see in Python scripts.

# Code Sample
# Let's use a slightly different code sample to explore how imports and scripts work. Suppose the following is in a file called foo.py.

# Link: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# Suppose this is foo.py.

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")