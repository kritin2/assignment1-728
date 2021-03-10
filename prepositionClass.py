from preprocessing import readXml

class PrepositionClass:
    def __init__(self, senseId, id, prepositionValue, leftContext, rightContext):
        self.senseId = senseId
        self.id = id
        self.prepositionValue = prepositionValue
        self.leftContext = leftContext
        self.rightContext = rightContext


# TODO add tokenizer for contexts    

