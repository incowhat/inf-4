url = input('URL: ').split('/')

print(f'protokol: {url[0][:-1]}')
print(f'domenova adresa servera: {url[2]}')
print(f'domena najvystej urovne: {url[2].split(".")[-1]}')