"""
https://adventofcode.com/2022/day/1
Find the elf carrying the most calories
"""
import os
import requests
import pathlib

# Tried to get via HTTP instead of copying, but need to authenticate via HTTP to get that
# response = requests.get(url="https://adventofcode.com/2022/day/1/input")

# Use input_sample.txt for testing
_fp = os.path.join(pathlib.Path(__file__).parent, "input.txt")
# New-line separated file: '1000\n' or '\n'. Split by \n\n to get each elf's calories
with open(_fp, "r") as f:
    lines = f.read()

elves_food = [list(map(int, elf_cal.split("\n"))) for elf_cal in lines.split("\n\n")]
elves_total_cal = list(map(sum, elves_food))
max_cal = max(elves_total_cal)
print(f"Maximum calories held by a single elf: {max_cal}")

top_3_calories_total = sum(sorted(elves_total_cal, reverse=True)[0:3])
print(f"Total calories held by 3 most calorie-rich elves: {top_3_calories_total}")
