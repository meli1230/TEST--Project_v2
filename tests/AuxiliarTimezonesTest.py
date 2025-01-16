import unittest
from data.storage import TIMEZONES

class TestTimezones(unittest.TestCase):
    """
    Testează integritatea listei globale `TIMEZONES`, care conține fusurile orare disponibile
    pentru utilizatori. Verificările includ:
    - Lista nu ar trebui să fie goală.
    - Lista ar trebui să conțină doar valori unice.
    """

    def test_timezones_not_empty(self):
        """
        Verifică dacă lista `TIMEZONES` conține cel puțin un element.
        - Acest test asigură că există fusuri orare definite pentru utilizatori.
        """
        self.assertTrue(len(TIMEZONES) > 0, "Lista TIMEZONES nu ar trebui să fie goală.")

    def test_timezones_are_unique(self):
        """
        Verifică dacă toate valorile din lista `TIMEZONES` sunt unice.
        - Previne duplicarea fusurilor orare, care ar putea duce la confuzie sau erori.
        """
        self.assertEqual(len(TIMEZONES), len(set(TIMEZONES)), "Lista TIMEZONES ar trebui să conțină doar valori unice.")