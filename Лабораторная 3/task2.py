def find_common_participants(fam1,fam2, comma=","):
    split_fam1 = fam1.split(comma)
    split_fam2 = fam2.split(comma)

    set_fam1 = set(split_fam1)
    set_fam2 = set(split_fam2)
    combined_fam = list((set_fam1).intersection(set_fam2))
    combined_fam.sort()
    return combined_fam


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
