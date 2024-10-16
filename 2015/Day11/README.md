# [2015 - Day 11 (Link)](https://adventofcode.com/2015/day/11)

## Part One
Pretty fun puzzle! Wasn't too difficult to get a function and a bunch of helper functions to determine whether or not a password was valid. The more challenging part was figuring out the cycling through passwords. I ended up checking if the last character in the password was a 'z', then recursively going up the string as long as the 'z's continued and cycling them to 'a's. Ended up working perfectly.

## Part Two
For part two, I ended up just pumping in the output of part one to the cycle function that I had created for part one and it gave me the next valid password no issue.