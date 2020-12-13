
def get_bank():
    """отримує данні по банкам

    Returns:
        bank_list : список банків
    """

    from_file = [
     "110;ІНКО",
     "120;АЖІО",
     "130;Градобанк",
     "140;Відродження",
     "150;Укрінбанк",
    ]

    # накопичувач рядків
    bank_list = []

    for line in from_file:
        line_list = line.split(';')
        bank_list.append(line_list)

    return bank_list




def get_kyrs():
    """отримує данні по банкам

    Returns:
        bank_list : список банків
    """

    from_file = [
     "110;4,5;5,4;6,3;3,4;3,45;4;2003",
     "120;4;5;7,5;2,7;3,4;4,78;2003",
     "130;3,9;5,1;8;2,74;3,32;5,3;2003",
     "140;4,2;5;7;2,459;3,252;4,8;2003",
     "150;4,5;5,1;7,7;3,169;3,312;4,8;2003",
     "110;6,5;6,8;7;4,5;4,7;4,8;2004",
     "120;7,9;8;8,1;5,1;5,2;5,3;2004",
     "130;8,25;8,33;8,5;5,3;5,34;5,38;2004",
     "140;8,27;8,3;8,52;5,28;5,3;5,35;2004",
     "150;8,3;8,31;8,5;5,28;5,3;5,35;2004",
     "110;8,1;8,4;9;5,1;5,11;5,2;2005",
     "120;8,2;8,35;8,55;5,4;5,48;5,5;2005",
     "130;8,7;8,78;8,82;5,45;5,5;5,55;2005",
     "140;8,68;8,8;8,85;5,46;5,5;5,55;2005",
     "150;8,65;8,8;8,84;5,46;5,52;5,56;2005",
    ]

    # накопичувач рядків
    bank_list = []

    for line in from_file:
        line_list = line.split(';')
        bank_list.append(line_list)

    return bank_list

def show_bank(bank):
    
    bank_code_from = input("З якого кода банк?")
    bank_code_to = input("По який код банк?")
    for bank in bank:
        if bank_code_from <= bank[0] <= bank_code_to:
            print("код: {:5} назва {:10}".format(bank[0], bank[1]))


bank = get_bank()
show_bank(bank)

def show_kyrs(kyrs):
    """виводить список банків зв заданої умови

    Args:
        bank :  список банків
    """
    kyrs_code_from = input("з якого кода банк?")
    kyrs_code_to = input("по який код банк?")
    for kyrs in kyrs:
        if kyrs_code_from <= kyrs[0] <= kyrs_code_to:
            print("код: {:5} Січень/Лютий = {:10} Березень/Квітень = {:10} Травень/червень = {:10} Липень/Серпень = {:10} Вересень/Жовтень = {:10} Листопад/Грудень = {:5} рік - {:6} ".format(kyrs[0], kyrs[1], kyrs[2], kyrs[3], kyrs[4], kyrs[5], kyrs[6], kyrs[7]))


kyrs = get_kyrs()
show_kyrs(kyrs)
