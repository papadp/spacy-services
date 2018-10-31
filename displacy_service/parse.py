from __future__ import unicode_literals


class Parse(object):
    def __init__(self, nlp, text, collapse_punctuation, collapse_phrases):
        self.doc = nlp(text)

    def to_json(self):
        words = [{'text': w.text, 'tag': w.tag_, 'pos': w.pos_, 'dep': w.dep_} for w in self.doc]

        return words


class Entities(object):
    def __init__(self, nlp, text):
        self.doc = nlp(text)
     
    def to_json(self):
        return [{'start': ent.start_char, 'end': ent.end_char, 'type': ent.label_}
                for ent in self.doc.ents]
