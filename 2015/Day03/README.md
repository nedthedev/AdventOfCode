# [2015 - Day 03 (Link)](https://adventofcode.com/2015/day/3)

## Part One
This one was fairly easy. All I did was step through each instruction, update the current x and y location based on the instruction and insert the coordinates into a dictionary. I check for the coordinates existing in my dictionary, if it's there I increment it to keep track of the presents delivered there, if it's not there I create it.

## Part Two
Bit more tricky, but ended up going the route of keeping two different x and y values, one for robo santa and one for real santa, and updating a shared dictionary same as I did in part one. Could have gone the route of two separate dictionaries as well, but that seems like it would overcomplicate the code for what was being asked.