# [2015 - Day 01 (Link)](https://adventofcode.com/2015/day/1)

## Part One
Pretty straight forward puzzle. I had a couple of plans to approach it, but I ended up simply stepping through each character in the input and increasing or decreasing a variable to keep track of the current 'floor' santa was on. Worked as expected.

## Part Two
Part two was also fairly straight forward. My approach to store a variable to keep track of his current floor, everytime santa would go down a floor I'd check the current state of the variable. If it was negative, I'd return how far into the string I was, which was easy by using Python's enumerate in the for loop. Only issue I had was that I needed to +1 the return value to get how far into the string we had actually gone, since enumerate will start at 0.