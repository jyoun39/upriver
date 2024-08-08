#def append_macro_writer(case_name,column_index,column_name,column_value,directory_path_local,end,run):

def append_macro_writer (row_index, parameter_to_add, batch,general):
  
  java_code ="" #start with blank

  for column_index in range(len(parameter_to_add)):
    try:
      sanity_check = batch.column_data[parameter_to_add[column_index]][row_index]
    except:
      print("Error: parameter_to_add does not match batch spreadsheet headers")
      
  for column_index in range(len(parameter_to_add)):
    end = False

    if column_index == (len(parameter_to_add) - 1):
      end = True

    print(f"Adding parameter {parameter_to_add[column_index]} of value {batch.column_data[parameter_to_add[column_index]][row_index]} for {batch.column_data['case_name'][row_index]}...")
    java_code = java_code + '''
  private void execute'''+str(column_index)+'''() {

    Simulation simulation_0 = 
      getActiveSimulation();

    simulation_0.get(GlobalParameterManager.class).createGlobalParameter(ScalarGlobalParameter.class, "Scalar");

    ScalarGlobalParameter scalarGlobalParameter_6 = 
      ((ScalarGlobalParameter) simulation_0.get(GlobalParameterManager.class).getObject("Scalar"));

    scalarGlobalParameter_6.setPresentationName("'''+str(parameter_to_add[column_index])+'''");

    Units units_0 = 
      ((Units) simulation_0.getUnitsManager().getObject(""));

    scalarGlobalParameter_6.getQuantity().setValueAndUnits('''+str(batch.column_data[parameter_to_add[column_index]][row_index])+''', units_0);
  }
'''

  if end == True:
    if general.run == True:
      java_code = java_code+'''
  private void executerun() {
    Simulation simulation_0 = 
      getActiveSimulation();
    simulation_0.getSimulationIterator().run();
  }
}'''
    if general.run == False:
      java_code = java_code + "\n }"

  # Path to the new Java file
  file_content_path = general.directory_path_local+batch.column_data['case_name'][row_index]+"\\"+batch.column_data['case_name'][row_index]+".java"

  # Open the file in write mode and write the content
  try:
    with open(file_content_path, 'a') as file:
      file.write(java_code)
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")