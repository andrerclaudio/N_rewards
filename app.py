import itertools

import pandas as pd

from turing.file import file_upload
from string import whitespace

def application():

    while True:
        reward = int(input('Valor do rewards para resgatar:      '))
        content = file_upload()

        if content is False or reward == 0:
            break

        df = pd.DataFrame(columns=['Valores', 'Soma'])
        values = []
        number = ''

        for character in content:
            if character == '\n':
                values.append(int(number))
                number = ''
            else:
                number = number + character

        if number != '':
            values.append(int(number))

        soma = 0

        for i in range(0, len(values) + 1):
            for subset in itertools.combinations(values, i):
                high_value = True
                for j in subset:
                    soma = soma + j
                    if soma > reward:
                        high_value = False
                        soma = 0
                        break

                if high_value:
                    df = df.append({'Valores': subset, 'Soma': soma}, ignore_index=True)
                    soma = 0

        df.sort_values(by=['Soma'], ascending=False, inplace=True)
        print(reward)
        print(df)

