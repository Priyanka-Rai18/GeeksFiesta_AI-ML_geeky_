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
 
    df=pd.read_csv("/content/train - train (2).csv")
### Step 3: Handling the missing data
 Data can be missing for a variety of reasons and must be handled in such a way that it does not impair the performance of our model. We used interpolation with backfilling method to replace the missing data in this case.
 interpolation Formula: y=y1+ (x-x1)(y2-y1)/(x2-x1) 
 where, y= linear interpolation value
        x= independent variable
    x1,y1= values of the function at one point
    x2,y2= values of the function at another point
    
    df=df.interpolate()
    df=df.fillna(method="bfill")
    df.head(8)
### Step 4: Encoding categorical data 
 Categorical data variable that contains level values rather than numeric values. the number of possible values is often limited to a fixed set. For example here the wind_direction column cannot be used in the mathematical equation of the model so we need to encode these variables into numbers. To achieve this we import the pandas library and use the get_dummies function.

    dummies = pd.get_dummies(df['wind_direction'])
    df = df.drop('wind_direction',1)
    df = pd.concat([df, dummies], axis=1)
### Step 5: Replacing the outliers
 
 
 
### Step 6: Feature scaling:
 High magnitude features will be given more weight in the distance calculation than low magnitude features. Done importing maxminscaler() from sklearn.processing.

    from sklearn.preprocessing import MinMaxScaler
    scaling = MinMaxScaler()
    df[['year','month','day','hour','PM2.5','temperature','pressure']]=scaling.fit_transform(df[['year','month','day','hour','PM2.5','temperature','pressure']])

 
     
