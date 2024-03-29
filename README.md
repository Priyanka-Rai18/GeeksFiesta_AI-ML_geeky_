# GeeksFiesta_AI-ML_geeky_
 10 days Hackathon on ML !!

 ## Tools
    Google colab  
 ## Libraries
  This Project needs python and uses the following libraries:
    
    Numpy
    Pandas 
    Matplotlib 
  	Seaborn
    Scikit learn
    Scipy
 ## Introduction| Day 1
  An introduction to machine learning was given, followed by a discussion of the roadmap.
 ## Github repo| Day 2
  We set up a private github repository named as 'GeeksFiesta_AI-ML_geeky_couple' and invited mentors to join as collaborators.
 ## Data Cleaning| Day 3
 ### Aim
    To clean/process the Data, find count of missing values in each column and describe the dataset.
  
### Step 1 : Importing the required libraries

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
 We identified Outliers by creating a Boxplot for each column and observing the range and number of dots or "too far away" points, which are values that deviate more or less than the expected range.
### Step 2: Replacing the outliers
First, we print the outlier's location by specifying the required condition. After that, we set the detected oulier to null and fill it using the **median** approach.

## Data Analysis| Day 4-Day 5
### Step 3: Analysing each column with every column
we found the relationship between each column and all other columns using the **corr()** function of the **pandas** library and then plotting graph using seaborn library.
 
### Step 4: Finding Correlation of 'PM2.5' with rest of the column
we found PM2.5 relation with every column using corr() funtion of pandas.

## Data Visualisation| Day 4-Day 5
### Step 5: Heatmap Visualization
 For Correlation analysis, we used the heatmap method from the seaborn library.
### Step 6: Performing line plot
 We then plotted a Graph for the dataframe using **Pandas** library.
### Step 7: Plotting Boxplot for every column after fixing outliers
 We observed in column "year" and "temperature" have median> mean while in column "month" and "wind_speed" have median<mean.
### Step 8: Performing Boxplot for every column
we then plotted a pairplot with PM2.5 as the x-axis vs each column. And we observed, PM2.5 is constant across all columns.
## Model training and Evaluation| Day 5-Day 6
### Aim
    We have to build and train a model which will predict the quality of air and PM 2.5 concentrations.
### Step 1: Splitting the Dataset
 We splitted the Dataset into 70:30 ratio for training and testing using skicit learn library.
### Step 2: Random Forest Regression| regression-1
 Here, We used the fit method to train our model by importing RandomForestRegressor from sklearn.ensemble.  
### Step 3: Decision Tree Regression| regression-2
 Here, We used the fit method to train our model by importing DecisiontreeRegressor from sklearn.ensemble.
### Step 4: Model Evaluation
 We used R^2 for calculating accuracy and also printed error like mean absolute, squared and root mean squared error.
### Step 5: Testing the model
 Here, we tested out model with the remaning 30% of data which we splitted in the beginning.
### Step 6: Plotting graph of actual vs predicted
 We plotted a graph between the actual values and prediccted values by using matplotlib.
### Step 7: Performance comparision
 Here, we observed that random forest gives more Accuracy i.e (46.35%) than decision tree(30.10%) as shown below. So, we opted random forest regression for our model.
### Step 8: Predicting output on 10 different inputs
 In this step, Our random forest model will provide predictions of PM2.5 concentration for ten alternative inputs to the dataset that we import.
 
## Prediction of PM2.5 on the given Testing dataset| Day 7

### Step 1: Filling the missing values
 At first, We filled the missing values of the given test dataset.
### Step 2: Scaling the test data
 After that, we used feature scaling to scale out the testing dataset.
### Step 3: Predicting PM2.5 concentration
 Then, using our model, we predicted PM2.5 concentrations and added them to our final dataframe.
## Deployment of model using Flask| Day 8- Day 9
http://127.0.0.1:5000/


    

 
     
