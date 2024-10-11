# [2015 - Day 05 (Link)](https://adventofcode.com/2015/day/5)

## Part One
An easy one still. I went the route of building designated functions for each qualifier. This made it easy to test whether or not the logic for these conditions are working as intended. Then the only thing I need to do is apply all of the checking functions, if they're true then increment the counter for how many nice strings there are.

## Part Two
Really this was the same thing as part two, but I had to build a couple of additional functions to check for the given conditions. Python makes it easy for the double instances checker. I ended up looking for n and n+1 being the same character. If they are, I then use Python's nifty array utilities to check the rest of the string from n to look for the same pair elsewhere in the string. Spcefically, I did <code>if(string[i:i+2] in string[i+2:])</code> which made that check very easy, but I had initially thought this one would be a bit tough.