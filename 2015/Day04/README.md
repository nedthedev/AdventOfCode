# 2015 - Day 04

## Part One
This one wasn't as tricky as I had initially thought it might be. Fortunately, Python has a nifty integrated utility to allow getting hashes. I had to read up on the documentation for how the library worked, but once I did that I was able to simply brute-force through all possibilities to find the md5 hash that started with 5 zeros. Not sure if there's a better way to go about this one without brute-force, but it was done quickly enough.

## Part Two
Same thing as part one, but an additional zero. I ended up just changing the part one function to search for a variable amount of leading zeros. After I did that, I simply called part_one function from part_two function with the different arguments and it worked perfectly.