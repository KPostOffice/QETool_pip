import request

apiLocation = 'http://localhost:5000'

class QEdataRequest():

    def validCards(self):
        return requests.get(apiLocation + "/valid/cards").json

    def validTests(self):
        return requests.get(apiLocation + "/valid/tests").json

    def validSubtests(self, test):
        payload = {"test": test}
        return requests.get(apiLocation+"/valid/subtests", params=payload).json

    def validTypes(self, test, subtest):
        payload = {"test": test, "subtest": subtest}
        return requests.get(apiLocation+"/valid/types", params=payload).json

    def validLabels(self, test, subtest, type):
        payload = {"test": test, "subtest": subtest, "type":type}
        return requests.get(apiLocation+"/valid/types", params=payload)

    def getData(self, **kwargs):
        payload = kwargs
        return requests.get(apiLocation+"/data",params=payload)

    def getStructure(self):
        return requests.get(apiLocation + "/charts")
