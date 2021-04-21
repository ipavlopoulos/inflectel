class adjectives:
    # Based on the solution of AM296-f3662010
    def __init__(self, lemma, category):
        inflection = []
        masculine = []
        feminine = []
        neutral = []
        inflection.append(masculine)
        inflection.append(feminine)
        inflection.append(neutral)

        # Adjectives belong to categories.
        if category == "a1":
            # Adjectives: -ος, -η, -ο
            masculine.append(lemma + 'ος')
            masculine.append(lemma + 'ου')
            masculine.append(lemma + 'ο')
            masculine.append(lemma + 'ε')
            masculine.append(lemma + 'οι')
            masculine.append(lemma + 'ων')
            masculine.append(lemma + 'ους')
            masculine.append(lemma + 'οι')

            feminine.append(lemma + 'η')
            feminine.append(lemma + 'ης')
            feminine.append(lemma + 'η')
            feminine.append(lemma + 'η')
            feminine.append(lemma + 'ες')
            feminine.append(lemma + 'ων')
            feminine.append(lemma + 'ες')
            feminine.append(lemma + 'ες')

            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'ου')
            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'α')
            neutral.append(lemma + 'ων')
            neutral.append(lemma + 'α')
            neutral.append(lemma + 'α')

        elif category == "a2":
            # Adjectives: -ός, -ή, -ό
            masculine.append(lemma + 'ός')
            masculine.append(lemma + 'ού')
            masculine.append(lemma + 'ό')
            masculine.append(lemma + 'έ')
            masculine.append(lemma + 'οί')
            masculine.append(lemma + 'ών')
            masculine.append(lemma + 'ούς')
            masculine.append(lemma + 'οί')

            feminine.append(lemma + 'ή')
            feminine.append(lemma + 'ής')
            feminine.append(lemma + 'ή')
            feminine.append(lemma + 'ή')
            feminine.append(lemma + 'ές')
            feminine.append(lemma + 'ών')
            feminine.append(lemma + 'ές')
            feminine.append(lemma + 'ές')

            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ού')
            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ά')
            neutral.append(lemma + 'ών')
            neutral.append(lemma + 'ά')
            neutral.append(lemma + 'ά')

        elif category == "b":
            # Adjectives: -ος, -α, -ο
            masculine.append(lemma + 'ος')
            masculine.append(lemma + 'ου')
            masculine.append(lemma + 'ο')
            masculine.append(lemma + 'ε')
            masculine.append(lemma + 'οι')
            masculine.append(lemma + 'ων')
            masculine.append(lemma + 'ους')
            masculine.append(lemma + 'οι')

            feminine.append(lemma + 'α')
            feminine.append(lemma + 'ας')
            feminine.append(lemma + 'α')
            feminine.append(lemma + 'α')
            feminine.append(lemma + 'ες')
            feminine.append(lemma + 'ων')
            feminine.append(lemma + 'ες')
            feminine.append(lemma + 'ες')

            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'ου')
            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'ο')
            neutral.append(lemma + 'α')
            neutral.append(lemma + 'ων')
            neutral.append(lemma + 'α')
            neutral.append(lemma + 'α')

        elif category == "c":
            # Adjectives: -ός, -ιά, -ό
            masculine.append(lemma + 'ός')
            masculine.append(lemma + 'ού')
            masculine.append(lemma + 'ό')
            masculine.append(lemma + 'έ')
            masculine.append(lemma + 'οί')
            masculine.append(lemma + 'ών')
            masculine.append(lemma + 'ούς')
            masculine.append(lemma + 'οί')

            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιάς')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ές')
            feminine.append(lemma + 'ών')
            feminine.append(lemma + 'ές')
            feminine.append(lemma + 'ές')

            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ού')
            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ό')
            neutral.append(lemma + 'ά')
            neutral.append(lemma + 'ών')
            neutral.append(lemma + 'ά')
            neutral.append(lemma + 'ά')

        elif category == "d":
            # Adgectives: -ύς, ιά, -ύ
            masculine.append(lemma + 'ύς')
            masculine.append(lemma + 'ύ' + '/' + lemma + 'ιού')
            masculine.append(lemma + 'ύ')
            masculine.append(lemma + 'ύ')
            masculine.append(lemma + 'ιοί')
            masculine.append(lemma + 'ιών')
            masculine.append(lemma + 'ιούς')
            masculine.append(lemma + 'ιοί')

            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιάς')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιές')
            feminine.append(lemma + 'ιών')
            feminine.append(lemma + 'ιές')
            feminine.append(lemma + 'ιές')

            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'ύ' + '/' + lemma + 'ιού')
            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'ιά')
            neutral.append(lemma + 'ιών')
            neutral.append(lemma + 'ιά')
            neutral.append(lemma + 'ιά')

        elif category == "e":
            # Adjectives: -ύς, -εία, -ύ
            masculine.append(lemma + 'ύς')
            masculine.append(lemma + 'έος')
            masculine.append(lemma + 'ύ')
            masculine.append(lemma + 'ύ')
            masculine.append(lemma + 'είς')
            masculine.append(lemma + 'έων')
            masculine.append(lemma + 'είς')
            masculine.append(lemma + 'είς')

            feminine.append(lemma + 'εία')
            feminine.append(lemma + 'είας')
            feminine.append(lemma + 'εία')
            feminine.append(lemma + 'εία')
            feminine.append(lemma + 'είες')
            feminine.append(lemma + 'ειών')
            feminine.append(lemma + 'είες')
            feminine.append(lemma + 'είες')

            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'έος')
            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'ύ')
            neutral.append(lemma + 'έα')
            neutral.append(lemma + 'έων')
            neutral.append(lemma + 'έα')
            neutral.append(lemma + 'έα')

        elif category == "f":
            # Adjectives: -ής, -ιά, -ί
            masculine.append(lemma + 'ής')
            masculine.append(lemma + 'ή' + '/' + lemma + 'ιού')
            masculine.append(lemma + 'ή')
            masculine.append(lemma + 'ή')
            masculine.append(lemma + 'ιοί')
            masculine.append(lemma + 'ιών')
            masculine.append(lemma + 'ιούς')
            masculine.append(lemma + 'ιοί')

            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιάς')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιά')
            feminine.append(lemma + 'ιές')
            feminine.append(lemma + 'ιών')
            feminine.append(lemma + 'ιές')
            feminine.append(lemma + 'ιές')

            neutral.append(lemma + 'ί')
            neutral.append(lemma + 'ιού')
            neutral.append(lemma + 'ί')
            neutral.append(lemma + 'ί')
            neutral.append(lemma + 'ιά')
            neutral.append(lemma + 'ιών')
            neutral.append(lemma + 'ιά')
            neutral.append(lemma + 'ιά')

        elif category == "g":
            # Adjectives: -ής, -ής, -ές
            masculine.append(lemma + 'ής')
            masculine.append(lemma + 'ούς')
            masculine.append(lemma + 'ή')
            masculine.append(lemma + 'ή')
            masculine.append(lemma + 'είς')
            masculine.append(lemma + 'ών')
            masculine.append(lemma + 'είς')
            masculine.append(lemma + 'είς')

            feminine.append(lemma + 'ής')
            feminine.append(lemma + 'ούς')
            feminine.append(lemma + 'ή')
            feminine.append(lemma + 'ή')
            feminine.append(lemma + 'είς')
            feminine.append(lemma + 'ών')
            feminine.append(lemma + 'είς')
            feminine.append(lemma + 'είς')

            neutral.append(lemma + 'ές')
            neutral.append(lemma + 'ούς')
            neutral.append(lemma + 'ές')
            neutral.append(lemma + 'ές')
            neutral.append(lemma + 'ή')
            neutral.append(lemma + 'ών')
            neutral.append(lemma + 'ή')
            neutral.append(lemma + 'ή')

        elif category == "h":
            # Adjectives: -ης, -α, -ικο
            masculine.append(lemma + 'ης')
            masculine.append(lemma + 'η')
            masculine.append(lemma + 'η')
            masculine.append(lemma + 'η')
            masculine.append(lemma + 'ηδες')
            masculine.append(lemma + 'ηδων')
            masculine.append(lemma + 'ηδες')
            masculine.append(lemma + 'ηδες')

            feminine.append(lemma + 'α')
            feminine.append(lemma + 'ας')
            feminine.append(lemma + 'α')
            feminine.append(lemma + 'α')
            feminine.append(lemma + 'ες')
            feminine.append('-')  # It does not exist.
            feminine.append(lemma + 'ες')
            feminine.append(lemma + 'ες')

            neutral.append(lemma + 'ικο')
            neutral.append(lemma + 'ικου')
            neutral.append(lemma + 'ικο')
            neutral.append(lemma + 'ικο')
            neutral.append(lemma + 'ικα')
            neutral.append(lemma + 'ικων')
            neutral.append(lemma + 'ικα')
            neutral.append(lemma + 'ικα')

        elif category == "i":
            # Adjectives: -ας, -ού, -άδικο/-ούδικο
            masculine.append(lemma + 'άς')
            masculine.append(lemma + 'ά')
            masculine.append(lemma + 'ά')
            masculine.append(lemma + 'ά')
            masculine.append(lemma + 'άδες')
            masculine.append(lemma + 'άδων')
            masculine.append(lemma + 'άδες')
            masculine.append(lemma + 'άδες')

            feminine.append(lemma + 'ού')
            feminine.append(lemma + 'ούς')
            feminine.append(lemma + 'ού')
            feminine.append(lemma + 'ού')
            feminine.append(lemma + 'ούδες')
            feminine.append(lemma + 'ούδων')
            feminine.append(lemma + 'ούδες')
            feminine.append(lemma + 'ούδες')

            neutral.append(lemma + 'άδικο' + '/' + lemma + 'ούδικο')
            neutral.append(lemma + 'άδικου' + '/' + lemma + 'ούδικου')
            neutral.append(lemma + 'άδικο' + '/' + lemma + 'ούδικο')
            neutral.append(lemma + 'άδικο' + '/' + lemma + 'ούδικο')
            neutral.append(lemma + 'άδικα' + '/' + lemma + 'ούδικα')
            neutral.append(lemma + 'άδικων' + '/' + lemma + 'ούδικων')
            neutral.append(lemma + 'άδικα' + '/' + lemma + 'ούδικα')
            neutral.append(lemma + 'άδικα' + '/' + lemma + 'ούδικα')

        elif category == "polis":
            # Irregular Adjective: πολύς, πολλή, πολύ
            masculine.append(lemma + 'ύς')
            masculine.append('(' + lemma + 'λού' + ')')  # Rarely used
            masculine.append(lemma + 'ύ')
            masculine.append('-')  # It does not exist
            masculine.append(lemma + 'λοί')
            masculine.append(lemma + 'λών')
            masculine.append(lemma + 'λούς')
            masculine.append('(' + lemma + 'λοί' + ')')  # Rarely used

            feminine.append(lemma + 'λή')
            feminine.append(lemma + 'λής')
            feminine.append(lemma + 'λή')
            feminine.append('-')  # It does not exist
            feminine.append(lemma + 'λές')
            feminine.append(lemma + 'λών')
            feminine.append(lemma + 'λές')
            feminine.append('(' + lemma + 'λές' + ')')  # Rarely used

            neutral.append(lemma + 'ύ')
            neutral.append('(' + lemma + 'λού' + ')')  # Rarely used
            neutral.append(lemma + 'ύ')
            neutral.append('-')  # It does not exist
            neutral.append(lemma + 'λά')
            neutral.append(lemma + 'λών')
            neutral.append(lemma + 'λά')
            neutral.append('(' + lemma + 'λά' + ')')  # Rarely used
        else:
            print('ERROR: No other POS implemented yet…')
            # There are a few adjective categories remaining.
        return inflection


class verb:

    def __init__(self, lemma, syzigia='A', category="a"):
        self.lemma = lemma
        self.syzigia = syzigia
        self.category = category

    def normal(self, lemma, syzigia, category):
        """
        Based on the solution of AM296-f3662010

        :param lemma:
        :param syzigia:
        :param category:
        :return:
        """
        inflection = []
        if syzigia == "A":
            if category == "a":
                inflection.append(lemma + 'ω')
                inflection.append(lemma + 'εις')
                inflection.append(lemma + 'ει')
                inflection.append(lemma + 'ουμε')
                inflection.append(lemma + 'ετε')
                inflection.append(lemma + 'ουν' + '/' + lemma + 'ουνε')
            else:
                print('ERROR: No other category exists.')
        elif syzigia == "B":
            if category == "a":
                inflection.append(lemma + 'άω' + '/' + lemma + 'ώ')
                inflection.append(lemma + 'άς')
                inflection.append(lemma + 'άει' + '/' + lemma + 'ά')
                inflection.append(lemma + 'άμε' + '/' + lemma + 'ούμε')
                inflection.append(lemma + 'άτε')
                inflection.append(lemma + 'άν' + '/' + lemma + 'ούν')
            elif category == "b":
                inflection.append(lemma + 'ώ')
                inflection.append(lemma + 'είς')
                inflection.append(lemma + 'εί')
                inflection.append(lemma + 'ούμε')
                inflection.append(lemma + 'είτε')
                inflection.append(lemma + 'ούν' + '/' + lemma + 'ούνε')
            else:
                print('ERROR: No other category exists.')
        else:
            # irregular verbs(syzigia=="irregular")
            inflection.append(lemma + 'ω')
            inflection.append(lemma + 'ς')
            inflection.append(lemma + 'ει')
            inflection.append(lemma + 'με')
            inflection.append(lemma + 'τε')
            inflection.append(lemma + 'νε')

        return inflection


    def idioklita(self, lemma):
        """
        Based on the solution of AM296-f3662009
        :param lemma:
        :return:
        """
        inflection = []
        inflection.append(lemma + "ω")
        inflection.append(lemma + "ς")
        inflection.append(lemma + "ει")
        inflection.append(lemma + "με")
        inflection.append(lemma + "τε")
        inflection.append(lemma + "νε")
        return inflection
