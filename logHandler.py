class LogHandler:

    def __init__(self) -> None:
        self.__logFileName = "log.txt"

        with open(self.__logFileName, "w+") as log:
            log.close()
        
    def writeIncompleteResponse(self, row, progress):
        with open(self.__logFileName, "a") as log:
            log.write("INCOMPLETE: Row " + str(row) + " is incomplete with " + str(progress) + " survey response progress\n")
            log.close()

    def writeNotInDateRange(self, row):
        with open(self.__logFileName, "a") as log:
            log.write("SKIPPED: Row " + str(row) + " is not within the specified date range\n")

    def writePostSuccess(self, row):
        with open(self.__logFileName, "a") as log:
            log.write("POST_SUCCESS: Row " + str(row) + " was successfully put\n")
            log.close()

    def writePostFailure(self, row, response):
        with open(self.__logFileName, "a") as log:
            log.write("POST_ERROR: Row " + str(row) + " failed to put, receiving response " + str(response) + "\n")
            log.close()
    
    def writeNotification(self, row, msg):
        with open(self.__logFileName, "a") as log:
            log.write("NOTE: Row " + str(row) + " " + msg + "\n")
            log.close()

    def writeError(self, row, error, msg):
        with open(self.__logFileName, "a") as log:
            log.write(str(error) + ": Row " + str(row) + " " + msg + "\n")
            log.close()
    