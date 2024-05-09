import re
import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class DIGConverter(InsuranceCompanyConverterInterface):
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)
        
        regex_pattern = re.escape("Secondary Diagnosis") + r"\s+(\d+)\s+-\s+ICD 10 code description"
        secondary_diagnosis_count = self.count_columns_with_phrase(inputFilePath, regex_pattern)

        # Mapping columns from DIG format to standard format
        column_mapping = {
            "Claim #*": "Invoice Number",
            "Member ID*": "Patient ID",
            "Date*": "Procedure Date",
            "CPT code*": "CPT Code",
            "CPT Description": "CPT Code Description",
            "Primary Diagnosis ICD 10 code*": "Principal ICD10 Code",
            "Primary Diagnosis ICD 10 description ": "Principal ICD10 Code Description",
            "QTY APPROVED": "QTY APPROVED",
            "QTY CLAIMED": "Quantity",
            "Approval Status ": "Approval Status",
            "GM Decision": "GM Decision (subclaim level)"
        }
        secon_diag_key = f"Secondary Diagnosis {{}} - ICD 10 code"
        secon_diag_value = f"Secondary ICD10 Code {{}}"
        secon_diag_desc_key = f"Secondary Diagnosis {{}} - ICD 10 code description "
        secon_diag_desc_value = f"Secondary ICD10 Code {{}} Description"
        self.generate_column_mapping(column_mapping, 
                                    secon_diag_key, secon_diag_value,
                                    secondary_diagnosis_count,
                                    secon_diag_desc_key, secon_diag_desc_value)
        
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
            "QTY APPROVED", "Quantity", "Amount Requested", "Approval Status", "GM Decision (subclaim level)",
            "Submitter User Note", "Patient DOB", "Patient Gender"
        ]
        insert_index = desired_order.index("Principal ICD10 Code Description") + 1
        secon_col_name = secon_diag_value
        secon_desc_col_name = secon_diag_desc_value
        self.generate_desired_order(desired_order, insert_index, 
                                    secondary_diagnosis_count,
                                    secon_col_name, secon_desc_col_name)
        data = data[desired_order]

        # Write the standardized data to the output file
        data.to_csv(outputFilePath, index=False)
        return outputFilePath
    
    def convertFromStandardFormat(self, inputFilePath, outputFilePath):
        # Implement conversion logic from standard format to Insurance Company 1 format
        data = pd.read_csv(inputFilePath)

        regex_pattern = r"Secondary ICD10 Code \d+ Description"
        secondary_diagnosis_count = self.count_columns_with_phrase(inputFilePath, regex_pattern)

        # Mapping columns from standard format to DIG format
        column_mapping = {
            "Invoice Number": "Claim #*",
            "Patient ID": "Member ID*",
            "Procedure Date": "Date*",
            "CPT Code": "CPT code*",
            "CPT Code Description": "CPT Description",
            "Principal ICD10 Code": "Primary Diagnosis ICD 10 code*",
            "Principal ICD10 Code Description": "Primary Diagnosis ICD 10 description ",
            "QTY APPROVED": "QTY APPROVED",
            "Quantity": "QTY CLAIMED",
            "Approval Status": "Approval Status ",
            "GM Decision (subclaim level)": "GM Decision"
        }
        secon_diag_key = f"Secondary ICD10 Code {{}}" 
        secon_diag_value = f"Secondary Diagnosis {{}} - ICD 10 code"
        secon_diag_desc_key = f"Secondary ICD10 Code {{}} Description"
        secon_diag_desc_value = f"Secondary Diagnosis {{}} - ICD 10 code description "
        self.generate_column_mapping(column_mapping, 
                                    secon_diag_key, secon_diag_value,
                                    secondary_diagnosis_count,
                                    secon_diag_desc_key, secon_diag_desc_value)

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
            "QTY APPROVED", "QTY CLAIMED", "Approval Status ", "GM Decision", "Unnamed: 34"
        ]
        insert_index = desired_order.index("Primary Diagnosis ICD 10 description ") + 1
        secon_col_name = secon_diag_value
        secon_desc_col_name = secon_diag_desc_value
        self.generate_desired_order(desired_order, insert_index,
                                    secondary_diagnosis_count,
                                    secon_col_name, secon_desc_col_name)
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath