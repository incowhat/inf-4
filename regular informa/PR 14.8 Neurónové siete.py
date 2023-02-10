with open('PR 14.8.1 neuronova_siet.txt', 'r+', encoding='utf-8') as file:
    output = '.\n'.join(file.read().split('. '))
    output = '\n'.join(f'({i:02}) {j}' for i, j in enumerate(output.split('.\n'), 1))

    print(output)
    file.write('\n\n' + output)