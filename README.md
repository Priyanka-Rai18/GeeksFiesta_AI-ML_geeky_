# GeeksFiesta_AI-ML_geeky_couple
 10 days Hackathon of ML !!
 ## Meet the Team
 ### geeky_couple
    Priyanka Rai (Team leader) & Sandeep Swain
 ## Using
    Python3
 ## Data PreProcessing| Day 2
 ### Aim
  To clean/process the Data, find count of missing values in each column and describe the dataset.
  
### Step 1 : Importing the required libraries:
    Numpy: It has mathematical functions in it.
  	 Pandas: Its purpose is to import and manage the dataset.
   	Matplotlib 
  	 Seaborn
    Scikit learn
### Step 2: Importing the dataset
 The majority of data states are available in.csv format. The CSV file format is used to store tabular data in plain text. To read a local CSV file as a dataframe, we use the  Pandas library's read_csv function.
 
### Step 3: Handling the missing data
 Data can be missing for a variety of reasons and must be handled in such a way that it does not impair the performance of our model. We used backfilling method to replace the missing data in this case.

### Step 4: Encoding categorical data 
 Categorical data variable that contains level values rather than numeric values. the number of possible values is often limited to a fixed set. For example here the wind_direction column cannot be used in the mathematical equation of the model so we need to encode these variables into numbers. To achieve this we import the pandas library and use the get_dummies function.

### Step 5: Replacing the outliers
 We start by detecting outliers with the seaborn library and plotting them with the boxplot approach. Then, using required conditions, we assign null to each column's odd values. After that, we used the backfilling approach to fill the null.
        
### Step 6: Feature scaling:
 High magnitude features will be given more weight in the distance calculation than low magnitude features. In order, to avoid this we used maxminscaler() from sklearn.processing.

    

 
     
