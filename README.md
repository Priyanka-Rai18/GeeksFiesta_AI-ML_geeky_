# GeeksFiesta_AI-ML_geeky_couple
 10 days Hackathon of ML !!
 ## Meet the Team
 ### geeky_couple
    Priyanka Rai (Team leader) & Sandeep Swain
 ## Using
    Python3   
 ## Introduction| Day 1
  An introduction to machine learning was given, followed by a discussion of the roadmap.
 ## Github repo| Day 2
  We set up a private github repository named as 'GeeksFiesta_AI-ML_geeky_couple' and invited mentors to join as collaborators.
 ## Data Cleaning| Day 3
 ### Aim
  To clean/process the Data, find count of missing values in each column and describe the dataset.
  
### Step 1 : Importing the required libraries
    Numpy: It has mathematical functions in it.
    Pandas: Its purpose is to import and manage the dataset.
    Matplotlib 
  	Seaborn
    Scikit learn
    Scipy
### Step 2: Importing the dataset
 The majority of data states are available in.csv format. The CSV file format is used to store tabular data in plain text. To read a local CSV file as a dataframe, we used the  Pandas library's read_csv function.
 
### Step 3: Handling the missing data
 Data can be missing for a variety of reasons and must be handled in such a way that it does not impair the performance of our model. We used backfilling method to replace the missing data in this case.
As the data set is already sorted concerning hours, day, month, year. So if we fill the missing values with mean-value, then the deviation would increase. Hence error would increase. The given features would be almost the same in the next hour also. For example, the temperature is 1.9 at a particular hour, then the next hour if the temperature would be around 1.9 only, not 14.356532039734322. So we opted backfilling method.

### Step 4: Encoding categorical data 
 Categorical data variable that contains level values rather than numeric values. the number of possible values is often limited to a fixed set. For example here the wind_direction column cannot be used in the mathematical equation of the model so we need to encode these variables into numbers. To achieve this we import the pandas library and use the get_dummies function.
        
### Step 5: Feature scaling
 High magnitude features will be given more weight in the distance calculation than low magnitude features. In order, to avoid this we used maxminscaler() from sklearn.processing.
## Data PreProcessing| Day 4-Day 5
### Step 1: Detecting outlier 
### Step 2: Replacing the outliers

## Data Analysis| Day 4-Day 5
### Step 1: Analysing each column with every column
### Step 2: Finding Correlation of 'PM2.5' with rest of the column

## Data Visualisation| Day 4-Day 5
### Step 1: Heatmap Visualization
 For Correlation analysis, we used the heatmap method from the seaborn library.
### Step 2: Performing line plot
### Step 3: Performing Boxplot for every column


    

 
     
