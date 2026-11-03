from docx import Document
import re
import json



my_list_crypt = []

for i in range(0, 5000):
    new_fake_name = 'X000'
    my_list_crypt.append(new_fake_name + str(i))
def encryption(file_name, output_file):
    '''Функция получает на вход файл для шифровки и название файла на выход.
    Зашифровывает docx-файл, меняет типовые названия установок на стандартные типа X0001.
    Создает новый файл на выходе (new_file) и словарик соответствий в формате json (dict_crypt.json).
    '''
    dict_crypt = {}
    next_number = 0
    document = Document(file_name)
    pattern = r"(?<!\w)1-[\w/,]*\w+(?!\w)"

    def replace_name(match):
        nonlocal next_number
        original_name =  match.group(0)
        if original_name not in dict_crypt:
            if next_number >= len(my_list_crypt):
                raise ValueError
            dict_crypt[original_name] = my_list_crypt[next_number]
            next_number += 1
        return dict_crypt[original_name]

    for paragraph in document.paragraphs:
        paragraph.text = re.sub(
            pattern,
            replace_name,
            paragraph.text,
        )

    document.save(output_file)
    with open("dict_crypt.json", "w", encoding="utf-8") as file:
        json.dump(
            dict_crypt,
            file,
            ensure_ascii=False,
            indent=4,
        )
    return dict_crypt
def decryption(file_name, output_file, dict_file):
    #Эта функция получает на вход зашифрованный файл, название файла,
    #который должен вернуться в результате
    #и json, в котором словарик соответствий.
    #Расшифровывает файл, возвращает обратно названия.
    document = Document(file_name)

    with open(dict_file, "r", encoding="utf-8") as file:
        dict_crypt = json.load(file)

    reverse_dict = {
        fake_name: original_name
        for original_name, fake_name in dict_crypt.items()
    }

    pattern = r"X\d{4,6}"

    def replace_name(match):
        fake_name = match.group(0)
        return reverse_dict.get(fake_name, fake_name)

    for paragraph in document.paragraphs:
        paragraph.text = re.sub(
            pattern,
            replace_name,
            paragraph.text
        )

    document.save(output_file)



if __name__=="__main__":
    '''encryption('test_file.docx', "new_file.docx")'''
    '''decryption(
        "new_file.docx",
        "back_file.docx",
        "dict_crypt.json"
    )'''





