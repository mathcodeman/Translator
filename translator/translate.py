from googletrans import Translator


def trans(raw_text):
    translation = Translator()
    trans_text = translation.translate(text=raw_text,dest='ja').text
    return trans_text

