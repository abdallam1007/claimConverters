from DIGConverter import DIGConverter
from QICConverter import QICConverter
from AlkootConverter import AlkootConverter
from QLMConverter import QLMConverter


# Test DIG

DIGConverter = DIGConverter()
DIGDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/ExternalClaimTemplates/ClaimsDIG1.csv"
standardizedDIGDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/DIG/ClaimDIG1ToStandard.csv"
convertedToDIGDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/DIG/ClaimStandardToDIG1.csv"

#DIGConverter.parseToStandardFormat(DIGDataPath, standardizedDIGDataPath)
#DIGConverter.convertFromStandardFormat(standardizedDIGDataPath, convertedToDIGDataPath)


# Test QIC

QICConverter = QICConverter()
QICDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/ExternalClaimTemplates/ClaimsQIC1.csv"
standardizedQICDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/QIC/ClaimQIC1ToStandard.csv"
convertedToQICDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/QIC/ClaimStandardToQIC1.csv"

#QICConverter.parseToStandardFormat(QICDataPath, standardizedQICDataPath)
#QICConverter.convertFromStandardFormat(standardizedQICDataPath, convertedToQICDataPath)


# Test Alkoot

AlkootConverter = AlkootConverter()
AlkootDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/ExternalClaimTemplates/ClaimsAlkoot1.csv"
standardizedAlkootDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/Alkoot/ClaimAlkoot1ToStandard.csv"
convertedToAlkootDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/Alkoot/ClaimStandardToAlkoot1.csv"

AlkootConverter.parseToStandardFormat(AlkootDataPath, standardizedAlkootDataPath)
AlkootConverter.convertFromStandardFormat(standardizedAlkootDataPath, convertedToAlkootDataPath)


# Test QLM

QLMConverter = QLMConverter()
QLMDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/ExternalClaimTemplates/ClaimsQLM1.csv"
standardizedQLMDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/QLM/ClaimQLM1ToStandard.csv"
convertedToQLMDataPath = "/Users/abdallamohamed/Desktop/Avey/claimConverters/src/results/QLM/ClaimStandardToQLM1.csv"

QLMConverter.parseToStandardFormat(QLMDataPath, standardizedQLMDataPath)
QLMConverter.convertFromStandardFormat(standardizedQLMDataPath, convertedToQLMDataPath)