from colors import Colors, split_into_syllables
from drawer import Drawer
from phonetics import Phonetics


sentence = "Example sentence"
drawer = Drawer()
for word in sentence.split():
    phonetics = Phonetics()
    phonemes_grp, syllables_sizes = phonetics.syllable_phonetic_breakdown(word)
    colors = Colors()
    new_sizes = colors.breakdown_correction(phonemes_grp, syllables_sizes)
    splitted = split_into_syllables(phonemes_grp, new_sizes)

    for syllable in splitted:
        onset_vals, nucleus_vals, coda_vals = colors.obtain_syllable_color_values(syllable)
        drawer.draw_syllable(onset_vals, nucleus_vals, coda_vals)
    drawer.draw_spacebar()

drawer.finish()
