import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class AlkootConverter(InsuranceCompanyConverterInterface):
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)

        # Mapping columns from Alkoot format to standard format
        column_mapping = {
            "INVOICE NO.": "Invoice Number",
            "MEMBER ID": "Patient ID",
            "MEMBER NAME": "Patient Name",
            "CLINICIAN NAME": "Clinician Name",
            "CLINICIAN ID": "Clinician ID",
            "DATE OF TREATMENT /ADMISSION": "Procedure Date",
            "CPT CODE": "CPT Code",
            "SYMPTOMS": "CPT Code Description",
            "PRINCIPAL ICD CODE": "Principal ICD10 Code",
            "ICD DESCRIPTION": "Principal ICD10 Code Description",
            "SECONDARY ICD CODE 1": "Secondary ICD10 Code 1",
            "SECONDARY ICD CODE 2": "Secondary ICD10 Code 2",
            "SECONDARY ICD CODE 3": "Secondary ICD10 Code 3",
            "SECONDARY ICD CODE 4": "Secondary ICD10 Code 4",
            "SECONDARY ICD CODE 5": "Secondary ICD10 Code 5",
            "QUANTITY": "Quantity",
            "AMOUNT CLAIMED": "Amount Requested",
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Secondary ICD10 Code 1 Description": "", "Secondary ICD10 Code 2 Description": "",
            "Secondary ICD10 Code 3 Description": "", "Secondary ICD10 Code 4 Description": "",
            "Secondary ICD10 Code 5 Description": "",
            "Secondary ICD10 Code 6": "", "Secondary ICD10 Code 6 Description": "",
            "Secondary ICD10 Code 7": "", "Secondary ICD10 Code 7 Description": "",
            "Secondary ICD10 Code 8": "", "Secondary ICD10 Code 8 Description": "",
            "Secondary ICD10 Code 9": "", "Secondary ICD10 Code 9 Description": "",
            "Secondary ICD10 Code 10": "", "Secondary ICD10 Code 10 Description": "",
            "Secondary ICD10 Code 11": "", "Secondary ICD10 Code 11 Description": "",
            "Secondary ICD10 Code 12": "", "Secondary ICD10 Code 12 Description": "",
            "Secondary ICD10 Code 13": "", "Secondary ICD10 Code 13 Description": "",
            "QTY APPROVED": "","Approval Status": "", "GM Decision (subclaim level)": "",
            "Submitter User Note": "", "Patient DOB": "", "Patient Gender": ""
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

        # Mapping columns from standard format to Alkoot format
        column_mapping = {
            "Invoice Number": "INVOICE NO.",
            "Patient ID": "MEMBER ID",
            "Patient Name": "MEMBER NAME",
            "Clinician Name": "CLINICIAN NAME",
            "Clinician ID": "CLINICIAN ID",
            "Procedure Date": "DATE OF TREATMENT /ADMISSION",
            "CPT Code": "CPT CODE",
            "CPT Code Description": "SYMPTOMS",
            "Principal ICD10 Code": "PRINCIPAL ICD CODE",
            "Principal ICD10 Code Description": "ICD DESCRIPTION",
            "Secondary ICD10 Code 1": "SECONDARY ICD CODE 1",
            "Secondary ICD10 Code 2": "SECONDARY ICD CODE 2",
            "Secondary ICD10 Code 3": "SECONDARY ICD CODE 3",
            "Secondary ICD10 Code 4": "SECONDARY ICD CODE 4",
            "Secondary ICD10 Code 5": "SECONDARY ICD CODE 5",
            "Quantity": "QUANTITY",
            "Amount Requested": "AMOUNT CLAIMED"
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "S.No": "", "PreApproval No.": "",
            "DATE OF DISCHARGE": "", "SYSTEM OF MEDICINE": "", "BENEFIT TYPE": "", "ENCOUNTER TYPE": "", 
            "FIRST  INCIDENT DATE": "", "FIRST REPORTED DATE": "", "SERVICE DATE": "", "Activity Type": "",
            "INTERNAL  SERVICE CODE": "", "SERVICE DESCRIPTION": "", "Tooth Number (For Dental Only)": "",
            "Date of LMP (For Maternity Only)": "", "Nature Of Conception(For Maternity Only)": "",
            "OBSERVATION": "", "Event Reference Number": ""
        }
        for col_name, col_value in additional_columns.items():
            data[col_name] = col_value

        desired_order = [
            "S.No", "INVOICE NO.", "MEMBER NAME", "MEMBER ID", "PreApproval No.", "DATE OF TREATMENT /ADMISSION",
            "DATE OF DISCHARGE", "SYSTEM OF MEDICINE", "BENEFIT TYPE", "ENCOUNTER TYPE", "CLINICIAN ID",
            "CLINICIAN NAME", "SYMPTOMS", "PRINCIPAL ICD CODE", "ICD DESCRIPTION", "SECONDARY ICD CODE 1",
            "SECONDARY ICD CODE 2", "SECONDARY ICD CODE 3", "SECONDARY ICD CODE 4", "SECONDARY ICD CODE 5",
            "FIRST  INCIDENT DATE", "FIRST REPORTED DATE", "SERVICE DATE", "Activity Type",
            "INTERNAL  SERVICE CODE", "SERVICE DESCRIPTION", "CPT CODE", "AMOUNT CLAIMED", "QUANTITY",
            "Tooth Number (For Dental Only)", "Date of LMP (For Maternity Only)", "Nature Of Conception(For Maternity Only)",
            "OBSERVATION", "Event Reference Number"
        ]
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath