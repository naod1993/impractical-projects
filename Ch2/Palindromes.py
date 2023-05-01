import load_dictionary

word_list = load_dictionary.load_file('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word[:] == word[::-1]:
        pali_list.append(word)
        print(word)

print("\nNumber of palindromes found is {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')


