import re


def email_address_generator(file: str):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()
        for email in re.finditer(email_regex, content):
            yield email.group()


def copy_emails_to_file(input_file: str, output_file: str):
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for email in email_address_generator(input_file):
            output_file.write(email + '\n')


input_file_path = '../email.txt'
output_file_path = '../email_new.txt'

copy_emails_to_file(input_file_path, output_file_path)