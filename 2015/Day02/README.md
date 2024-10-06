# 2015 - Day 02

## Part One
Not much was involed with this one. I ended up just interating throw each row of dimensions, splitting as the 'x' and then applying the math to get the value they needed. Most difficult part was determining the smallest value in the dimensions, but ended up just iterating through them and keeping a variable that would hold on to the smallest one.

## Part Two
Same kind of thing as step one, but changed the logic a bit since I need the two smallest dimensions, not just one. To do that I used python's sorted function to order the array, then used the first two indices to do the remaining math.