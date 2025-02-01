import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseURL")
        return url

    @staticmethod
    def getPhoneNumber():
        phonenumber = config.get("common info", "phonenumber")
        return phonenumber

    @staticmethod
    def getInput1():
        input1 = config.get("common info", "input1")
        return input1

    @staticmethod
    def getInput2():
        input2 = config.get("common info", "input2")
        return input2

    @staticmethod
    def getInput3():
        input3 = config.get("common info", "input3")
        return input3

    @staticmethod
    def getInput4():
        input4 = config.get("common info", "input4")
        return input4