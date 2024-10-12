# [2015 - Day 10 (Link)](https://adventofcode.com/2015/day/10)

## Part One
This one was a good break from the past couple of days more challenging problems. This one wasn't bad, I iterated through using a while loop, and a nested while loop. The purpose of the outer while loop is to ensure that I can skip over repeated instances of a number, and the repeated instances of a number are found using the nested while loop. After the nested while loop completes, I know how many instances of the number at i were sequential, then I can offset the outer while loop to skip over those numbers. Then, I'll take the instances that I found and append that value to the answer string, and then append the actual value of the instance to the answer string. Sounds confusing, but it is fairly straightforward. To wrap it up, I called the read_aloud function 40 times, like the challenge requires, and pump in the output as the input to repeatedly perform this on the string.

## Part Two
Used the same function as part one, only changing the number of iterations that I had to run on the string.