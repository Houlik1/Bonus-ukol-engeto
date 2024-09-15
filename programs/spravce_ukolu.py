ukoly = []


def pridat_ukol(ukol,popis):
    """Funkce pro přidání nového úkolu."""  
    message = f"Ukol {ukol} byl přidán."
    print(message)
    ukoly.append((ukol,popis))
    return message
    
    

def zobrazit_ukoly():
    """Funkce pro zobrazení všech úkolů."""
    print("Seznam úkolů: ")
    for index, (task,describe) in enumerate(ukoly,start=1):
        print (f"{index}. {task} - {describe}")
        return (f"{index}. {task} - {describe}")
   
    

def odstranit_ukol(vymazani):
    """Funkce pro odstranění úkolu."""
    
    odebrany_prvek =ukoly.pop(vymazani-1)

    print(f"Úkol {odebrany_prvek[0]} byl odstraněn.")
    return f"Úkol {odebrany_prvek[0]} byl odstraněn."
    

    pass

def hlavni_menu():
    """Hlavní menu aplikace."""
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol ")
    print("4. Konec programu")
    volba = input("Vyberte možnost (1-4):")
    if volba =="1":
        ukol = input("Zadejte název ukolu: ")
        popis = input("Zadejte popis úkolu: ")
        pridat_ukol(ukol,popis)
        hlavni_menu()
    elif volba=="2":
        zobrazit_ukoly()
        hlavni_menu()
    elif volba=="3":
        zobrazit_ukoly()
        vymazani =int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        odstranit_ukol(vymazani)
        hlavni_menu()
    elif volba =="4":
        print("Konec programu")
    else:
        print("Neplatna volba")
        
    pass

if __name__ == "__main__":
    hlavni_menu()