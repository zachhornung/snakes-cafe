TOTAL_WIDTH = 38
HEADER = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""
FOOTER = """
***********************************
** What would you like to order? **
***********************************
"""
menu = {
    "Appetizers": ['Wings', 'Cookies', 'Spring Rolls'], 
    "Entrees": ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    "Desserts": ['Ice Cream', 'Cake', 'Pie'],
    "Drinks": ['Coffee', 'Tea', 'Unicorn Tears']
    }
def create_menu_sections(menu):
    menu_string = ''
    for section_header in menu:
        menu_string+=f'{section_header}\n' + '-'*len(section_header)+'\n'
        for menu_item in menu[section_header]:
            menu_string+=f'{menu_item}\n'
        menu_string+='\n'
    return menu_string
def print_order_confirmation_message(response, order):
    print(f'** {order[response]} order of {response} have been added to your meal **\n')
created_menu = create_menu_sections(menu)
print(f"{HEADER}\n{created_menu}{FOOTER}")
running = True
order = {}
while running:
    response = input('> ')
    if response == 'quit':
        full_order = ''
        if order:
            for item in order:
                full_order+=f'{order[item]} {item}, '
        print(f'Your order is: {full_order}')
        print('Have a great day!')
        running = False
    elif response in order:
        order[response]+=1
        print_order_confirmation_message(response, order)
    else:
        order[response] = 1
        print_order_confirmation_message(response, order)