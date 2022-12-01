input_content = []
with open("input.txt") as f:
    f = map(lambda s: s.strip("\n"), f)
    for i in f:
        input_content.append(i)

one_elf_sum = 0;
summed_list = []
for x in input_content:
    if x == "":
        summed_list.append(one_elf_sum)
        one_elf_sum = 0
    else:
        one_elf_sum += int(x)

summed_list.sort(reverse=True)
print(summed_list[0])

# Part Two

total = 0
for y in range(3):
    total += summed_list[y]
print(total)