import pandas as pd

class BabyNamesProject(object):

    # Header Names
    header_names = ('Name','Sex','Number',)

    def __init__(self, file_name, separator=None) -> None:
        '''
            Constructor
        '''
        self._file_name = file_name
        self._separator = separator

    @property
    def file_name(self):
        return self._file_name
    
    @file_name.setter
    def file_name(self, new_filename):
        if not new_filename:
            raise ValueError('Filename cannot be empty')
        self._file_name = new_filename

    @property
    def separator(self):
        return self._separator
    
    @separator.setter
    def separator(self, new_separator):
        self._separator = new_separator

    @staticmethod
    def read_file(function, file_name, separator, header_names):
        '''
            This is a static method that takes a pandas read function,
            the file_name, separator, and header names as input. The
            method returns a DataFrame if the file is valid and a File
            not Found Error if it is not.
        '''
        try:
            df = function(file_name, sep=separator, names=header_names)
            return df
        except FileNotFoundError:
            print('File Not Found')


    def load_data(self):
        '''
            This method returns the dataframe, an error if it
            cannot read the file extension, and a file not found
            error if the file cannot be read
        '''
        # Set the output datadrame to None
        df = None
        # Set the file type to None
        file_type = None
        # Check for index error exception
        # when getting the file extension
        try:
            file_type = self.file_name.split('.')[-1]
        except IndexError:
            print('Not a valid file')
        # Return the dataframe depending on the input file
        # For this task, the file is a text file
        match file_type:
            case 'txt':
                df = self.read_file(pd.read_csv, self.file_name, separator=self.separator, header_names=self.header_names)
            case 'csv':
                df = self.read_file(pd.read_csv, self.file_name, separator=self.separator, header_names=self.header_names)
            case 'xlsx':
                df = self.read_file(pd.read_excel, self.file_name, separator=self.separator, header_names=self.header_names)
        return df
    

    def display_data(self):
        '''
            This method displays the 
            first ten rows of baby names data. 
        '''
        df = self.load_data()
        return df.head(10).to_markdown()
    

    def number_rows_cols(self):
        '''
            This method displays the number of rows
            and columns in the dataframe
        '''
        df = self.load_data();
        rows, cols = df.shape
        return (rows, cols)


    def total_babies_born(self):
        '''
            This method calculates the total
            number of babies born
        '''
        df = self.load_data()
        # Get the Number header name
        number = self.header_names[-1]
        # Calculate the sum
        return df[number].sum()
    

    def total_babies_born_by_sex(self):
        '''
            This method groups the data into boys and girls
            and calculates the individual sum of boys and 
            girls
        '''
        sex = self.header_names[1] # Get the Sex header name
        number = self.header_names[-1] # Get the Number header name
        df = self.load_data() # Get the data
        # Group the data by the sex and calculate the sum from the Number column
        df_sex_group = df.groupby(sex)[number].sum().reset_index()
        boys = df_sex_group.iloc[1]['Number']
        girls = df_sex_group.iloc[0]['Number']
        return (boys, girls)
    

    def check_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be empty')
        # Set found initially to False
        found = False
        # Get the Name header column name
        name_col = self.header_names[0]
        # Get the dataframe
        df = self.load_data()
        # Get the Name column
        names = df[name_col]
        # Check if the first letter of the name to be checked is uppercase,
        if not new_name[0].isupper():
            # if it is not, convert the first letter to uppercase and add the remaining letters
            new_name = new_name[0].upper() + new_name[1:].lower()
        else:
            new_name = new_name[0] + new_name[1:].lower()
        # Check if the name to be searched for is in the list of names
        if new_name in list(names):
            # Set found to True
            found = True
        return found
    
    def percentage_boys_girls(self):
        '''
            This method calculates the percentage total of the boys 
            and the girls
        '''
        # Get the total number of the babies born grouped by sex
        boys_total, girls_total = self.total_babies_born_by_sex()
        # Get the total of the babies born
        total_babies_born = self.total_babies_born()
        # Calculate the percentage of boys born
        percentage_boys = round((boys_total / total_babies_born) * 100.0, 2)
        # Calculate the percentage of girls born
        percentage_girls = round((girls_total / total_babies_born) * 100.0, 2)
        # Return
        return (percentage_boys, percentage_girls)
    
    
    def top_names(self):
        '''
            This method outputs a dataframe with
            the top five baby names given
        '''
        # Get the Name header column name
        name = self.header_names[0]
        # Get the sex header column name
        sex = self.header_names[1]
        # Get the Number header column name
        number = self.header_names[2]
        # Create a dictionary with list values to hold the top names
        table = {'Top Boys Names': [], 'Top Girls Names': []}
        # Get the data
        df = self.load_data()
        # Get the five top names grouped by sex
        top_data = df.set_index(name).groupby(sex)[number].nlargest(5).reset_index()
        # Loop through the data
        for value in range(len(top_data)):
            # Get each value of the Sex column and check if 'M'
            if top_data.iloc[value][self.header_names[1]] == 'M':
                # Append the names to the Top Boys Names section in the dictionary
                table['Top Boys Names'].append(top_data.iloc[value][self.header_names[0]])
            else:
                # Else Append the names to the Top Girls Names section in the dictionary
                table['Top Girls Names'].append(top_data.iloc[value][self.header_names[0]])
        # Return the dictionary as a dataframe
        return pd.DataFrame(table)
    

    def write_to_excel(self):
        '''
            This method writes the top five baby names to
            an excel spreadsheet
        '''
        # Get the top names data
        df_top_names = self.top_names()
        # Export to an excel file
        df_top_names.to_excel("top_names.xlsx")