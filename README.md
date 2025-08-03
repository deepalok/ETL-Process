# ETL-Process
<h3>Acquiring and Processing Information on the World's Largest Banks</h3>

<h3>Scenario</h3>
A multi-national firm has hired you as a data engineer. Your job is to access and process data as per requirements.
Your boss asked you to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, you need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available to you as a CSV file. You should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.

<h3>Directions</h3>

1.	Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
2.	Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
3.	Write a function to load the transformed data frame to an output CSV file.
4.	Write a function to load the transformed data frame to an SQL database server as a table.
5.	Write a function to run queries on the database table.
6.	Run the following queries on the database table:
a. Extract the information for the London office, that is Name and MC_GBP_Billion
b. Extract the information for the Berlin office, that is Name and MC_EUR_Billion
c. Extract the information for New Delhi office, that is Name and MC_INR_Billion
7.	Write a function to log the progress of the code.
8.	While executing the data initialization commands and function calls, maintain appropriate log entries.
<br>

<table>
  <tbody>
    <tr>
      <td>Parameter</td>
      <td>Value</td>
    </tr>
    <tr>
      <td>Code name</td>
      <td>banks_project.py</td>
    </tr>
    <tr>
      <td>Data URL</td>
      <td>https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks</td>
    </tr>
    <tr>
      <td>Exchange rate CSV path</td>
      <td>https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv</td>
    </tr>
    <tr>
      <td>Table Attributes (upon Extraction only)</td>
      <td>Name, MC_USD_Billion</td>
    </tr>
    <tr>
      <td>Table Attributes (final)</td>
      <td>Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion</td>
    </tr>
    <tr>
      <td>Output CSV Path</td>
      <td>./Largest_banks_data.csv</td>
    </tr>
    <tr>
      <td>Database name</td>
      <td>Banks.db</td>
    </tr>
    <tr>
      <td>Table name</td>
      <td>Largest_banks</td>
    </tr>
    <tr>
      <td>Log file</td>
      <td>code_log.txt</td>
    </tr>
  </tbody>
</table>	
<br>	

<h3><b>Project tasks</b></h3>

#Task 1:
Write a function log_progress() to log the progress of the code at different stages in a file code_log.txt. Use the list of log points provided to create log entries as every stage of the code.

#Task 2:
Extract the tabular information from the given URL under the heading 'By market capitalization' and save it to a dataframe.
a. Inspect the webpage and identify the position and pattern of the tabular information in the HTML code
b. Write the code for a function extract() to perform the required data extraction.
c. Execute a function call to extract() to verify the output.

#Task 3:
Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
a. Write the code for a function transform() to perform the said task.
b. Execute a function call to transform() and verify the output.

#Task 4:
Load the transformed dataframe to an output CSV file. Write a function load_to_csv(), execute a function call and verify the output.

#Task 5:
Load the transformed dataframe to an SQL database server as a table. Write a function load_to_db(), execute a function call and verify the output.

#Task 6:
Run queries on the database table. Write a function run_queries(), execute a given set of queries and verify the output.

<br>

#Task 7:
Verify that the log entries have been completed at all stages by checking the contents of the file code_log.txt.
