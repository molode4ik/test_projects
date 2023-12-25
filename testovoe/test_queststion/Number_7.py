from faker import Faker
import time
import re


def email_address_generator(file: str):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()
        for email in re.finditer(email_regex, content):
            yield email.group()


def add_emails_to_file(filename: str, num_emails: int):
    fake = Faker()
    with open(filename, 'a') as file:
        for _ in range(num_emails):
            email = fake.email()
            file.write(email + '\n')


def timeit(N: float):
    def decorator(func):
        def wrapper(*args):
            time_start = time.time()
            result = func(*args)
            end_time = time.time()
            if end_time - time_start > N:
                print("Время выполнения превышает нужное нам время")
            return result
        return wrapper
    return decorator


@timeit(0.05)
def copy_emails_to_file(input_file: str, output_file: str):
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for email in email_address_generator(input_file):
            output_file.write(email + '\n')


if __name__ == '__main__':
    add_emails_to_file("email.txt", 100_000)
    copy_emails_to_file("../email.txt", "../email_new.txt")