from eng_syl.syllabify import Syllabel
from eng_syl.onceler import Onceler
from eng_syl.phonify import onc_to_phon


class Phonetics:
    def __init__(self):
        self.otp = onc_to_phon()
        self.onc = Onceler()
        self.syllabler = Syllabel()

    def syllable_phonetic_breakdown(self, word):
        word = word.capitalize()
        word_syllables = self.syllabler.syllabify(word)
        if word_syllables is None:
            word_syllables = input("Could not divide '" + word + "' into syllables. Enter manual answer: ")
        phonemes_grp_eng = []
        syllables_sizes = []
        for syllable in word_syllables.split('-'):
            if syllable != '':
                syllable_size = 0
                syllable_breakdown = self.onc.onc_split(syllable)
                for phoneme_grp_eng in syllable_breakdown.split('-'):
                    if phoneme_grp_eng != '':
                        phonemes_grp_eng.append(phoneme_grp_eng.lower())
                        syllable_size += 1
                syllables_sizes.append(syllable_size)
        phonemes_grp = self.otp.ipafy(phonemes_grp_eng)
        print(phonemes_grp)
        return phonemes_grp, syllables_sizes
