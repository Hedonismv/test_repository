#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
#'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого
#ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
#получить список ключе - использовать метод .keys()
#(подсказка: создается новы ключ с цифро в конце,
#стары удаляется)

currency = {'test':'test_value','europe':'eur','dollar':'usd','ruble':'rub'}
i = 0
while i < 4:
    if 'test' in list(currency.keys()):
        print("NASHEL TEST!")
        length = str(len('test'))
        new_key = 'test' + length
        print(f"{new_key} NOVI KLUCH")
        del currency['test']
        print(currency.keys())
        print("UDALIL")
        currency[new_key] = "test_value"
        print("SDELAL!!")
        print(currency)
        i += 1
        print(i)
    elif 'europe' in list(currency.keys()):
        print("NASHEL EUROPE!")
        length = str(len('europe'))
        new_key = 'europe' + length
        print(f"{new_key} NOVI KLUCH")
        del currency['europe']
        print(currency.keys())
        print("UDALIL")
        currency[new_key] = "eur"
        print("SDELAL!!")
        print(currency)
        i += 1
        print(i)
    elif 'dollar' in list(currency.keys()):
        print("NASHEL DOLLAR!")
        length = str(len('dollar'))
        new_key = "dollar" + length
        print(f"{new_key} NOVI KLUCH")
        del currency['dollar']
        print(currency.keys())
        print("UDALIL")
        currency[new_key] = "usd"
        print("SDELAL!!")
        print(currency)
        i += 1
        print(i)
    elif 'ruble' in list(currency.keys()):
        print("NASHEL RUBLE!")
        length = str(len('ruble'))
        new_key = "ruble" + length
        print(f"{new_key} NOVI KLUCH")
        del currency['ruble']
        print(currency.keys())
        print("UDALIL")
        currency[new_key] = "rub"
        print("SDELAL!!")
        print(currency)
        i += 1
        print(i)
    else:
        print(f"wtf")
print(currency)



    #i = 0
    #while i < 5:
        #key = str(currency.keys())
        #new_key = key + str(len(key))
        #currency[new_key] = currency[key]
        #del currency[key]
        #i += 1
        #continue
    #print(currency.items())

    #for i in currency:
        #for i in new_currency:
            #currency[new_currency[i]] = currency.pop(i)
    #print(currency)
    #print(new_currency)
    #new_currency = {}
    #for key,value in currency.items():
        #length = str(len(key))
        #print(currency.keys())
        #print(currency.values())
        #if key in currency:
            #new_key = key + length
            #print("EST KLUCH!")
            #currency[new_key] = currency.pop(key)
            #print("UDALIL")
        #elif key not in currency:
            #print("KONEC")
            #print(currency.items())
            #break
    #key = currency.keys()
    #value = currency.values()
    #for k,v in currency.items():
        #pass
    #print(key)
    #print(value)
