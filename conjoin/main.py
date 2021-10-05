import os
from pathlib import Path

path = os.getcwd()
directory = [f for f in os.listdir(path) if f.endswith('.txt')]
def get_size_doc(file_name):
    document_size = {}
    for name in file_name:
        with open(f'{name}', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip() != '']
        document_size[name] = len(lines)
    sorted_document = {}
    sorted_doc = sorted(document_size, key=document_size.get)
    for w in sorted_doc:
        sorted_document[w] = document_size[w]
    return sorted_document


def create_new_file(name_file):
    with open(f'{name_file}', 'w+', encoding='utf-8') as file:
       file.write('')

create_new_file('New File.txt')

def write_new_file(file):
    dict_ = get_size_doc(directory)
    list_key = []
    list_value = []
    for key, value in dict_.items():
        list_key.append(key)
        list_value.append(value)
    for i in range(len(list_key)):
        with open(f'{list_key[0]}', 'a', encoding='utf-8') as second, open(f'{list_key[i+1]}', encoding='utf-8') as first:
            data = first.read()
            second.write(f'{list_key[i+1]}\n')
            second.write(f'{list_value[i+1]}\n')
            second.write(f'{data}\n')
            second.write('\n')

write_new_file(create_new_file('New File.txt'))