def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def print_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')


def copy_contact():
    print_contacts()
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split('\n\n')
        new_contacts_list = []
        for nn, contact in enumerate(contacts_list, 1):
            contact = f'{nn}. {contact}'
            new_contacts_list.append(contact)
    num_contact = int(input("Введите номер контакта для копирования: "))
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contact_str = new_contacts_list[0]
        for i in range(len(new_contacts_list)):
            if f'{num_contact}.' in new_contacts_list[i]:
                with open('newphonebook.txt', 'a', encoding='utf-8') as file:
                    file.write(new_contacts_list[i])
                    print("\n Контакт скопирован! \n")

def search_contact(field=""):
    print(
            "Возможные варианты поиска:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По номеру\n"
            "5. По городу\n"
        )

    index_var = int(input("Введите вариант поиска: ")) -1

    search = input("Введите данные для поиска: ")

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()

    contacs_list = contacts_str.rstrip().split('\n\n')

    for contact_str in contacs_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')
def interface():
    with open("phonebook.txt", "a"):
        pass

    user_input = None
    while user_input != "5":
        print(
            "Возможные варианты действия:\n"
            "1. Добавить контакт\n"
            "2. Вывод списка контактов\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Выход из программы\n"
        )

        user_input = input("Введите вариант: ")

        while user_input not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод.")
            user_input = input("Введите вариант: ")

        print()

        match user_input:
            case "1":
                write_contact()
            case "2":
                print_contacts()
            case "3":
                search_contact()
            case "4":
                copy_contact()
        print()


if __name__ == "__main__":
    interface()