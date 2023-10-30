import json
from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection
import pymongo

"""
This file processes the given data from the user and formats it into proper JSON format for the frontend to use.

The data is formatted as follows:
sampleData = [
    {
        "Q": "What is the capital of the United States?",
        "A": "Washington D.C.",
    },
    {
        "Q": "What is the capital of Canada?",
        "A": ["Ottawa", "Ottawa, Ontario", "Ottawa, ON"],
    }
]
"""

class processData():
    def __init__(self, data: str, separator: str|int, quiztype:str, quizname: str, mongoDBclient: Collection, username: str, isupdate: bool) -> None:
        self.data = data
        self.processedData = {}
        self.separator = separator
        self.quiztype = quiztype
        self.quizname = quizname
        self.DB = mongoDBclient
        self.user = username
        self.isupdate = isupdate
        self.parser = "TypedAnswer"
        self.parsers = {
            "TA": "TypedAnswer",
            "MCQ": "MultipleChoice",
            "TF": "TrueFalse",
            "FITB": "FillInTheBlanks"
        }
        self.separators = {
            "tab": "\t",
            "semicolon": ";",
            "colon": ":",
            "dash": "-",
            "equals": "=",
        }
        self.preprocess()

    def preprocess(self):
        # prepare data and variables for processing
        for parser in self.parsers:
            if parser in self.quiztype:
                self.parser = self.parsers[parser]
                print(f"Chosen parser: {self.parser}")
                break
        else:
            raise Exception("Invalid quiz type")
        for separator in self.separators:
            if separator in self.separator:
                self.separator = self.separators[separator]
                print(f"Chosen separator: {self.separator}")
                break
        else:
            raise Exception(f"Invalid separator: {self.separator}")
        self.process()

    def process(self):
        if self.isupdate == False:
            # create new quiz
            self.processedData={
                "type": self.quiztype,
                "quizName": self.quizname,
                "questions": [],
            }
            print(self.processedData)
            if self.parser == "TypedAnswer":
                self.processTypedAnswer()
            elif self.parser == "MultipleChoice":
                self.processMultipleChoice()
            elif self.parser == "TrueFalse":
                self.processTrueFalse()
            elif self.parser == "FillInTheBlanks":
                self.processFillInTheBlanks()
            else:
                raise Exception("Invalid parser")
            try:
                docment = self.DB.find_one({"username": self.user})
                legn = len(docment["quizzes"])
                print("processedData: ",self.processedData)
                document = self.DB.find_one_and_update({"username": self.user}, {
                    "$set": {
                        f"quizzes.{legn}":self.processedData
                    }

                }, return_document=pymongo.ReturnDocument.AFTER)
                print(document)
            except Exception as error:
                print(f"error: {error}")
        else:
            # update existing quiz
            if self.parser == "TypedAnswer":
                self.processTypedAnswer()
            elif self.parser == "MultipleChoice":
                self.processMultipleChoice()
            elif self.parser == "TrueFalse":
                self.processTrueFalse()
            elif self.parser == "FillInTheBlanks":
                self.processFillInTheBlanks()
            else:
                raise Exception("Invalid parser")
            try:
                docment = self.DB.find_one({"username": self.user})
                quizindex = self.DB.find_one(
                {
                    "quizzes": {
                    "$elemMatch": {
                        "quizName": f"{self.quizname}"
                    }
                    }
                }
                )
                if quizindex:
                    quizzes = quizindex.get("quizzes", [])
                    for index, quiche in enumerate(quizzes):
                        if quiche.get("quizName") == self.quizname:
                            # The index variable now contains the index of the "testMCQ" quiz.
                            print(f"Index of '{self.quizname}' quiz: {index}")
                            break
                legn = len(docment["quizzes"][index]["questions"])
                legn = legn-1 if legn != 0 else 0
                print(f"index:{index}")
                print(f"legn: {legn}")
                print(f"processedData: {self.processedData}")
                for item in self.processedData:
                    document = self.DB.find_one_and_update({"username": self.user}, {
                        "$push": {
                            f"quizzes.{index}.questions": item
                        }
                    }, return_document=pymongo.ReturnDocument.AFTER)
                print(document)
            except Exception as error:
                print(f"error: {error} --- ln 139 quizDSP.py")

    def processTypedAnswer(self):
        print(self.processedData)
        if self.isupdate == False:
            for line in self.data.splitlines():
                if self.separator in line:
                    self.processedData["questions"].append({
                        "Q": line.split(self.separator)[0].strip(),
                        "A": line.split(self.separator)[1].strip(),
                    })
            processedJSON = json.dumps(self.processedData, indent=4)
            with open("testdata.json", "w+") as f:
                f.write(processedJSON)
            return self.processedData
        else:
            self.processedData = []
            for line in self.data.splitlines():
                if self.separator in line:
                    self.processedData.append({
                        "Q": line.split(self.separator)[0].strip(),
                        "A": line.split(self.separator)[1].strip(),
                    })
            processedJSON = json.dumps(self.processedData, indent=4)
            return self.processedData

    def processMultipleChoice(self):
        if self.isupdate == False:
            for line in self.data.splitlines():
                if self.separator in line:
                    Q = line.split(self.separator)[0].strip()
                    A = line.split(self.separator)[1].strip()
                    A = A.strip("[]")
                    A = A.split(",")
                    A = list(map(str.strip, A))
                    print(A)
                    self.processedData["questions"].append({
                        "Q": line.split(self.separator)[0].strip(),
                        "A": A,
                    })
            processedJSON = json.dumps(self.processedData, indent=4)
            with open("testdata.json", "w+") as f:
                f.write(processedJSON)
            return self.processedData


# print(processData(testText, "dash", "TA"))
