#!/usr/bin/sh

# Generate every year's days and build a main.py with shebang and mark is as executable

pwd=$(pwd)

for year in {2015..2024}
do 
  for day in {01..25}
  do 
    day="${pwd}/${year}/Day_${day}"
    mkdir -p $day
    printf "#!/usr/bin/python3\n\nif __name__ == \"__main__\":\n\tprint(\"Hi :)\")" >> "${day}/main.py"
    chmod +x "${day}/main.py"
  done
done
