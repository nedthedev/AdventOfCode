# [2015 - Day 13 (Link)](https://adventofcode.com/2015/day/13)

## Part One
I feel pretty good about how I went about this one. I ended up repurposing my algorithm from a few days ago. I ended up taking my algorithm that I used for the optimal route challenge and redesigning it slightly to account for the "doubly linked" and cyclical twist on what I'd already made. Ended up saving me some time, but I ended up taking a little too long to figure out that I hadn't accounted for the 'loss' vs 'gain' keyword in the problem input... oh well. After I noticed that and fixed how I was parsing the data that algorithm worked as intended.

## Part Two
Ended up just using part one, but added a little bit of logic to add myself to the table with a net gain of 0 for myself and everybody else.
