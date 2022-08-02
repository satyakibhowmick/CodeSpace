def NameDoBSalary():
    
    """
    Generates dummy dataset for educational purposes.

    Note: NumPy and Pandas are required to be installed before using this function.
        
    "Name(s)" is/are to be manually entered in the prompted dialogue box.
       
    "DoB" and "Salary" are randomly generated.
    
    
    
    Schema Description for dummy dataset:

     |-- Name: string
     |-- DoB: timestamp
     |-- Salary: double
    """
    
    # Importing required packages.
    
    import numpy as np
    import pandas as pd
    
    # Generating placeholders.
    
    ## Prompt for entering names separated by commas.
    names_string = input("Please enter names separated by commas: ")
    ## Empty dictionary.
    name_dob = {}
    
    # Populating dictionary with "Name" and "DoB".
    
    for i in names_string.split(','):
        name_dob[i.strip().strip('.')] = ((str(np.random.randint(1989,1996,1)) \
                        +str(np.random.randint(1,12,1)) \
                        +str(np.random.randint(1,28,1))). \
                       replace('[','').replace(']',''))
    
    # Generating Pandas DataFrame.
    
    df = pd.DataFrame(name_dob,range(1)).transpose(). \
        reset_index().rename(columns={'index':'Name',0:'DoB'})
    
    # Changing DoB column format to timestamp.
    
    df['DoB'] = pd.to_datetime(df['DoB'], format='%Y%m%d')
    
    # Adding "Salary" column.
    
    df['Salary'] = np.random.rand(len(df)) * 175875
    
    # Generating dataset as csv.
    
    df.to_csv('func_out.csv',index=False)
    
    # Message on execution.
    
    return print("Demo dataset saved in directory as 'func_out.csv'!")