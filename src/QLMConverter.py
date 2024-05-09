import re
import pandas as pd

from insuranceCompanyConverterInterface import InsuranceCompanyConverterInterface

class QLMConverter(InsuranceCompanyConverterInterface):
    def generate_column_mapping_suffex_key(self, column_mapping, 
                                secon_diag_key_format, secon_diag_value_format,
                                secondary_diagnosis_count,
                                secon_diag_desc_key_format=None, secon_diag_desc_value_format=None):
        """
        Function to dynamically generate the column mapping dictionary
        based on the count of columns containing a common phrase.
        """
        
        # Add dynamically generated Secondary Diagnosis columns to the mapping
        for i in range(1, secondary_diagnosis_count + 1):
            # Determine the suffix for the ordinal indicator
            if (i+1) % 10 == 1 and (i+1) != 11:
                suffix = "st"
            elif (i+1) % 10 == 2 and (i+1) != 12:
                suffix = "nd"
            elif (i+1) % 10 == 3 and (i+1) != 13:
                suffix = "rd"
            else:
                suffix = "th"
            
            # Add the column mappings with the appropriate suffix
            secon_diag_key = secon_diag_key_format.format(i+1, suffix)
            column_mapping[secon_diag_key] = secon_diag_value_format.format(i)
            if secon_diag_desc_key_format is not None and secon_diag_desc_value_format is not None:
                secon_diag_desc_key = secon_diag_desc_key_format.format(i+1, suffix)
                column_mapping[secon_diag_desc_key] = secon_diag_desc_value_format.format(i)

        return column_mapping
    
    def generate_column_mapping_suffex_value(self, column_mapping, 
                                secon_diag_key_format, secon_diag_value_format,
                                secondary_diagnosis_count,
                                secon_diag_desc_key_format=None, secon_diag_desc_value_format=None):
        """
        Function to dynamically generate the column mapping dictionary
        based on the count of columns containing a common phrase.
        """
        
        # Add dynamically generated Secondary Diagnosis columns to the mapping
        for i in range(1, secondary_diagnosis_count + 1):
            # Determine the suffix for the ordinal indicator
            if (i+1) % 10 == 1 and (i+1) != 11:
                suffix = "st"
            elif (i+1) % 10 == 2 and (i+1) != 12:
                suffix = "nd"
            elif (i+1) % 10 == 3 and (i+1) != 13:
                suffix = "rd"
            else:
                suffix = "th"
            
            # Add the column mappings with the appropriate suffix
            secon_diag_key = secon_diag_key_format.format(i)
            column_mapping[secon_diag_key] = secon_diag_value_format.format(i+1, suffix)
            if secon_diag_desc_key_format is not None and secon_diag_desc_value_format is not None:
                secon_diag_desc_key = secon_diag_desc_key_format.format(i)
                column_mapping[secon_diag_desc_key] = secon_diag_desc_value_format.format(i+1, suffix)

        return column_mapping
    
    def generate_desired_order_different_value(self, base_order, insert_index, 
                            secondary_diagnosis_count,
                            secon_col_name_format, secon_desc_col_name_format=None):
        """
        Function to generate the desired order of columns dynamically,
        considering the number of secondary ICD10 codes, while preserving the original order.
        """
        
        # Generate the column names for secondary ICD10 codes and their descriptions
        for i in range(secondary_diagnosis_count, 0, -1):
            # Determine the suffix for the ordinal indicator
            if (i+1) % 10 == 1 and (i+1) != 11:
                suffix = "st"
            elif (i+1) % 10 == 2 and (i+1) != 12:
                suffix = "nd"
            elif (i+1) % 10 == 3 and (i+1) != 13:
                suffix = "rd"
            else:
                suffix = "th"
            
            # Insert the column names with the appropriate suffix
            secon_col_name = secon_col_name_format.format(i + 1, suffix)
            base_order.insert(insert_index, secon_col_name)
            
            if secon_desc_col_name_format is not None:
                secon_desc_col_name = secon_desc_col_name_format.format(i + 1, suffix)
                base_order.insert(insert_index + 1, secon_desc_col_name)

        return
    
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        # Implement parsing logic for Insurance Company 1
        data = pd.read_csv(inputFilePath)

        regex_pattern = r"\d+(st|nd|rd|th) Diag Code"
        secondary_diagnosis_count = self.count_columns_with_phrase(inputFilePath, regex_pattern)

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
            "Quantity": "Quantity",
        }
        secon_diag_key = f"{{}}{{}} Diag Code"
        secon_diag_value = f"Secondary ICD10 Code {{}}"
        self.generate_column_mapping_suffex_key(column_mapping, 
                                    secon_diag_key, secon_diag_value,
                                    secondary_diagnosis_count)

        # Filter columns based on the mapping
        columns_to_keep = list(column_mapping.keys())
        data = data[columns_to_keep]

        # Rename columns based on the mapping
        data.rename(columns=column_mapping, inplace=True)

        # Add additional columns to the DataFrame
        additional_columns = {
            "Clinician Name": "", "Clinician ID": "",
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
            "QTY APPROVED", "Quantity", "Amount Requested", "Approval Status", "GM Decision (subclaim level)",
            "Submitter User Note", "Patient DOB", "Patient Gender"
        ]
        insert_index = desired_order.index("Principal ICD10 Code Description") + 1
        secon_col_name = secon_diag_value
        self.generate_desired_order(desired_order, insert_index, 
                                    secondary_diagnosis_count,
                                    secon_col_name)
        data = data[desired_order]

        # Write the standardized data to the output file
        data.to_csv(outputFilePath, index=False)
        return outputFilePath
    
    def convertFromStandardFormat(self, inputFilePath, outputFilePath):
        # Implement conversion logic from standard format to Insurance Company 1 format
        data = pd.read_csv(inputFilePath)

        regex_pattern = r"Secondary ICD10 Code \d+"
        secondary_diagnosis_count = self.count_columns_with_phrase(inputFilePath, regex_pattern)

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
            "Quantity": "Quantity"
        }
        secon_diag_key = f"Secondary ICD10 Code {{}}" 
        secon_diag_value = f"{{}}{{}} Diag Code"
        self.generate_column_mapping_suffex_value(column_mapping, 
                                    secon_diag_key, secon_diag_value,
                                    secondary_diagnosis_count)


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
            "Primary Diag Code", "Primary Diag Description", "Provider Treat Code",
            "Provider Treat Description", "Quantity", "Gross Claim Amt", "Discount", "Ded/Co-payment",
            "Co-insurance", "Net Payable Amount", "Physician License No.", "Clinic/Specialty",
            "Provider File No.", "Qatar ID",
            "Service Category", "Sub Benefit", "Inpatient Type (M/S)", "Inpatient Admission Date",
            "First Reported Date", "Tooth No", "LMP Date", "Nature of Conception", "CPT Code",
            "Duration (for pharmacy)", "Dosage (for pharmacy)", "Investigation Result", "Chief Compliant"
        ]
        insert_index = desired_order.index("Primary Diag Description") + 1
        secon_col_name = secon_diag_value
        self.generate_desired_order_different_value(desired_order, insert_index,
                                    secondary_diagnosis_count,
                                    secon_col_name)
        data = data[desired_order]

        data.to_csv(outputFilePath, index=False)
        return outputFilePath