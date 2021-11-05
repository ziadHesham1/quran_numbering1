rf = open('names.txt', encoding="utf8")
wf = open('names_with_numbers.txt', 'w', encoding="utf8")
file_lines = rf.readlines() * 3
rf.close()
intList = list(range(1, len(file_lines * 3)))
dictionary = dict(zip(intList, file_lines))

readers = ["ahmed_alnufais", "hatem farid", "Nabil-Ar-Rifai"]
c = 0
print(type(dictionary))
for k, v in dictionary.items():
    wf.writelines(str(k) + " - " + v)
    c += 1
    if c % 114 == 0 and (c / 114) < 0:
        reader_name = "----------- " + readers[int((c / 114) - 1)] + " ----------- "
        wf.writelines(reader_name)

wf.close()
