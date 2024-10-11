# [2015 - Day 06 (Link)](https://adventofcode.com/2015/day/6)

## Part One
This one was a bit more tough. There has to be a better way to go about it than how I did. I ended up going the straight forward route of creating a 999x999 2D array. It's definitely the most obvious way to go about this problem, but it very inefficient. With that, I made specific functions for each type of instruction, toggle and turn. Toggle I'd just swap the power to whatever it wasn't, and power on / off would just set it to whatever it's been told. There was no real issues with this one.
## Part Two
This one was a bit more tricky, although mostly because I decided to use all of the same functions that I had used for part one. This required me adding an additional argument to each utility function and changing some logic within to handle this additional variable. It worked fine, and didn't interrupt the functionality of part one, but it did make the code a bit more difficult to understand/maintain.