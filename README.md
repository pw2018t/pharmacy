# Description 
The script calculate the summary metrics for the pharmacy data. The summary metrics include the count of individual drugs and total sales price. 
1. [Script Description](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Instructions](README.md#instructions)
4. [Output](README.md#output)

# Description
We are provided a clean dataset of prescriptions data from a pharmacy database (Centers for Medicare & Medicaid Services).
We are required to generate a list of all the drugs sold by that pharmacy alongwith information related to the no: of prescribers that purchased these drugs and the total cost for each of these drugs. 

# Input Dataset
The original dataset provided contains over 24 million cleaned and simplified records related to prescriptions including prescribers, name of the drug and drug cost.

# Output Dataset
The output file 'top_cost_drug.txt' displays a list of all the drugs, no: of drug prescribers and total cost for those drugs. This list displays drugs with the highest total cost at the top.

# Scripts
Script to generate the summary metrics around the pharmacy input is located in the src folder.

To execute the script:

    1.) clone the repository with below command
      git clone "https://github.com/pw2018t/pharmacy.git"
      
    2.) Go to the pharmacy directory
       cd pharmacy
       
    3.) To test the large file place the new file under input folder
    
    4.) provide the large input file location with filename in run.sh script and output location and filename.
      ./src/pharmacy_sales_summary.py {input file location/filename} {output file location/filename}
    
    5.)run the script with the below command
        bash run.sh



