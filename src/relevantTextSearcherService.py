__author__ = 'msinghal'

from summarize_text import SummarizeText

class SentimentAnalyzingService(object):

    def __init__(self):
        self.textSummarizer = SummarizeText()

    def summarizeText(self,textToBeSummarized):
        summarizedText = self.textSummarizer.summarizeText(textToBeSummarized, 3)
        return summarizedText

