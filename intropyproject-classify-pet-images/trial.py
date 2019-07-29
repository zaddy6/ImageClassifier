from os import listdir

fileName = listdir("pet_images")

pet_labels = []


for files in fileName:

    lower_pet_name = files.lower()
    pet_name_list = lower_pet_name.split('_')
    pet = ""
    for name in pet_name_list:
        if name.isalpha():
            pet += name + " "
            pet_labels.append(pet)

pet_labels = [name.strip() for name in pet_labels]


result_dict = dict()


# print(pet_labels)

for idx in range(0, len(fileName), 1):
    if fileName[idx] not in result_dict:
        result_dict[fileName[idx]] = [pet_labels[idx]]
    else:
        print("**Warning: Key=", fileName[idx], "already exist in result dict with Value=", result_dict[fileName[idx]])


for key in result_dict:
    print("Filename", key, " Pet label=", result_dict[key][0])



