104. Please write a program which accepts a string from console and print it in 
reverse order.
 Example: If the following string is given as input to the program:*
rise to vote sir
Then, the output of the program should be:
ris etov ot esir

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")
