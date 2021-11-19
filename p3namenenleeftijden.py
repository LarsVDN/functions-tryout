def agePerson():
    while True:
        name = input('Naam: ')
        if name == 'stop':
            break
        age = input('Leeftijd: ')

        print('Hallo', name, 'je leeftijd is', age)

agePerson()
