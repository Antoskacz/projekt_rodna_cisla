class Osoba:
    def __init__(self, rodne_cislo):
        self.rodne_cislo = rodne_cislo
        self.datum_narozeni = None
        self.pohlavi = None


    def overeni(self):
        if len(self.rodne_cislo) < 9 or len(self.rodne_cislo) > 10:
            return False
        try:
            int(self.rodne_cislo[:6])
        except ValueError:
            return False
        return True

    def ziskej_datum_narozeni(self):
        datum = self.rodne_cislo[:6]
        den = int(datum[4:6])
        mesic = int(datum[2:4])
        rok = int(datum[0:2])
        if mesic > 12:
            mesic -= 50
        if rok > 24:
            rok += 1900
        else:
            rok += 2000
        self.datum_narozeni = f"{den}.{mesic}.{rok}"
        datum_narozeni = self.datum_narozeni

    def urci_pohlavi(self):
        mesic = int(self.rodne_cislo[2:4])
        self.pohlavi = "žena" if mesic > 12 else "muž"

    def vek(self):
        from datetime import datetime
        today = datetime.now()
        rok_narozeni = int(self.rodne_cislo[0:2])
        mesic_narozeni = int(self.rodne_cislo[2:4])
        den_narozeni = int(self.rodne_cislo[4:6])
        if mesic_narozeni > 12:
            mesic_narozeni -= 50
        if rok_narozeni > 24:
            rok_narozeni += 1900
        else:
            rok_narozeni += 2000
        vek = today.year - rok_narozeni - ((today.month, today.day) < (mesic_narozeni, den_narozeni))
        return vek

    def informace(self):
        if self.datum_narozeni and self.pohlavi:
            print(f"Datum narození: {self.datum_narozeni}")
            print(f"Pohlaví: {self.pohlavi}")
            print(f"Věk: {self.vek()} let")

    def __iter__(self):
        yield from (self.rodne_cislo, self.datum_narozeni, self.pohlavi)


def main():
    rodne_cislo = input("Zadejte rodné číslo bez přidaných znaků: ")
    osoba = Osoba(rodne_cislo)
    if not osoba.overeni():
        print("Neplatné rodné číslo. Prosím, zadejte ve správném formátu.")
        return
    osoba.ziskej_datum_narozeni()
    osoba.urci_pohlavi()
    osoba.informace()
    cesta_k_souboru = "rodna_cisla.txt"
    with open(cesta_k_souboru, "a") as file:
        file.writelines(f"\n {rodne_cislo}")


if __name__ == "__main__":
    main()



import unittest
from datetime import datetime

class TestOsoba(unittest.TestCase):

    def test_overeni_valid(self):
        osoba = Osoba("9205141234")
        self.assertTrue(osoba.overeni())

    def test_overeni_invalid_length(self):
        osoba = Osoba("92051")
        self.assertFalse(osoba.overeni())

    def test_overeni_invalid_format(self):
        osoba = Osoba("92A5141234")
        self.assertFalse(osoba.overeni())

    def test_ziskej_datum_narozeni_muz(self):
        osoba = Osoba("9205141234")
        osoba.ziskej_datum_narozeni()
        self.assertEqual(osoba.datum_narozeni, "14.5.1992")

    def test_ziskej_datum_narozeni_zena(self):
        osoba = Osoba("9255141234")
        osoba.ziskej_datum_narozeni()
        self.assertEqual(osoba.datum_narozeni, "14.5.1992")

    def test_urci_pohlavi_muz(self):
        osoba = Osoba("9205141234")
        osoba.urci_pohlavi()
        self.assertEqual(osoba.pohlavi, "muž")

    def test_urci_pohlavi_zena(self):
        osoba = Osoba("9255141234")
        osoba.urci_pohlavi()
        self.assertEqual(osoba.pohlavi, "žena")

    def test_vek(self):
        osoba = Osoba("9205141234")
        self.assertEqual(osoba.vek(), datetime.now().year - 1992)

if __name__ == '__main__':
    unittest.main()
