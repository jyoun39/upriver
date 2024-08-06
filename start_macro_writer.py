#def start_macro_writer(num_columns,case_name, directory_path_local,run):

def start_macro_writer(row_index, general):
    import os
    print("\n")
    print(f"creating java file for {general.case_name[row_index]}...")
    java_code = '''
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;

public class '''+general.case_name[row_index]+''' extends StarMacro {
    public void execute() {'''
    
    for column_num in range(general.num_columns):
        java_code = java_code + '''\n       execute'''+ str(column_num) +'''();'''

    if general.run == 1:
        java_code = java_code + '''\n       executerun();\n       }'''
    elif general.run == 0:
        java_code = java_code + '''\n   }'''

    # Path to the new Java file
    case_directory = general.directory_path_local + general.case_name[row_index]

    os.makedirs(case_directory, exist_ok=True)
    print(f"Directory '{case_directory}' created successfully")
    file_content_path = general.directory_path_local + general.case_name[row_index]+"\\"+general.case_name[row_index]+".java"

    # Open the file in write mode and write the content
    try:
        with open(file_content_path, 'w') as file:
            file.write(java_code)
        print(f"Java code successfully written to {file_content_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")