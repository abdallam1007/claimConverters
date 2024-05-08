import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class QICConverter(InsuranceCompanyConverterInterface):
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)

        # Mapping columns from QIC format to standard format
        column_mapping = {
            "Claim No": "Invoice Number",
            "Doctor Name": "Clinician Name",
            "CPT Code": "CPT Code",
            "CPT Desc": "CPT Code Description",
            "Diagnosis Code": "Principal ICD10 Code",
            "Diagnosis Name": "Principal ICD10 Code Description",
            "Gender": "Patient Gender"
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Patient ID": "", "Patient Name": "", "Clinician ID": "", "Procedure Date": "",
            "Secondary ICD10 Code 1": "", "Secondary ICD10 Code 1 Description": "",
            "Secondary ICD10 Code 2": "", "Secondary ICD10 Code 2 Description": "",
            "Secondary ICD10 Code 3": "", "Secondary ICD10 Code 3 Description": "",
            "Secondary ICD10 Code 4": "", "Secondary ICD10 Code 4 Description": "",
            "Secondary ICD10 Code 5": "", "Secondary ICD10 Code 5 Description": "",
            "Secondary ICD10 Code 6": "", "Secondary ICD10 Code 6 Description": "",
            "Secondary ICD10 Code 7": "", "Secondary ICD10 Code 7 Description": "",
            "Secondary ICD10 Code 8": "", "Secondary ICD10 Code 8 Description": "",
            "Secondary ICD10 Code 9": "", "Secondary ICD10 Code 9 Description": "",
            "Secondary ICD10 Code 10": "", "Secondary ICD10 Code 10 Description": "",
            "Secondary ICD10 Code 11": "", "Secondary ICD10 Code 11 Description": "",
            "Secondary ICD10 Code 12": "", "Secondary ICD10 Code 12 Description": "",
            "Secondary ICD10 Code 13": "", "Secondary ICD10 Code 13 Description": "",
            "QTY APPROVED": "", "Quantity": "", "Amount Requested": "", "Approval Status": "", 
            "GM Decision (subclaim level)": "", "Submitter User Note": "", "Patient DOB": ""
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

        # Mapping columns from standard format to QIC format
        column_mapping = {
            "Invoice Number": "Claim No",
            "Clinician Name": "Doctor Name",
            "CPT Code": "CPT Code",
            "CPT Code Description": "CPT Desc",
            "Principal ICD10 Code": "Diagnosis Code",
            "Principal ICD10 Code Description": "Diagnosis Name",
            "Patient Gender": "Gender"
        }


        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)


        # Add additional columns to the DataFrame
        additional_columns = {
            "Speciality": "", "In/Out Patient": "", "Invoice No": "", "Nationality": "",
            "Payment Currency": "", "Provider Name": "", "Provider Service Code": "",
            "Provider service Desc": "", "QIC Treatment Desc": "", "Benefit": "",
            "Sub Benefit": "", "Treatment Mode": ""
        }
        for col_name, col_value in additional_columns.items():
            data[col_name] = col_value

        desired_order = [
            "Claim No", "CPT Code", "CPT Desc", "Diagnosis Code", "Diagnosis Name", "Doctor Name",
            "Speciality", "Gender", "In/Out Patient", "Invoice No", "Nationality", "Payment Currency",
            "Provider Name", "Provider Service Code", "Provider service Desc", "QIC Treatment Desc",
            "Benefit", "Sub Benefit", "Treatment Mode"
        ]
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath