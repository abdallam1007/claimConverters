from abc import ABC, abstractmethod

class InsuranceCompanyConverterInterface(ABC):
    @abstractmethod
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        pass
    
    @abstractmethod
    def convertFromStandardFormat(self, inputFilePath, outputFilePath):
        pass