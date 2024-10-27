# [2015 - Day 15 (Link)](https://adventofcode.com/2015/day/15)

## Part One
This was another fun one. I've been busy with other projects, but was able to get this one done in about an hour. Ended up repurposing some code from Day 11, where I cycled through all possible passwords to find the next valid one. Tweaked that code so that it would cycle through all values between 1 and however many servings of whatever ingredient we could fit to fully use however many servings we were allotted. Tough one, but not too bad.

## Part Two
Added an extra argument to my functions to clarify whether or not it was part one or part two. Not a huge fan of that, but it seemed cleaner than basically copying and pasting utility functions that would be nearly identical. For maintainability / readability, I think what I did is still the best way to go.