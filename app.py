from turing.file import file_upload
import stackoverflow
import hetland
import wikipedia


def application():

    while True:
        reward = int(input('Valor do rewards para resgatar:      '))
        content = file_upload()

        if content is False or reward == 0:
            break

        number = ''
        values = []

        for character in content:
            if character == '\n':
                values.append(int(number))
                number = ''
            else:
                number = number + character

        if number != '':
            values.append(int(number))

        break

    so = stackoverflow.stackoverflow(values, reward)
    he = hetland.bb_knapsack(values, reward)
    wi = wikipedia.approx_with_accounting_and_duplicates(values, reward)

    print('Stackoverflow:', so)
    print('Hetland:', he)
    print('Wikipedia:', wi)
