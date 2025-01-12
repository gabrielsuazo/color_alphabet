def init_vowels_dict():
    vowels = dict()
    vowels['ɑ'] = 335
    vowels['a'] = 0
    vowels['æ'] = 25
    vowels['ɔ'] = 310
    vowels['ʌ'] = 285
    vowels['ɛ'] = 50
    vowels['ɜ'] = 75
    vowels['ə'] = 100
    vowels['o'] = 260
    vowels['e'] = 125
    vowels['ʊ'] = 235
    vowels['ɪ'] = 150
    vowels['u'] = 210
    vowels['i'] = 175
    return vowels


def init_consonants_dict():
    consonants = dict()
    consonants['p'] = (11, 29)
    consonants['b'] = (11, 53)
    consonants['v'] = (11, 73)
    consonants['f'] = (11, 89)
    consonants['d'] = (29, 11)
    consonants['t'] = (29, 29)
    consonants['tʃ'] = (29, 53)
    consonants['dʒ'] = (29, 73)
    consonants['j'] = (29, 89)
    consonants['θ'] = (53, 11)
    consonants['ð'] = (53, 29)
    consonants['k'] = (53, 53)
    consonants['g'] = (53, 73)
    consonants['r'] = (53, 89)
    consonants['s'] = (73, 11)
    consonants['z'] = (73, 29)
    consonants['ʒ'] = (73, 53)
    consonants['ʃ'] = (73, 73)
    consonants['l'] = (73, 89)
    consonants['m'] = (89, 11)
    consonants['n'] = (89, 29)
    consonants['ŋ'] = (89, 53)
    consonants['w'] = (89, 73)
    consonants['h'] = (89, 89)

    return consonants


def split_into_syllables(phonemes_grp, syllables_sizes):
    size_cumul = 0
    syllables_list = []
    for size in syllables_sizes:
        syllable = []
        for i in range(size_cumul, size_cumul + size):
            phoneme = phonemes_grp[i]
            syllable.append(phoneme)
        size_cumul += size
        syllables_list.append(syllable)
    return syllables_list


class Colors:
    def __init__(self):
        self.vowels_hue = init_vowels_dict()
        self.consonants_sat_val = init_consonants_dict()

    def check_dictionaries(self, character):
        if character in self.vowels_hue:
            return True, self.vowels_hue[character]
        elif character in self.consonants_sat_val:
            return False, self.consonants_sat_val[character]
        else:
            print(character + " not found in the dictionaries")
            raise Exception

    def breakdown_correction(self, phonemes_grp, syllables_sizes):
        phonemes_counter = 0
        new_sizes = []
        sizes_counter = 0

        while sizes_counter < len(syllables_sizes):
            size = syllables_sizes[sizes_counter]
            if size == 1 and phonemes_grp[phonemes_counter] in self.consonants_sat_val:
                if sizes_counter + 1 < len(syllables_sizes):
                    combined = size + syllables_sizes[sizes_counter + 1]
                    new_sizes.append(combined)
                    phonemes_counter += combined
                    sizes_counter += 2
                else:
                    new_sizes[sizes_counter - 1] += 1
                    phonemes_counter += size
                    sizes_counter += 1
            else:
                new_sizes.append(size)
                phonemes_counter += size
                sizes_counter += 1

        return new_sizes

    def obtain_syllable_color_values(self, phonemes_grp):
        onset_vals = []
        nucleus_vals = []
        coda_vals = []
        for phoneme_grp in phonemes_grp:
            i = 0
            while i < len(phoneme_grp):
                character = phoneme_grp[i]
                if character == ':':
                    i += 1
                    continue
                if i < len(phoneme_grp) - 1:
                    if character == 't':
                        if phoneme_grp[i + 1] == 'ʃ':
                            _, val = self.check_dictionaries('tʃ')
                            if len(nucleus_vals) == 0:
                                onset_vals.append(val)
                            else:
                                coda_vals.append(val)
                            i += 2
                    elif character == 'd':
                        if phoneme_grp[i + 1] == 'ʒ':
                            _, val = self.check_dictionaries('dʒ')
                            if len(nucleus_vals) == 0:
                                onset_vals.append(val)
                            else:
                                coda_vals.append(val)
                            i += 2
                boolean, val = self.check_dictionaries(character)
                if boolean:
                    nucleus_vals.append(val)
                else:
                    if len(nucleus_vals) == 0:
                        onset_vals.append(val)
                    else:
                        coda_vals.append(val)
                i += 1
        return onset_vals, nucleus_vals, coda_vals
