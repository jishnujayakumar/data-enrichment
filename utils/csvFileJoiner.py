import os
import errno
import pandas as pd


class csvFileJoiner:
    fileFrames = []
    dirContainsFile = False
    joinedFrame = None

    def __init__(self, fileDirectoryPath):
        self.fileDirectoryPath = fileDirectoryPath
        for file in os.listdir(self.fileDirectoryPath):
            if file.endswith(".csv"):
                self.fileFrames.append(pd.read_csv(os.path.join(self.fileDirectoryPath, file)))
        if len(self.fileFrames) > 0:
            self.dirContainsFile = True

    def joinAndGenerateCSVFiles(self, path, fileName):
        if (self.dirContainsFile):
            self.joinedFrame = pd.concat(self.fileFrames, join='outer')
            self.makeSurePathExists(path)
            pd.DataFrame.to_csv(self.joinedFrame, os.path.join(path, fileName), header=True, index=False,
                                index_label=None)
        else:
            print "The specified directory doesn't have any csv file."

    def makeSurePathExists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
