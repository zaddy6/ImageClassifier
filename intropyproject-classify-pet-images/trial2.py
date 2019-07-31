dognames_dic = dict()

dogfile = 'dognames.txt'

with open(dogfile) as file:
    # line = file.readline()
    for line in file:
        dognames_dic[line.strip()] = 1

nmx = 'maltese'

# if nmx in dognames_dic.keys():
#     # print('yassss')

# print(dognames_dic['chihuahua'])
# print(dognames_dic.items())


dTest = {
    'maltise': ['car', 'house', 2]
}
# print(dTest['maltise'][1])

for key in dTest:
    dTest[key].extend((1))

print(dTest.items())
