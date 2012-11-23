__author__ = 'msinghal'

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk
from sentenceBean import SentenceBean

class SummarizeText(object):

    def reorderSentences(self, resultantSentencesList, sentenceListFromInputText ):
        sortedSentenceList = []
        for sentence in sentenceListFromInputText:
            if sentence in resultantSentencesList:
                sortedSentenceList.append(sentence)
        return sortedSentenceList

    def summarizeText(self,textToBeSummarized, numberOfSentences):
        tokenizer = RegexpTokenizer('\w+')
        wordList = tokenizer.tokenize(textToBeSummarized)
        baseWordList = [word.lower() for word in wordList]
        actualWordList = [word for word in baseWordList if word not in stopwords.words()]
        wordFrequencies = FreqDist(actualWordList)
        mostFrequentWords = [pair[0] for pair in wordFrequencies.items()[:100]]
        sentenceDetector = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = sentenceDetector.tokenize(textToBeSummarized)
        sentencesInLowerCase = [sentence.lower() for sentence in sentences]

        sentencesListWithPriorities = []
        for i in range(0, len(sentencesInLowerCase)):
            sentencePriority = 0
            tokenizer = RegexpTokenizer('\w+')
            listOfWordsInSentence = tokenizer.tokenize(sentencesInLowerCase[i])
            for word in mostFrequentWords:
                sentencePriority = sentencePriority + listOfWordsInSentence.count(word)
            sentencesListWithPriorities.append(SentenceBean(sentences[i],sentencePriority))

        listOfPriorityValues = []
        for sentenceElement in sentencesListWithPriorities:
            priorityValue = sentenceElement.priority
            if priorityValue not in listOfPriorityValues:
                listOfPriorityValues.append(priorityValue)

        listOfPriorityValues = sorted(listOfPriorityValues, key=int, reverse=True)

        sentencesContainingMostFrequentWords = []
        for listElement in listOfPriorityValues:
            for sentenceElement in sentencesListWithPriorities:
                priorityValue = sentenceElement.priority
                if priorityValue==listElement and len(sentencesContainingMostFrequentWords)<numberOfSentences:
                    sentencesContainingMostFrequentWords.append(sentenceElement.sentence)

        sentencesContainingMostFrequentWords = self.reorderSentences(sentencesContainingMostFrequentWords, sentences)

        return "  ".join(sentencesContainingMostFrequentWords)
