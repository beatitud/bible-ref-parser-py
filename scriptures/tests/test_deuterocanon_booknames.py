import unittest

from ..texts.deuterocanon import Deuterocanon

dc = Deuterocanon()


def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return dc.reference_to_string(
            *dc.normalize_reference(*dc.scripture_re.match(txt).groups()))


class TestDeuterocanonBookNames(unittest.TestCase):
    def setUp(self):
        pass

    def test_1esd(self):
        self.assertEqual(f('1esdras 1'),
                         'I Esdras 1')
        self.assertEqual(f('1esd 1'),
                         'I Esdras 1')
        self.assertEqual(f('Iesdras 1'),
                         'I Esdras 1')

    def test_2esd(self):
        self.assertEqual(f('2esdras 1'),
                         'II Esdras 1')
        self.assertEqual(f('2esd 1'),
                         'II Esdras 1')
        self.assertEqual(f('IIesdras 1'),
                         'II Esdras 1')

    def test_tobit(self):
        self.assertEqual(f('tobit 1:1'), 'Tobit 1:1')
        self.assertEqual(f('tob 1:1'), 'Tobit 1:1')

    def test_judith(self):
        self.assertEqual(f('judith 1:1'), 'Judith 1:1')
        self.assertEqual(f('Jud 1:1'), 'Judith 1:1')

    def test_additions_to_esther(self):
        self.assertEqual(f('esther (greek) 1:1'), 'Esther (Greek) 1:1')

    def test_wisdom_of_solomon(self):
        self.assertEqual(f('the wisdom of solomon 1:1'),
                         'The Wisdom of Solomon 1:1')
        self.assertEqual(f('wis 1:1'), 'The Wisdom of Solomon 1:1')
        self.assertEqual(f('wisdom of solomon 1:1'),
                         'The Wisdom of Solomon 1:1')
        self.assertEqual(f('wisdom 1:1'),
                         'The Wisdom of Solomon 1:1')

    def test_ecclesiasticus_aka_sirach(self):
        self.assertEqual(f('sirach 1:1'), 'Sirach 1:1')
        self.assertEqual(f('sir 1:1'), 'Sirach 1:1')

    def test_baruch(self):
        self.assertEqual(f('baruch 1:1'), 'Baruch 1:1')
        self.assertEqual(f('bar 1:1'), 'Baruch 1:1')

    def test_letter_of_jeremiah(self):
        self.assertEqual(f('letter of jeremiah 1'),
                         'Letter of Jeremiah 1')

    def testprayer_of_azariah(self):
        self.assertEqual(f('prayer of azariah 1'),
                         'Prayer of Azariah 1')
        self.assertEqual(f('azar 1'),
                         'Prayer of Azariah 1')

    def test_susanna(self):
        self.assertEqual(f('susanna 1'), 'Susanna 1')

    def test_bel_and_the_dragon(self):
        self.assertEqual(f('bel and the dragon 1'),
                         'Bel and the Dragon 1')
        self.assertEqual(f('bel 1'),
                         'Bel and the Dragon 1')
        self.assertEqual(f('bel dragon 1'),
                         'Bel and the Dragon 1')

    def test_prayer_of_manasseh(self):
        self.assertEqual(f('prayer of manasseh 1'),
                         'Prayer of Manasseh 1')
        self.assertEqual(f('manasseh 1'),
                         'Prayer of Manasseh 1')

    def test_1_maccabees(self):
        self.assertEqual(f('1 maccabees 1:1'), 'I Maccabees 1:1')
        self.assertEqual(f('1Macc 1:1'), 'I Maccabees 1:1')
        self.assertEqual(f('I Macc 1:1'), 'I Maccabees 1:1')
        self.assertEqual(f('I Maccabees 1:1'), 'I Maccabees 1:1')

    def test_2_maccabees(self):
        self.assertEqual(f('2 maccabees 1:1'), 'II Maccabees 1:1')
        self.assertEqual(f('2Macc 1:1'), 'II Maccabees 1:1')
        self.assertEqual(f('II Macc 1:1'), 'II Maccabees 1:1')
        self.assertEqual(f('II Maccabees 1:1'), 'II Maccabees 1:1')
