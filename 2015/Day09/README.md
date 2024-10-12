# [2015 - Day 09 (Link)](https://adventofcode.com/2015/day/9)

## Part One
Oof, struggled on this one for far too long. Recursion can be a tricky thing to wrap your head around, but it makes it really hard when you're consistently returning your value and not doing the proper checks... This was one of those cases where I should've just stopped and picked the code back up later. I did do that, but I should've done it sooner. I had a really broken depth first search function that I wrote, but it wasn't comparing values, just blindly returning them, which doesn't help what I was trying to achieve. Tried for a really long time to get it to work, but ended up leaving it, coming back and writing a new funciton, and just like that I had the code done. Depth first searches are fun to implement, is there a more efficient way I could've done this? Probably, but it works.

## Part Two
Ended up just adding an argument to my functions to determine whether or not to get the shortest path or to get the longest path. Logic to find the shortest route worked just fine with a couple of additional checks to see if instead we want to get the longest route through all the locations.