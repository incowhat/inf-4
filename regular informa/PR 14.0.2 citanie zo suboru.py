with open('PR 14.0.1 zapis.txt', 'r') as r:
    with open('PR 14.0.2 citanie.txt', 'w') as f:
        f.write('toto je napisane v predoslom subore "zapis":''\n\n')
        f.write(r.read())
