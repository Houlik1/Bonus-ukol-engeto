import pytest
from programs import spravce_ukolu

def test_pridat_ukol():
    response = spravce_ukolu.pridat_ukol("Testovací úkol", "Popis testovacího úkolu")
    assert response ==  "Ukol Testovací úkol byl přidán."
    assert len(spravce_ukolu.ukoly)==1
    assert spravce_ukolu.ukoly ==[("Testovací úkol", "Popis testovacího úkolu")]

def test_zobrazit_ukoly ():
    response = spravce_ukolu.zobrazit_ukoly()
    assert response == "1. Testovací úkol - Popis testovacího úkolu"

def test_odstranit_ukol():
    response = spravce_ukolu.odstranit_ukol(1)
    assert response == "Úkol Testovací úkol byl odstraněn."
    
    
    
    
