#!/usr/bin/sh

# Generate every year's days and build a main.py with shebang and mark is as executable

pwd=$(pwd)

for i in $(ls -d */) 
do 
  for day in {01..25}
  do 
    day="${pwd}/${i}Day_${day}"
    mkdir $day
    echo "#!/usr/bin/python3" >> "${day}/main.py"
    chmod +x "${day}/main.py"
  done
done
