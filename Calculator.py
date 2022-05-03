user_choice_after_result = "1"
while user_choice_after_result == "1":
    print()
    print("----------------------------")
    print("Calculator")
    print("")
    first_number = input("Podaj pierwszą wartość  ")
    print("")
    print("Dodawanie [1]")
    print("Odejmowanie [2]")
    print("Mnożenie [3]")
    print("Dzielenie [4]")
    print("")
    type_of_operation = input("Wybierz rodzaj działania ")
    print("")
    if int(type_of_operation) > 5 or int(type_of_operation) < 1:
        print("Wybrałeś zły numer")
    second_number = input("Podaj drugą wartość ")
    print("")

    if type_of_operation == "1":
        result = int(first_number) + int(second_number)
        print("Twój wynik to:   " + str(result))
    if type_of_operation == "2":
        result = int(first_number) - int(second_number)
        print("Twój wnik to:   " + str(result))
    if type_of_operation == "3":
        result = int(first_number) * int(second_number)
        print("Twój wnik to:   " + str(result))
    if type_of_operation == "4":
        result = int(first_number) / int(second_number)
        print("Twój wnik to:   " + str(result))
    print()
    print("Powrót [1]")
    print("Wyjście [2]")
    user_choice_after_result = input("Co chcesz zrobić?  ")
    if user_choice_after_result == "2":
        break
