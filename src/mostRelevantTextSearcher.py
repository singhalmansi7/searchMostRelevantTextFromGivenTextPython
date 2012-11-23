__author__ = 'msinghal'

import web
from relevantTextSearcherService import SentimentAnalyzingService

render = web.template.render('/home/msinghal/PycharmProjects/searchMostRelevantTextFromGivenTextPython/templates')

urls = (
    '/Ok', 'Index'
    )

app = web.application(urls, globals())

class Index(object):

    def GET(self):
        return render.get_text()

    def POST(self):
        form = web.input(paragraph="None")
        textToBeAnalysed = "%s" % (form.paragraph)
        service = SentimentAnalyzingService()
        summarizedText = service.summarizeText(textToBeAnalysed);
        return render.result(summarizedText = summarizedText)


if __name__ == "__main__":
    app.run()


