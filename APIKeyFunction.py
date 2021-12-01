class APIKey:
    def __init__(self):
        with open("APIKey.txt", "r") as api:
            self.__api = api.readline()
    
    def getAPI(self):
        return self.__api