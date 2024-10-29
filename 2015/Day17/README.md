# [2015 - Day 17 (Link)](https://adventofcode.com/2015/day/17)

## Part One
I spent a good amount of time thinking about the best approach to this one. I ended up really liking how I went about it. What I did, was find every possible combination of containers by doing 2^(length of containers), then stepping through that range and converting the integer to binary to get a string representation of 1 or 0, for whether or not we use the container or not. If, when stepping through the binary, the value is 1, then add that container to the sum. If by the end of the iterating the sum is the same as the volume of eggnog then we know it's a valid combination.

## Part Two
Used the same logic as part one, but it was a matter of finding the combination that required the fewest number of containers. Not too bad, same iterating, just a matter of keeping an additional variable that would monitor whether or not the number of containers is a new minimum or if it matches the current minimum.