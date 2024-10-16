# [2015 - Day 12 (Link)](https://adventofcode.com/2015/day/12)

## Part One
This one proved to be suprisingly difficult. Had thought about going at it in JavaScript, since that seemed logical, but ended up sticking with Python. The initial part one wasn't so tough, and you could also go about it where you treat the input as a string instead and run a regex to pull all of the ints out the list. I didn't do that, but I'd be lying if I said I didn't think about it :) Ended up treating the data as a list of dictionaries though, not JSON. This made it easy to recursively call on all subdata without having to add any extra imports to handle JSON data as true JSON within Python. After iterating to the lowest level of all the data the function just sums up all values that are integers.

## Part Two
Definitely more difficult than part one, but ended up being not too bad. Ended up being able to check for red being in the data and from there I just skipped any additional parsing for that data and any subdata.