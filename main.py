#questionnaire 5 questions

# questionnaire 5 questions



print("questionnaire 5 questions ")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("quel est votre nom ? ")

    return reponse_nom


def question_1():
    resultat_question_1 = input("quel est la capitale de la france ? ")
    if resultat_question_1 == "paris":
        print(" vrai ")
    elif resultat_question_1 == "Paris":
        print(" vrai ")
    else:print(" faux ")
    return resultat_question_1


def question_2():
    resultat_question_2 = input("quel est la capitale de l'allemagne ? ")
    if resultat_question_2 == "berlin":
        print(" vrai ")
    elif resultat_question_2 == "Berlin":
        print(" vrai ")
    else:print(" faux ")
    return resultat_question_2


def question_3():
    resultat_question_3 = input("quel est la capitale de la guinée ? ")
    if resultat_question_3 == "conakry":
        print(" vrai ")
    elif resultat_question_3 == "Conakry":
        print(" vrai ")
    else:print(" faux ")
    return resultat_question_3


def question_4():
    resultat_question_4 = input(" quel la capital de la russie ? ")
    if resultat_question_4 == "moscou":
        print(" vrai ")
    elif resultat_question_4 == "Moscou":
        print(" vrai ")
    else:print(" faux ")
    return resultat_question_4


def question_5():
    resultat_question_5 = input(" quel la capital de la chine ? ")
    if resultat_question_5 == "hong kong":
        print(" vrai ")
    elif resultat_question_5 == "hong-kong":
        print(" vrai ")
    elif resultat_question_5 == "hongkong":
        print(" vrai ")
    else:print(" faux ")
    return resultat_question_5


# demander nom
nom = demander_nom()








# posez les questions
print(" bonjour "+ nom + " bienvenue sur ce questionnaire nous allons vous posez 5 questions ,")
question_1()
question_2()
question_3()
question_4()
question_5()
print(" merci d'avoir participer au questionnaire, bonne journée . ")


