from preprocessing import readXml
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
class PrepositionClass:
    def __init__(self, senseId, id, prepositionValue, leftContext, rightContext):
        self.senseId = senseId
        self.id = id
        self.prepositionValue = prepositionValue
        self.leftContext = leftContext
        self.rightContext = rightContext

    def print(self):
        print('id : ', self.id)
        print('senseId : ',self.senseId)
        print(self.leftContext + "\n" + self.prepositionValue + "\n" + self.rightContext )
        print(self.leftContextList , self.prepositionValue , self.rightContextList )
    
    def tokenizeSentence(self):
        leftContextTemp = self.leftContext.lower()
        leftContextTemp = re.sub(r'[^\w\s]', '', leftContextTemp)
        leftContextToken = word_tokenize(leftContextTemp)
        self.leftContextList = [word for word in leftContextToken if not word in stopwords.words()]

        rightContextTemp = self.rightContext.lower()
        rightContextTemp = re.sub(r'[^\w\s]', '', rightContextTemp)
        rightContextToken = word_tokenize(rightContextTemp)
        self.rightContextList = [word for word in rightContextToken if not word in stopwords.words()]    
        

if __name__ == '__main__' :
    testObject = PrepositionClass('2(1)', 'aboutid','about','He saw Owen redden with pleasure , and laughed , flinging an arm', 
    'his shoulders so forgetfully that it was a worthy as well as a willing sacrifice Owen made for him , containing the pain of the embrace .')
    testObject.tokenizeSentence()
    testObject.print()
