x= input("In which category does the lemma ,that you will entry, belong? Please input 'A' for verb or 'B' for adjective: ")

if x == 'A' :
  lemma= input("Please input the thema of the word, ex: for word : 'κλίνω' input 'κλιν-' : ") 
  syzigia= input("In which conjuction does the verb belong? Please input 'A' or 'B' or 'Irregular Verb' or 'Contracting Verb': ")
  category= input("In which category does the verb belong? Please input 'a' or 'b' : ") 
elif x == 'B' : 
  lemma_adj= input("Please input the thema of the word, ex: for word : 'καλός' input 'καλ' : ") 
  category_adj= input("In which category does the adjective belong? \n Please input: \n 'a1' for adjectives -ος, -η, -ο \n 'a2' for -ός, -ή, -ό \n 'b' for -ος, -α, -ο \n 'c' for -ός, -ιά, -ό \n 'd' for -ύς, ιά, -ύ \n 'e' for -ύς, -εία, -ύ \n 'f' for -ής, -ιά, -ί \n 'g' for -ής, -ής, -ές \n 'h' for -ης, -α, -ικο \n 'i' for -ας, -ού, -άδικο/-ούδικο \n 'polis' for irregular adjective πολύς, πολλή, πολύ   ")
else:
  print('No other categories implemented yet.')

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



inflection=[]
if category_adj == "a1":
            # Adjectives: -ος, -η, -ο
            masculine.append(lemma_adj + 'ος')
            masculine.append(lemma_adj + 'ου')
            masculine.append(lemma_adj + 'ο')
            masculine.append(lemma_adj + 'ε')
            masculine.append(lemma_adj + 'οι')
            masculine.append(lemma_adj + 'ων')
            masculine.append(lemma_adj + 'ους')
            masculine.append(lemma_adj + 'οι')

            feminine.append(lemma_adj + 'η')
            feminine.append(lemma_adj + 'ης')
            feminine.append(lemma_adj + 'η')
            feminine.append(lemma_adj + 'η')
            feminine.append(lemma_adj + 'ες')
            feminine.append(lemma_adj + 'ων')
            feminine.append(lemma_adj + 'ες')
            feminine.append(lemma_adj + 'ες')

            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'ου')
            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'α')
            neutral.append(lemma_adj + 'ων')
            neutral.append(lemma_adj + 'α')
            neutral.append(lemma_adj + 'α')

elif category_adj == "a2":
            # Adjectives: -ός, -ή, -ό
            masculine.append(lemma_adj + 'ός')
            masculine.append(lemma_adj + 'ού')
            masculine.append(lemma_adj + 'ό')
            masculine.append(lemma_adj + 'έ')
            masculine.append(lemma_adj + 'οί')
            masculine.append(lemma_adj + 'ών')
            masculine.append(lemma_adj + 'ούς')
            masculine.append(lemma_adj + 'οί')

            feminine.append(lemma_adj + 'ή')
            feminine.append(lemma_adj + 'ής')
            feminine.append(lemma_adj + 'ή')
            feminine.append(lemma_adj + 'ή')
            feminine.append(lemma_adj + 'ές')
            feminine.append(lemma_adj + 'ών')
            feminine.append(lemma_adj + 'ές')
            feminine.append(lemma_adj + 'ές')

            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ού')
            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ά')
            neutral.append(lemma_adj + 'ών')
            neutral.append(lemma_adj + 'ά')
            neutral.append(lemma_adj + 'ά')

elif category_adj == "b":
            # Adjectives: -ος, -α, -ο
            masculine.append(lemma_adj + 'ος')
            masculine.append(lemma_adj + 'ου')
            masculine.append(lemma_adj + 'ο')
            masculine.append(lemma_adj + 'ε')
            masculine.append(lemma_adj + 'οι')
            masculine.append(lemma_adj + 'ων')
            masculine.append(lemma_adj + 'ους')
            masculine.append(lemma_adj + 'οι')

            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'ας')
            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'ες')
            feminine.append(lemma_adj + 'ων')
            feminine.append(lemma_adj + 'ες')
            feminine.append(lemma_adj + 'ες')

            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'ου')
            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'ο')
            neutral.append(lemma_adj + 'α')
            neutral.append(lemma_adj + 'ων')
            neutral.append(lemma_adj + 'α')
            neutral.append(lemma_adj + 'α')

elif category_adj == "c":
            # Adjectives: -ός, -ιά, -ό
            masculine.append(lemma_adj + 'ός')
            masculine.append(lemma_adj + 'ού')
            masculine.append(lemma_adj + 'ό')
            masculine.append(lemma_adj + 'έ')
            masculine.append(lemma_adj + 'οί')
            masculine.append(lemma_adj + 'ών')
            masculine.append(lemma_adj + 'ούς')
            masculine.append(lemma_adj + 'οί')

            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιάς')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ές')
            feminine.append(lemma_adj + 'ών')
            feminine.append(lemma_adj + 'ές')
            feminine.append(lemma_adj + 'ές')

            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ού')
            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ό')
            neutral.append(lemma_adj + 'ά')
            neutral.append(lemma_adj + 'ών')
            neutral.append(lemma_adj + 'ά')
            neutral.append(lemma_adj + 'ά')

elif category_adj == "d":
            # Adgectives: -ύς, ιά, -ύ
            masculine.append(lemma_adj + 'ύς')
            masculine.append(lemma_adj + 'ύ' + '/' + lemma_adj + 'ιού')
            masculine.append(lemma_adj + 'ύ')
            masculine.append(lemma_adj + 'ύ')
            masculine.append(lemma_adj + 'ιοί')
            masculine.append(lemma_adj + 'ιών')
            masculine.append(lemma_adj + 'ιούς')
            masculine.append(lemma_adj + 'ιοί')

            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιάς')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιές')
            feminine.append(lemma_adj + 'ιών')
            feminine.append(lemma_adj + 'ιές')
            feminine.append(lemma_adj + 'ιές')

            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'ύ' + '/' + lemma_adj + 'ιού')
            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'ιά')
            neutral.append(lemma_adj+ 'ιών')
            neutral.append(lemma_adj + 'ιά')
            neutral.append(lemma_adj + 'ιά')

elif category_adj == "e":
            # Adjectives: -ύς, -εία, -ύ
            masculine.append(lemma_adj + 'ύς')
            masculine.append(lemma_adj + 'έος')
            masculine.append(lemma_adj + 'ύ')
            masculine.append(lemma_adj + 'ύ')
            masculine.append(lemma_adj + 'είς')
            masculine.append(lemma_adj + 'έων')
            masculine.append(lemma_adj + 'είς')
            masculine.append(lemma_adj + 'είς')

            feminine.append(lemma_adj + 'εία')
            feminine.append(lemma_adj + 'είας')
            feminine.append(lemma_adj + 'εία')
            feminine.append(lemma_adj + 'εία')
            feminine.append(lemma_adj + 'είες')
            feminine.append(lemma_adj + 'ειών')
            feminine.append(lemma_adj + 'είες')
            feminine.append(lemma_adj + 'είες')

            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'έος')
            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'ύ')
            neutral.append(lemma_adj + 'έα')
            neutral.append(lemma_adj + 'έων')
            neutral.append(lemma_adj + 'έα')
            neutral.append(lemma_adj + 'έα')

elif category_adj == "f":
            # Adjectives: -ής, -ιά, -ί
            masculine.append(lemma_adj + 'ής')
            masculine.append(lemma_adj + 'ή' + '/' + lemma_adj + 'ιού')
            masculine.append(lemma_adj + 'ή')
            masculine.append(lemma_adj + 'ή')
            masculine.append(lemma_adj + 'ιοί')
            masculine.append(lemma_adj + 'ιών')
            masculine.append(lemma_adj + 'ιούς')
            masculine.append(lemma_adj + 'ιοί')

            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιάς')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιά')
            feminine.append(lemma_adj + 'ιές')
            feminine.append(lemma_adj + 'ιών')
            feminine.append(lemma_adj + 'ιές')
            feminine.append(lemma_adj + 'ιές')

            neutral.append(lemma_adj + 'ί')
            neutral.append(lemma_adj + 'ιού')
            neutral.append(lemma_adj + 'ί')
            neutral.append(lemma_adj + 'ί')
            neutral.append(lemma_adj + 'ιά')
            neutral.append(lemma_adj + 'ιών')
            neutral.append(lemma_adj + 'ιά')
            neutral.append(lemma_adj + 'ιά')

elif category_adj == "g":
            # Adjectives: -ής, -ής, -ές
            masculine.append(lemma_adj + 'ής')
            masculine.append(lemma_adj + 'ούς')
            masculine.append(lemma_adj + 'ή')
            masculine.append(lemma_adj + 'ή')
            masculine.append(lemma_adj + 'είς')
            masculine.append(lemma_adj + 'ών')
            masculine.append(lemma_adj + 'είς')
            masculine.append(lemma_adj + 'είς')

            feminine.append(lemma_adj + 'ής')
            feminine.append(lemma_adj + 'ούς')
            feminine.append(lemma_adj + 'ή')
            feminine.append(lemma_adj + 'ή')
            feminine.append(lemma_adj + 'είς')
            feminine.append(lemma_adj + 'ών')
            feminine.append(lemma_adj + 'είς')
            feminine.append(lemma_adj + 'είς')

            neutral.append(lemma_adj + 'ές')
            neutral.append(lemma_adj + 'ούς')
            neutral.append(lemma_adj + 'ές')
            neutral.append(lemma_adj + 'ές')
            neutral.append(lemma_adj + 'ή')
            neutral.append(lemma_adj + 'ών')
            neutral.append(lemma_adj + 'ή')
            neutral.append(lemma_adj + 'ή')

elif category_adj == "h":
            # Adjectives: -ης, -α, -ικο
            masculine.append(lemma_adj + 'ης')
            masculine.append(lemma_adj + 'η')
            masculine.append(lemma_adj + 'η')
            masculine.append(lemma_adj + 'η')
            masculine.append(lemma_adj + 'ηδες')
            masculine.append(lemma_adj + 'ηδων')
            masculine.append(lemma_adj + 'ηδες')
            masculine.append(lemma_adj + 'ηδες')

            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'ας')
            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'α')
            feminine.append(lemma_adj + 'ες')
            feminine.append('-')  # It does not exist.
            feminine.append(lemma_adj + 'ες')
            feminine.append(lemma_adj + 'ες')

            neutral.append(lemma_adj + 'ικο')
            neutral.append(lemma_adj + 'ικου')
            neutral.append(lemma_adj + 'ικο')
            neutral.append(lemma_adj + 'ικο')
            neutral.append(lemma_adj + 'ικα')
            neutral.append(lemma_adj + 'ικων')
            neutral.append(lemma_adj + 'ικα')
            neutral.append(lemma_adj + 'ικα')

elif category_adj == "i":
            # Adjectives: -ας, -ού, -άδικο/-ούδικο
            masculine.append(lemma_adj + 'άς')
            masculine.append(lemma_adj + 'ά')
            masculine.append(lemma_adj + 'ά')
            masculine.append(lemma_adj + 'ά')
            masculine.append(lemma_adj + 'άδες')
            masculine.append(lemma_adj + 'άδων')
            masculine.append(lemma_adj + 'άδες')
            masculine.append(lemma_adj + 'άδες')

            feminine.append(lemma_adj + 'ού')
            feminine.append(lemma_adj + 'ούς')
            feminine.append(lemma_adj + 'ού')
            feminine.append(lemma_adj + 'ού')
            feminine.append(lemma_adj + 'ούδες')
            feminine.append(lemma_adj + 'ούδων')
            feminine.append(lemma_adj + 'ούδες')
            feminine.append(lemma_adj + 'ούδες')

            neutral.append(lemma_adj + 'άδικο' + '/' + lemma_adj + 'ούδικο')
            neutral.append(lemma_adj + 'άδικου' + '/' + lemma_adj + 'ούδικου')
            neutral.append(lemma_adj + 'άδικο' + '/' + lemma_adj + 'ούδικο')
            neutral.append(lemma_adj + 'άδικο' + '/' + lemma_adj + 'ούδικο')
            neutral.append(lemma_adj + 'άδικα' + '/' + lemma_adj + 'ούδικα')
            neutral.append(lemma_adj + 'άδικων' + '/' + lemma_adj + 'ούδικων')
            neutral.append(lemma_adj + 'άδικα' + '/' + lemma_adj + 'ούδικα')
            neutral.append(lemma_adj + 'άδικα' + '/' + lemma_adj + 'ούδικα')

elif category_adj == "polis":
            # Irregular Adjective: πολύς, πολλή, πολύ
            masculine.append(lemma_adj + 'ύς')
            masculine.append('(' + lemma_adj + 'λού' + ')')  # Rarely used
            masculine.append(lemma_adj + 'ύ')
            masculine.append('-')  # It does not exist
            masculine.append(lemma_adj + 'λοί')
            masculine.append(lemma_adj + 'λών')
            masculine.append(lemma_adj + 'λούς')
            masculine.append('(' + lemma_adj  + 'λοί' + ')')  # Rarely used

            feminine.append(lemma_adj + 'λή')
            feminine.append(lemma_adj + 'λής')
            feminine.append(lemma_adj + 'λή')
            feminine.append('-')  # It does not exist
            feminine.append(lemma_adj + 'λές')
            feminine.append(lemma_adj + 'λών')
            feminine.append(lemma_adj + 'λές')
            feminine.append('(' + lemma_adj + 'λές' + ')')  # Rarely used

            neutral.append(lemma_adj + 'ύ')
            neutral.append('(' + lemma_adj + 'λού' + ')')  # Rarely used
            neutral.append(lemma_adj + 'ύ')
            neutral.append('-')  # It does not exist
            neutral.append(lemma_adj + 'λά')
            neutral.append(lemma_adj + 'λών')
            neutral.append(lemma_adj + 'λά')
            neutral.append('(' + lemma_adj + 'λά' + ')')  # Rarely used
else:
      print('ERROR: No other category implemented yet…')
            # There are a few adjective categories remaining.
            
print(inflection)


class verb:

    def __init__(self, lemma, syzigia, category):
        self.lemma = lemma
        self.syzigia = syzigia
        self.category = category


    def inflect(lemma, syzigia, category):
          inflection = []
          syzigia
          category


          
inflection= []

if syzigia=="A":
    if category=="a":
          inflection.append(lemma + 'ω')
          inflection.append(lemma + 'εις')
          inflection.append(lemma + 'ει')
          inflection.append(lemma + 'ουμε')
          inflection.append(lemma + 'ετε')
          inflection.append(lemma + 'ουν' + '/' + lemma + 'ουνε')
    else:
          print('ERROR: No other category implemented yet…')         
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
                    
elif syzigia == "Irregular Verb" :
          inflection.append(lemma + 'ω')
          inflection.append(lemma + 'ς')
          inflection.append(lemma + 'ει')
          inflection.append(lemma + 'με')
          inflection.append(lemma + 'τε')
          inflection.append(lemma + 'νε')
                    
elif syzigia == "Contracting Verb" :
          inflection.append(lemma + "ω")
          inflection.append(lemma + "ς")
          inflection.append(lemma + "ει")
          inflection.append(lemma + "με")
          inflection.append(lemma + "τε")
          inflection.append(lemma + "νε")
                
else :
        print('ERROR: No other "syzigia" implemented yet…')
                

print(inflection) 
