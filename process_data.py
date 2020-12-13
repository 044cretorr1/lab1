""" формування заявок на устаткування по магазину
"""

from data_service import get_bank, get_kyrs


# структура рядка вихідних даних
zajavka = {
    
    'bank_code'    : 0,     # kod banky
    'bank_name'    : '',     # nazva banky
    'year'         : 0,     # rik kyrsy
    'dollars'      : 0.00,      # dolary
    'marks'        : 0.00,    # marky
}

banks = get_bank()
kyrss = get_kyrs()

# накопичувач заявок
zajavka_list = []

def create_zajavka_list():  
    """[summary]
    """
    
    def get_bank_name(bank_code):
        """повертає назву bank по його коду

        Args:
            bank_code ([type]): код bank

        Returns:
            [type]: назва bank
        """
        for bank in banks:
            if bank_code == bank[0]:
                return bank[1]
            
        return "*** назва не знайдена"
            
     
    # накопичувач заявок
    zajavka_list = []

    for kyrs in kyrss:
        
        # створити робочу копію
        zajavka_work = zajavka.copy()
        
        zajavka_work['year']          = kyrs[7]
        zajavka_work['dollars']       = kyrs[1],kyrs[2],kyrs[3]
        zajavka_work['marks']         = kyrs[4], kyrs[5], kyrs[6]
        zajavka_work['bank_code']     = kyrs[0]

        
        zajavka_list.append(zajavka_work)
        
    return zajavka_list
        

z = create_zajavka_list()
for i in z:
    print(i)