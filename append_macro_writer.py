#def append_macro_writer(case_name,column_index,column_name,column_value,directory_path_local,end,run):

def append_macro_writer (row_index,column_index,general,end):
  print(f"Adding parameter {general.headers[column_index+1]} of value {general.batch_parameter_data.iloc[row_index,column_index]} for {general.case_name[row_index]}...")
  java_code = '''
  private void execute'''+str(column_index)+'''() {

    Simulation simulation_0 = 
      getActiveSimulation();

    simulation_0.get(GlobalParameterManager.class).createGlobalParameter(ScalarGlobalParameter.class, "Scalar");

    ScalarGlobalParameter scalarGlobalParameter_6 = 
      ((ScalarGlobalParameter) simulation_0.get(GlobalParameterManager.class).getObject("Scalar"));

    scalarGlobalParameter_6.setPresentationName("'''+general.headers[column_index]+'''");

    Units units_0 = 
      ((Units) simulation_0.getUnitsManager().getObject(""));

    scalarGlobalParameter_6.getQuantity().setValueAndUnits('''+str(general.batch_parameter_data.iloc[row_index,column_index])+''', units_0);
  }
'''

  if end == 1:
    if general.run == 1:
      java_code = java_code+'''
  private void executerun() {
    Simulation simulation_0 = 
      getActiveSimulation();
    simulation_0.getSimulationIterator().run();
  }
}'''
    if general.run == 0:
      java_code = java_code + "\n }"

  # Path to the new Java file
  file_content_path = general.directory_path_local+general.case_name[row_index]+"\\"+general.case_name[row_index]+".java"

  # Open the file in write mode and write the content
  try:
    with open(file_content_path, 'a') as file:
      file.write(java_code)
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")