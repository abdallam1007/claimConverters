import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class QLMConverter(InsuranceCompanyConverterInterface):
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)

        # Mapping columns from QLM format to standard format
        column_mapping = {
            "Invoice No.": "Invoice Number",
            "MEMBER ID (MEM)": "Patient ID",
            "Patient Name": "Patient Name",
            "Service Date": "Procedure Date",
            "CPT Code": "CPT Code",
            "Chief Compliant": "CPT Code Description",
            "Primary Diag Code": "Principal ICD10 Code",
            "Primary Diag Description": "Principal ICD10 Code Description",
            "2nd Diag Code": "Secondary ICD10 Code 1",
            "3rd Diag Code": "Secondary ICD10 Code 2",
            "4th Diag Code": "Secondary ICD10 Code 3",
            "5th Diag Code": "Secondary ICD10 Code 4",
            "Quantity": "Quantity",
        }

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Clinician Name": "", "Clinician ID": "", "Secondary ICD10 Code 1": "", 
            "Secondary ICD10 Code 1 Description": "", "Secondary ICD10 Code 2 Description": "", 
            "Secondary ICD10 Code 3 Description": "", "Secondary ICD10 Code 4 Description": "",
            "Secondary ICD10 Code 5": "", "Secondary ICD10 Code 5 Description": "",
            "Secondary ICD10 Code 6": "", "Secondary ICD10 Code 6 Description": "",
            "Secondary ICD10 Code 7": "", "Secondary ICD10 Code 7 Description": "",
            "Secondary ICD10 Code 8": "", "Secondary ICD10 Code 8 Description": "",
            "Secondary ICD10 Code 9": "", "Secondary ICD10 Code 9 Description": "",
            "Secondary ICD10 Code 10": "", "Secondary ICD10 Code 10 Description": "",
            "Secondary ICD10 Code 11": "", "Secondary ICD10 Code 11 Description": "",
            "Secondary ICD10 Code 12": "", "Secondary ICD10 Code 12 Description": "",
            "Secondary ICD10 Code 13": "", "Secondary ICD10 Code 13 Description": "",
            "QTY APPROVED": "", "Amount Requested": "", "Approval Status": "", "GM Decision (subclaim level)": "", 
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

        # Mapping columns from standard format to QLM format
        column_mapping = {
            "Invoice Number": "Invoice No.",
            "Patient ID": "MEMBER ID (MEM)",
            "Patient Name": "Patient Name",
            "Procedure Date": "Service Date",
            "CPT Code": "CPT Code",
            "CPT Code Description": "Chief Compliant",
            "Principal ICD10 Code": "Primary Diag Code",
            "Principal ICD10 Code Description": "Primary Diag Description",
            "Secondary ICD10 Code 1": "2nd Diag Code",
            "Secondary ICD10 Code 2": "3rd Diag Code",
            "Secondary ICD10 Code 3": "4th Diag Code",
            "Secondary ICD10 Code 4": "5th Diag Code",
            "Quantity": "Quantity"
        }


        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "QLM Visit No./ Barcode No.": "", "Benefit": "",
            "Service Type (I/O)": "", "Pre-Approval Code": "", "Provider Treat Code": "",
            "Provider Treat Description": "", "Gross Claim Amt": "", "Discount": "", "Ded/Co-payment": "",
            "Co-insurance": "", "Net Payable Amount": "", "Physician License No.": "",
            "Clinic/Specialty": "", "Provider File No.": "", "Qatar ID": "", "Service Category": "",
            "Sub Benefit": "", "Inpatient Type (M/S)": "", "Inpatient Admission Date": "",
            "First Reported Date": "", "Tooth No": "", "LMP Date": "", "Nature of Conception": "",
            "Duration (for pharmacy)": "", "Dosage (for pharmacy)": "", "Investigation Result": ""
        }

        for col_name, col_value in additional_columns.items():
            data[col_name] = col_value


        desired_order = [
            "QLM Visit No./ Barcode No.", "MEMBER ID (MEM)", "Patient Name",
            "Benefit", "Service Type (I/O)", "Service Date", "Invoice No.", "Pre-Approval Code",
            "Primary Diag Code", "Primary Diag Description", "2nd Diag Code", "Provider Treat Code",
            "Provider Treat Description", "Quantity", "Gross Claim Amt", "Discount", "Ded/Co-payment",
            "Co-insurance", "Net Payable Amount", "Physician License No.", "Clinic/Specialty",
            "Provider File No.", "Qatar ID", "3rd Diag Code", "4th Diag Code", "5th Diag Code",
            "Service Category", "Sub Benefit", "Inpatient Type (M/S)", "Inpatient Admission Date",
            "First Reported Date", "Tooth No", "LMP Date", "Nature of Conception", "CPT Code",
            "Duration (for pharmacy)", "Dosage (for pharmacy)", "Investigation Result", "Chief Compliant"
        ]
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath