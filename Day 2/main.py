input_content = []
with open("input.txt") as f:
    f = map(lambda s: s.strip("\n"), f)
    for i in f:
        input_content.append(i)

for i in input_content:
            