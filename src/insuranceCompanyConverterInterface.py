from abc import ABC, abstractmethod
import re
import pandas as pd

class InsuranceCompanyConverterInterface(ABC):
    def count_columns_with_phrase(self, csv_file_path, pattern):
        """
        Function to count the number of columns matching a regular expression pattern.
        """
        # Read the first row of the CSV file to get the header
        df = pd.read_csv(csv_file_path, nrows=1)
        header = df.columns
        
        # Compile the regular expression pattern
        regex = re.compile(pattern)
        
        # Count the columns matching the pattern
        count = sum(1 for col_name in header if regex.search(col_name))
        
        return count
    
    def generate_column_mapping(self, column_mapping, 
                                secon_diag_key, secon_diag_value,
                                secondary_diagnosis_count,
                                secon_diag_desc_key=None, secon_diag_desc_value=None):
        """
        Function to dynamically generate the column mapping dictionary
        based on the count of columns containing a common phrase.
        """
        
        # Add dynamically generated Secondary Diagnosis columns to the mapping
        for i in range(1, secondary_diagnosis_count + 1):
            column_mapping[secon_diag_key.format(i)] = secon_diag_value.format(i)
            if (secon_diag_desc_key != None and secon_diag_desc_value != None):
                column_mapping[secon_diag_desc_key.format(i)] = secon_diag_desc_value.format(i)

        return
    
    def generate_desired_order(self, base_order, insert_index, 
                               secondary_diagnosis_count,
                               secon_col_name, secon_desc_col_name=None):
        """
        Function to generate the desired order of columns dynamically,
        considering the number of secondary ICD10 codes, while preserving the original order.
        """
        
        # Generate the column names for secondary ICD10 codes and their descriptions
        for i in range(secondary_diagnosis_count, 0, -1):
            base_order.insert(insert_index, secon_col_name.format(i))
            if (secon_desc_col_name != None):
                base_order.insert(insert_index + 1, secon_desc_col_name.format(i))
        
        return

    @abstractmethod
    def parseToStandardFormat(self, inputFilePath, outputFilePath):
        pass
    
    @abstractmethod
    def convertFromStandardFormat(self, inputFilePath, outputFilePath):
        pass