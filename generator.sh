#!/usr/bin/sh

# Generate every year's days and build a main.py with shebang and mark is as executable

pwd=$(pwd)

for year in {2015..2024}
do 
  for day in {01..25}
  do 
    # Create the directory and ensure all parents folders exist
    dir="${pwd}/${year}/Day${day}"
    mkdir -p $dir

    # Create the main Python file and main function within
    printf "#!/usr/bin/python3\n\nDATA = \"\"\"\"\"\"\n\ndef part_one(data):\n\tpass\n\ndef part_two(data):\n\tpass\n\nif __name__ == \"__main__\":\n\tprint(\"Hi :)\")" >> "${dir}/main.py"

    # Ensure you're able to execute the script
    chmod +x "${dir}/main.py"

    # The Advent of Code link needs to be single digit number
    day_single=$(expr $day + 0)
 
    # Generates a README where I can notate my thought process, things I learned, hurdles I encountered
    printf "# [${year} - Day ${day} (Link)](https://adventofcode.com/${year}/day/${day_single})\n\n## Part One\n\n## Part Two\n" >> "${dir}/README.md"
  done
done
