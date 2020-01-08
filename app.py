import itertools
import pandas as pd
from turing.file import file_upload


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

        sun = 0
        success = False

        for i in range(0, len(values) + 1):
            for subset in itertools.combinations(values, i):
                high_value = True
                for j in subset:
                    sun = sun + j
                    if sun > reward:
                        high_value = False
                        sun = 0
                        break
                    elif sun == reward:
                        success = True
                        break

                if high_value:
                    df = df.append({'Valores': subset, 'Soma': sun}, ignore_index=True)
                    sun = 0

                if success:
                    break

            if success:
                break

        df.sort_values(by=['Soma'], ascending=False, inplace=True)
        print(reward)
        print(df)

