"""головний модуль додатку
виводить розрахункову талицю, зберігає результати в файл
показу на екрані первинні дані
"""

from os import system
from process_data import create_zajavka_list
from data_service import show_banks, show_kyrs, get_banks, get_kyrs

MAIN_MENU = \
"""
~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА УСТАТКУВАННЯ ~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
---------------------------
"""

STOP_MESSAGE = 'Для продовження нажмить <Enter>'

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
=====================================================================================
   Устаткування     |  Клієнт         | Номер заказа | Кількість | Ціна   |  Сума      
=====================================================================================  
"""

FOOTER =  \
"""
=====================================================================================  
"""

def show_table_on_screen(zajavka_list):
    """вивід таблиці заявок на екран

    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n{TITLE:^86}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['oborud_name']:20}",     \
              f"{zajavka['client_name']:20}",     \
              f"{zajavka['order_number']:^10}",   \
              f"{zajavka['kol']:>10}",            \
              f"{zajavka['price']:>10.2f}",       \
              f"{zajavka['total']:>10.2f}"            
              ) 
    
    print(FOOTER)


def write_zajavka(zajavka_list):
    """записує масив заявок в файл

    Args:
        zajavka_list ([type]): список заявок
    """