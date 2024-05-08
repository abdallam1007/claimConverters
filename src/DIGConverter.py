import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class DIGConverter(InsuranceCompanyConverterInterface):
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)

        # Mapping columns from DIG format to standard format
        column_mapping = {
            "Claim #*": "Invoice Number",
            "Member ID*": "Patient ID",
            "Date*": "Procedure Date",
            "CPT code*": "CPT Code",
            "CPT Description": "CPT Code Description",
            "Primary Diagnosis ICD 10 code*": "Principal ICD10 Code",
            "Primary Diagnosis ICD 10 description ": "Principal ICD10 Code Description",
            "Secondary Diagnosis 1 - ICD 10 code": "Secondary ICD10 Code 1",
            "Secondary Diagnosis 1 - ICD 10 code description ": "Secondary ICD10 Code 1 Description",
            "Secondary Diagnosis 2 - ICD 10 code": "Secondary ICD10 Code 2",
            "Secondary Diagnosis 2 - ICD 10 code description ": "Secondary ICD10 Code 2 Description",
            "Secondary Diagnosis 3 - ICD 10 code": "Secondary ICD10 Code 3",
            "Secondary Diagnosis 3 - ICD 10 code description ": "Secondary ICD10 Code 3 Description",
            "Secondary Diagnosis 4 - ICD 10 code": "Secondary ICD10 Code 4",
            "Secondary Diagnosis 4 - ICD 10 code description ": "Secondary ICD10 Code 4 Description",
            "Secondary Diagnosis 5 - ICD 10 code": "Secondary ICD10 Code 5",
            "Secondary Diagnosis 5 - ICD 10 code description ": "Secondary ICD10 Code 5 Description",
            "Secondary Diagnosis 6 - ICD 10 code": "Secondary ICD10 Code 6",
            "Secondary Diagnosis 6 - ICD 10 code description ": "Secondary ICD10 Code 6 Description",
            "Secondary Diagnosis 7 - ICD 10 code": "Secondary ICD10 Code 7",
            "Secondary Diagnosis 7 - ICD 10 code description ": "Secondary ICD10 Code 7 Description",
            "Secondary Diagnosis 8 - ICD 10 code": "Secondary ICD10 Code 8",
            "Secondary Diagnosis 8 - ICD 10 code description ": "Secondary ICD10 Code 8 Description",
            "Secondary Diagnosis 9 - ICD 10 code": "Secondary ICD10 Code 9",
            "Secondary Diagnosis 9 - ICD 10 code description ": "Secondary ICD10 Code 9 Description",
            "Secondary Diagnosis 10 - ICD 10 code": "Secondary ICD10 Code 10",
            "Secondary Diagnosis 10 - ICD 10 code description ": "Secondary ICD10 Code 10 Description",
            "Secondary Diagnosis 11 - ICD 10 code": "Secondary ICD10 Code 11",
            "Secondary Diagnosis 11 - ICD 10 code description ": "Secondary ICD10 Code 11 Description",
            "QTY APPROVED": "QTY APPROVED",
            "QTY CLAIMED": "Quantity",
            "Approval Status ": "Approval Status",
            "GM Decision": "GM Decision (subclaim level)"
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Patient Name": "",
            "Clinician Name": "",
            "Clinician ID": "",
            "Secondary ICD10 Code 12": "",
            "Secondary ICD10 Code 12 Description": "",
            "Secondary ICD10 Code 13": "",
            "Secondary ICD10 Code 13 Description": "",
            "Amount Requested": "",
            "Submitter User Note": "",
            "Patient DOB": "",
            "Patient Gender": ""
        }
        for col_name, col_value in additional_columns.items():
            data[col_name] = col_value

        # Reorder columns to match the desired output order
        desired_order = [
            "Invoice Number", "Patient ID", "Patient Name", "Clinician Name", "Clinician ID", 
            "Procedure Date", "CPT Code", "CPT Code Description",
            "Principal ICD10 Code", "Principal ICD10 Code Description",
            "Secondary ICD10 Code 1", "Secondary ICD10 Code 1 Description",
            "Secondary ICD10 Code 2", "Secondary ICD10 Code 2 Description",
            "Secondary ICD10 Code 3", "Secondary ICD10 Code 3 Description",
            "Secondary ICD10 Code 4", "Secondary ICD10 Code 4 Description",
            "Secondary ICD10 Code 5", "Secondary ICD10 Code 5 Description",
            "Secondary ICD10 Code 6", "Secondary ICD10 Code 6 Description",
            "Secondary ICD10 Code 7", "Secondary ICD10 Code 7 Description",
            "Secondary ICD10 Code 8", "Secondary ICD10 Code 8 Description",
            "Secondary ICD10 Code 9", "Secondary ICD10 Code 9 Description",
            "Secondary ICD10 Code 10", "Secondary ICD10 Code 10 Description",
            "Secondary ICD10 Code 11", "Secondary ICD10 Code 11 Description",
            "Secondary ICD10 Code 12", "Secondary ICD10 Code 12 Description",
            "Secondary ICD10 Code 13", "Secondary ICD10 Code 13 Description",
            "QTY APPROVED", "Quantity", "Amount Requested", "Approval Status", "GM Decision (subclaim level)",
            "Submitter User Note", "Patient DOB", "Patient Gender"
        ]
        data = data[desired_order]

        # Write the standardized data to the output file
        data.to_csv(outputFilePath, index=False)
        return outputFilePath
    
    def convertFromStandardFormat(self, inputFilePath, outputFilePath):
        # Implement conversion logic from standard format to Insurance Company 1 format
        data = pd.read_csv(inputFilePath)

        # Mapping columns from standard format to DIG format
        column_mapping = {
            "Invoice Number": "Claim #*",
            "Patient ID": "Member ID*",
            "Procedure Date": "Date*",
            "CPT Code": "CPT code*",
            "CPT Code Description": "CPT Description",
            "Principal ICD10 Code": "Primary Diagnosis ICD 10 code*",
            "Principal ICD10 Code Description": "Primary Diagnosis ICD 10 description ",
            "Secondary ICD10 Code 1": "Secondary Diagnosis 1 - ICD 10 code",
            "Secondary ICD10 Code 1 Description": "Secondary Diagnosis 1 - ICD 10 code description ",
            "Secondary ICD10 Code 2": "Secondary Diagnosis 2 - ICD 10 code",
            "Secondary ICD10 Code 2 Description": "Secondary Diagnosis 2 - ICD 10 code description ",
            "Secondary ICD10 Code 3": "Secondary Diagnosis 3 - ICD 10 code",
            "Secondary ICD10 Code 3 Description": "Secondary Diagnosis 3 - ICD 10 code description ",
            "Secondary ICD10 Code 4": "Secondary Diagnosis 4 - ICD 10 code",
            "Secondary ICD10 Code 4 Description": "Secondary Diagnosis 4 - ICD 10 code description ",
            "Secondary ICD10 Code 5": "Secondary Diagnosis 5 - ICD 10 code",
            "Secondary ICD10 Code 5 Description": "Secondary Diagnosis 5 - ICD 10 code description ",
            "Secondary ICD10 Code 6": "Secondary Diagnosis 6 - ICD 10 code",
            "Secondary ICD10 Code 6 Description": "Secondary Diagnosis 6 - ICD 10 code description ",
            "Secondary ICD10 Code 7": "Secondary Diagnosis 7 - ICD 10 code",
            "Secondary ICD10 Code 7 Description": "Secondary Diagnosis 7 - ICD 10 code description ",
            "Secondary ICD10 Code 8": "Secondary Diagnosis 8 - ICD 10 code",
            "Secondary ICD10 Code 8 Description": "Secondary Diagnosis 8 - ICD 10 code description ",
            "Secondary ICD10 Code 9": "Secondary Diagnosis 9 - ICD 10 code",
            "Secondary ICD10 Code 9 Description": "Secondary Diagnosis 9 - ICD 10 code description ",
            "Secondary ICD10 Code 10": "Secondary Diagnosis 10 - ICD 10 code",
            "Secondary ICD10 Code 10 Description": "Secondary Diagnosis 10 - ICD 10 code description ",
            "Secondary ICD10 Code 11": "Secondary Diagnosis 11 - ICD 10 code",
            "Secondary ICD10 Code 11 Description": "Secondary Diagnosis 11 - ICD 10 code description ",
            "QTY APPROVED": "QTY APPROVED",
            "Quantity": "QTY CLAIMED",
            "Approval Status": "Approval Status ",
            "GM Decision (subclaim level)": "GM Decision"
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Quantity*": "",
            "Unnamed: 34": ""
        }
        for col_name, col_value in additional_columns.items():
            data[col_name] = col_value

        desired_order = [
            "Claim #*", "Member ID*", "Date*", "CPT code*", "CPT Description", "Quantity*",
            "Primary Diagnosis ICD 10 code*", "Primary Diagnosis ICD 10 description ",
            "Secondary Diagnosis 1 - ICD 10 code", "Secondary Diagnosis 1 - ICD 10 code description ",
            "Secondary Diagnosis 2 - ICD 10 code", "Secondary Diagnosis 2 - ICD 10 code description ",
            "Secondary Diagnosis 3 - ICD 10 code", "Secondary Diagnosis 3 - ICD 10 code description ",
            "Secondary Diagnosis 4 - ICD 10 code", "Secondary Diagnosis 4 - ICD 10 code description ",
            "Secondary Diagnosis 5 - ICD 10 code", "Secondary Diagnosis 5 - ICD 10 code description ",
            "Secondary Diagnosis 6 - ICD 10 code", "Secondary Diagnosis 6 - ICD 10 code description ",
            "Secondary Diagnosis 7 - ICD 10 code", "Secondary Diagnosis 7 - ICD 10 code description ",
            "Secondary Diagnosis 8 - ICD 10 code", "Secondary Diagnosis 8 - ICD 10 code description ",
            "Secondary Diagnosis 9 - ICD 10 code", "Secondary Diagnosis 9 - ICD 10 code description ",
            "Secondary Diagnosis 10 - ICD 10 code", "Secondary Diagnosis 10 - ICD 10 code description ",
            "Secondary Diagnosis 11 - ICD 10 code", "Secondary Diagnosis 11 - ICD 10 code description ",
            "QTY APPROVED", "QTY CLAIMED", "Approval Status ", "GM Decision", "Unnamed: 34"
        ]
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath