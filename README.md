# Projekt - Správce úkolů

## Zadání č. 1
Vaším úkolem je doplnit prázdné funkce pro správu úkolů ve správném pořadí. Program by měl umožnit přidávat, zobrazovat a odstraňovat úkoly. 
Následující části kódu jsou prázdné funkce, které musíte doplnit (soubor spravce_ukolu.py). Každá funkce má svůj specifický úkol, který je popsán níže. Úkoly budou ukládány do seznamu ```ukoly = []```. 

### def hlavni_menu()
Funkce hlavního menu, která poskytuje možnosti pro přidání, zobrazení a odstranění úkolu. Pokud uživatel zadá neplatnou volbu, program ho upozorní a nechá uživatele opakovat znovu volbu. 

Výstup v konzoli:
```
Správce úkolů - Hlavní menu
1. Přidat nový úkol      
2. Zobrazit všechny úkoly
3. Odstranit úkol        
4. Konec programu     
Vyberte možnost (1-4):   
```

### def pridat_ukol()
Tato funkce má uživateli umožnit zadat název a popis nového úkolu a uložit jej do seznamu úkolů. Zde platí volba 1 v hlavním menu. Po zadání úkolu program pokračuje dál nabídkou hlavního menu. Při zadání neplatného vstupu do Zadejte název úkolu nebo Popis úkolu, program upozorní uživatele, že zadal prázdný vstup a nechá ho zadat název i popis znovu. 

Výstup v konzoli:
```
Správce úkolů - Hlavní menu
1. Přidat nový úkol      
2. Zobrazit všechny úkoly
3. Odstranit úkol        
4. Konec programu        
Vyberte možnost (1-4): 1 

Zadejte název úkolu: Úkol 1
Zadejte popis úkolu: Popis pro úkol 1
Úkol 'Úkol 1' byl přidán.

Správce úkolů - Hlavní menu
1. Přidat nový úkol        
2. Zobrazit všechny úkoly  
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4):   
```

### def zobrazit_ukoly()
Tato funkce má zobrazit všechny úkoly v seznamu. Zde platí volba 2 v hlavním menu. Po zobrazení úkolů program pokračuje dál nabídkou hlavního menu.

Výstup v konzoli:
```
Správce úkolů - Hlavní menu
1. Přidat nový úkol        
2. Zobrazit všechny úkoly  
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 2   

Seznam úkolů:
1. Úkol 1 - Popis pro úkol 1

Správce úkolů - Hlavní menu 
1. Přidat nový úkol
2. Zobrazit všechny úkoly   
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4):
```

### def odstranit_ukol()
Tato funkce má uživateli umožnit zadat číslo úkolu, který chce odstranit, a tento úkol odstranit. Zde platí volba 3 v hlavním menu. Po odstranění úkolu program pokračuje dál nabídkou hlavního menu. Zde je potřeba, aby uživatel viděl všechny uložené úkoly. 

Výstup v konzoli:
```
Správce úkolů - Hlavní menu 
1. Přidat nový úkol
2. Zobrazit všechny úkoly   
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 3

Seznam úkolů:
1. Úkol 1 - Popis pro úkol 1

Zadejte číslo úkolu, který chcete odstranit: 1
Úkol 'Úkol 1' byl odstraněn.

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4):
```

### Konec programu
Pokud uživatel zadá volbu 4 v hlavním menu program se ukončí. 

Výstup v konzoli:
```
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 4

Konec programu.
```

## Zadání č. 2
Vytvořte testovací scénáře pro každou funkci v projektu Správce úkolů. Testy by měly pokrýt všechny možné cesty a okrajové případy pro dané funkce.

