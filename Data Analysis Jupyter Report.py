#!/usr/bin/env python
# coding: utf-8

# <br>
# 
# ## **Data Analysis of Galaxy Data using Fixed Magnitude and Fixed Diameter**
# 
# <br>

# ### **Domain-Specific Area and Objectives**
# 

# **Domain Area**
# <br>
# 
# The Domain area will be Observational Cosmology, focusing specifically on the motion of spiral galaxies to model the expansion rate of the universe as a continuation from a previous project. Linear regression is used quite often in astronomy, as it can handle large datasets quickly and produce visualizations.
# 
# 
# **Objectives**
# <br>
# In this project, we will go deeper and find the distance of each spiral galaxy from Earth using two different methods to plot the linear relationship between recessional velocity and distance and to find the slope ( Hubble's constant). Although Hubble's constant has already been calculated, this project will show why there is still much debate and uncertainty. 
# 
# The two different methods we will use to analyze spiral galaxies are the Fixed Diameter method and the Fixed Magnitude method. We will then calculate the age of our universe for both constants and show the discrepancies compared to Hubble's constant estimated from the cosmic microwave background, 67km/s/Mpc. 
# 
# **Contributions**
# <br>
# The discrepancy between early universe Hubble's constant and late universe Hubble's constant is called Hubble's Tension. An inaccurate constant affects our ability to find the correct distances of galaxies and other celestial objects, as well as the age and behavior of the universe. For example, having a universe with a rate of expansion faster than when it was a baby leads us to think that there could be dark energy or some other thing that is causing it to expand faster. On the other hand, if the rate is lower in our late universe than early universe, we assume that the universe is slowing down.
# 
# 
# **The Fixed Diameter Method**
# <br>
# 
# The first method will come from an online science lab from the University of Washington, where they use 27 galaxy images from the University of Arizona and the equation below to calculate distance. This is assuming the true diameter of the galaxy is about the same as that of the M31 Andromeda Galaxy, 22 kpc.
# 
# $$d = s / a$$
# 
# * d is the distance to the galaxy 
# * s is the true diameter of the galaxy 
# * a is the apparent angular size
# 
#   
# **The Fixed Magnitude Method** 
# <br>
# 
# The second method will use the distance modulus and assume that the absolute magnitude, M = -20.5. This is because we do not have the absolute magnitude, but we do have the apparent magnitude. With over 1000 spiral galaxies in our data, hopefully, the small differences don't drastically change the results. 
# 
# $$d = 10^{\frac{m-M+5}{5}}$$
# 
# * d is the distance to the galaxy
# * m is the apparent magnitude
# * M is the absolute Magnitude
# 
# <br>
# 
# **Hubble's Law**
# <br>
# 
# After we find the distance for each spiral galaxy using both methods, we will use linear regression to find Hubble's constant with the equation and model it.
# 
# $$ v = H_{0}D $$
# 
# * v is the recession velocity from Earth
# * $H_{0}$ is the slope, Hubble's constant
# * D is the distance from the Earth
#   
# <br>
# 
# 

# ### **Dataset Description**
# 

# 
# #### **Fixed Diameter Method**
# <br>
# 
# **Source**
# <br>
# > https://depts.washington.edu/astroed/HubbleLaw/measurements.html
# 
# **Origin and Directions**
# <br>
# The data acquired from the lab was manually entered into a Google Sheet file by following the lab instructions. To find Hubble's constant in the lab, we need to find the recessional velocity and distance from Earth. 
# 
# This dataset of 27 galaxies comes from the University of Washington's Hubble Law lab. The data were acquired by manually measuring the calcium H and K absorption lines (2 lowest troughs) and the Hα emission line (the highest peak) for each galaxy. All 3 wavelengths were notated to find the redshift. We used the equation: redshift =(measured wavelength - rest wavelength) / rest wavelength. After finding the average redshift, we found the average for all 3 and added it to the data file as the average redshift. With the average redshift, we found the recessional velocity using the speed of light: velocity = redshift x speed of light.
# 
# Now, with the distances from Earth, we used a fixed diameter of 22 kpc for each galaxy, and we measured the angular size of each galaxy through images. To solve for distance, we used the equation: distance = diameter / apparent angular size.
# 
# **Structure and Data Types**
# <br>
# The dataset created has 27 rows by 11 columns, including Object Name, Ca K (Å), Ca H (Å), Hα (Å), Ca K Redshift, Ca H Redshift, Hα Redshift, Average Redshift, Velocity (km/s), Galaxy Size (mrad), and Distance (Mpc). The data types are strings and floating numbers. We are keeping floating numbers until the very end for accurate data modeling. 									
# 
# **Fitness for LR**
# <br>
# The data is highly fit for linear regression with the linear relationship between velocity and distance. The slope m will be Hubble's constant. Since the dataset is only 27 galaxies, we can see that there are no duplicates, no missing data, no multiple entries, or extra cleaning to do. 
# 
# #### **Fixed Magnitude Method**
# <br>
# 
# **Source**
# <br>
# > https://ned.ipac.caltech.edu/
# <br>
# > 
# **Origin**
# This data is sourced from the NASA/IPAC Extragalactic Database (NED). Data had to be constrained to enable download. The data file given from the website was a text file, but was converted to a CSV file and then loaded and cleaned. This data will be used for the Fixed Magnitude Method. We use constraints for z = Redshift to avoid relativistic effects. When z < 0.1, then the Hubble constant error is negligible. 
# <br>
# 
# 
# **Directions**
# <br>
# > => https://ned.ipac.caltech.edu/byparams<br>
# > => Search Objects<br>
# > => By Parameters<br>
# > => Redshift Constraints: Between 0 < z < 0.050<br>
# > => Photometric Constraints: Flux density: Between: 0.1 and 10, Flux Unit: Jy, Spectral Region: Optical, Spectral Band: Full Spectral Region<br>
# > => Object Type Constraints: Inclusions: Classified Extragalactic Galaxies: (G)<br>
# 
# **Structure and Data Types**
# <br>
# The data downloaded has 1120 rows and  17 columns. The column headings are Number, Object Name, Right Ascension, Declination, Type, Velocity, Redshift, Redshift Flag, Magnitude and Filter, Separation, References, Notes, Photometry Points, Positions, Redshift Points, Diameter Points, Associations. The data types are integer, string, and floating-point numbers. The data already comes with rounded integers for velocity, so we will leave it as an integer. The other columns, like Distance, will be used for data modeling and will remain as floating numbers. 
# 
# **Fitness for LR**
# <br>
# The data are suitable for linear regression because we have redshift and velocity, and we can compute distances from the apparent magnitude already present in the data. We can use the distance modulus and use a fixed value for absolute magnitude (data is missing M) to solve for distance. Once we find all the distances, we can plot the Linear Relationship between velocity and distance to find the slope, Hubble's constant. 
# <br>
# <br>

# ### **Data Preparation**
# 
# 

# #### **Fixed Diameter Method**
# <br>
# 
# **Acquisition/Cleaning/Sanitisation/Normalisation**
# 
# The dataset was acquired through an online lab using the radial size of galaxies to find the distance. Since we only have 27 galaxies, with columns for redshift, velocity, and distance, we can easily check the data set for duplicates, missing values, wrong or multiple entries, and wrong data types. The data set we created we made sure it was in first normal form. The data from the lab has been curated so that cleaning is not necessary, but cleaning is necessary for the Fixed Magnitude Method. In that one we take raw data straight from NED. 

# In[1]:


get_ipython().run_line_magic('pip', 'install pandas numpy')


# In[2]:


#my code starts here

#load libraries
import pandas as pd
import numpy as np

#load data
lab_data=pd.read_csv(r"C:\Users\maybe\OneDrive\Desktop\One elective Data Science\lab_data.csv")

#check first rows to verify it loaded correctly
print(lab_data.head(1))


# In[3]:


#data types and null values 
lab_data.info()


# In[4]:


#check for missing values or Na, True for missing, false for NOT missing
lab_missing = lab_data.isna()
#check for missing data
total=lab_missing.sum()
print(total)


# In[5]:


#removes duplicate rows
duplicates=lab_data.drop_duplicates(inplace=True)
print("Duplicates Removed:", duplicates)


# In[6]:


#rename column
lab_data = lab_data.rename(columns={'Average Redshift': 'Redshift'})
print(lab_data)


# In[7]:


#new critical columns 
critical_lab_columns=['Object Name', 'Redshift','Velocity(km/s)', 'Distance(Mpc)']
lab_data = lab_data[critical_lab_columns]
print(lab_data)


# In[8]:


#store cleaned data in new CSV file
cleaned_lab_data = lab_data.copy()
cleaned_lab_data.to_csv('cleaned_lab_data.csv', index=False)


# #### **Fixed Magnitude Method**

# In[9]:


#load data
data=pd.read_csv(r"C:\Users\maybe\OneDrive\Desktop\One elective Data Science\galaxy_data.csv")

#check first rows to verify it loaded correctly
print(data.head(1))


# In[10]:


#data types and null values 
data.info()


# **Acquisition**
# <br>
# This data is sourced from the NASA/IPAC Extragalactic Database (NED) funded by the National Aeronautics and Space Administration and operated by the California Institute of Technology. Data had to have constraints to allow data to be downloaded. The data file given from the website was a text file, but was converted to a CSV file and then loaded and cleaned.
# 
# The first steps in preprocessing include loading libraries like pandas and numpy, loading the csv file using pandas, and checking the first row to make sure the data loaded correctly. Then, we quickly looked at the data structure, data types, and null values by using $data.info()$. We confirmed that the data had 17 columns, 1120 rows, floating numbers, integers, and strings, and no null values. 
# 
# Then we looked at missing data using $data.isna()$ where it returns True or False for missing value. It returned False for every row and column. However, we could not see all 1120 rows so we used $sum()$ to add up the number of missing values. We used the variable $missing$ for $missing=data.isna()$ and $print(missing)$. The result came back with a total of $0$ for every column. 
# <br>
# <br>

# In[11]:


#check random rows
data.sample(4)


# In[12]:


#check for missing values or Na, True for missing, false for NOT missing
missing=data.isna()
print(missing)


# In[13]:


total=missing.sum()
print(total)


# **Cleaning**
# <br>
# The cleaning process involved taking out the columns we don't need and filtering the rows for the ones with spiral galaxies only. First, we defined a new array with the column heading we wanted. Then we redefined the data with those columns. For the galaxy filtering, we used $unique=data['Type'].unique()$ to find all the types of galaxies under Object Name. We found 9 but we will only use singular spiral galaxies so we filtered out everything except for 'G' using $data = data[(data['Type'] == 'G')]$ and double checked with $unique=data['Type'].unique()$. It came back with only 'G' found under the heading 'Type'. Finally, we checked the data types again before we moved on to sanitation. 
# <br>
# <br>
# 

# In[14]:


#Filter Columns
#Object Name: Galaxy ID
#RA: Position Coordinate in degrees
#DEC: Position Coordinate in degrees
#Type: Type of Celestial Object 
#Redshift: to calculate distance
#Magnitude and Filter: magnitude related to luminosity
critical_columns=['Object Name', 'Type', 'Velocity', 'Redshift', 'Magnitude and Filter']
data = data[critical_columns]
print(data)


# In[15]:


#finds all types of galaxies listed in the column
unique=data['Type'].unique()
print(unique)


# In[16]:


#Locate rows where Type column contains G or GPair
data = data[(data['Type'] == 'G')]
print(data)


# In[17]:


#finds all types of galaxies listed in the column
unique=data['Type'].unique();
print(unique)


# In[18]:


data[['Type']].describe()


# In[19]:


#check data types
data.info()


# **Sanitation**
# <br>
# In sanitation, we moved into fixing the column 'Magnitude and Filter'. The data type is string, but we want a floating number. First, we looked at all the rows that contained letters from A to Z and found 202 rows with letters. We used $str.extract(r'(\d+\.\d+)').astype(float)$ and created a new column called 'Magnitude'. We are left with 1041 rows, and we checked for missing data and found 27 rows with missing values under Magnitude. We used $dropna()$ to drop all rows that are empty, and then we recalculated the sum of the missing values again with $missing=data.isna()$ and $total=missing.sum()$. After this, we are left with 1014 rows. 
# <br>
# <br>

# In[20]:


#find the apparent magnitudes with filters
#finds all values with strings that contain letters A-Z, a-z
with_filter = data[data['Magnitude and Filter'].str.contains(r'[A-Za-z]')]
print(with_filter['Magnitude and Filter'])


# In[21]:


#to take out the letter from the magnitudes with filters
#then added to new column
data['Magnitude'] = data['Magnitude and Filter'].str.extract(r'(\d+\.\d+)').astype(float)
print(data['Magnitude'])


# In[22]:


#check for missing values or Na, True for missing, false for NOT missing
missing = data.isna()
print(missing)


# In[23]:


#check for missing data
total=missing.sum()
print(total)


# In[24]:


#we need to drop all rows with missing values under Magnitude
data.dropna(subset=['Magnitude'], inplace=True)

#calculating missing values again
missing=data.isna()
total=missing.sum()
print(total)


# In[25]:


#data updated
print(data)


# **Normalization**
# <br>
# 
# For normalization, we made sure that every row had one entry and one data type for each column. We filtered out letters from floating numbers, and we took out missing values and extra galaxies other than spiral galaxies. We added a new column called 'Magnitude' to replace 'Magnitude and Filter'. We drop duplicates and save the cleaned data. 
# <br>
# <br>
# 

# In[26]:


#new critical columns 
critical_columns=['Object Name', 'Velocity', 'Redshift', 'Magnitude']
data = data[critical_columns]
print(data)


# In[27]:


#rename velocity column to include units
data = data.rename(columns={'Velocity': 'Velocity(km/s)'})
print(data)


# In[28]:


#removes duplicate rows
duplicates=data.drop_duplicates(inplace=True)
print("Duplicates Removed:", duplicates)

#check data types again
data.info()


# **Adding Distance to Data**
# <br>
# After cleaning the data, we can add a column with a function to calculate the distance each galaxy is from Earth. We need to add this column to model the linear relationship between velocity and distance. 
# 
# The function will use the apparent magnitude and a fixed absolute magnitude M = -20.5 
# 
# $$d = 10^{\frac{m-M+5}{5}}$$
# 
# * d is the distance to the galaxy
# * m is the apparent magnitude
# * M is the absolute Magnitude
# 
# The formula will give the distance in parsecs, so we will divide by 10^6 for Megaparsecs. 
# 
# 

# In[29]:


# Instead of adding the function in Google Sheets, we will use Python to add a column with a function 
#this is the apparent magnitude that we will use to find distance
val = data['Magnitude']

#function for distance
def distance(val):

    #we've cut the distance equation into parts below

    #10 ^ x , x = exponent 
    exponent = (val - (-20.5) +5) / 5

    #distance in parsecs
    parsecs = 10**exponent

    #distance in mega parsecs
    distance = parsecs/(10**6)

    return distance

data['Distance(Mpc)'] = data.apply(lambda row: distance(row['Magnitude']), axis=1)

#We test to see if the distance is correct using Google to search for distance
#estimates are correct
print(data)


# In[30]:


#store cleaned data in new CSV file
cleaned_galaxy_data = data.copy()
cleaned_galaxy_data.to_csv('cleaned_galaxy_data.csv', index=False)
print(cleaned_galaxy_data)


# ### **Statistical Analysis**

# #### **Fixed Diameter Method**
# <br>
# 
# To perform a statistical analysis, we've saved the data to new files named "cleaned_lab_data" and "cleaned_galaxy_data". For this portion, we will use only "cleaned_lab_data," which comprises the 27 galaxies using the fixed-diameter method. We do statistical analysis on each column from the data file. 
# 
# **Measures of Central Tendency**
# <br>
# 
# Redshift
# <br>
# Mean: 0.006030074074074075<br>
# Median: 0.004852<br>
# Mode: -0.001867<br>
# 
# Velocity(km/s)
# <br>
# Mean: 1807.7407407407406<br>
# Median: 1455.0<br>
# Mode: -560<br>
# 
# Distance(Mpc)
# <br>
# Mean: 32.333333333333336<br>
# Median: 26.0<br>
# Mode: 26<br>
# 
# **Spread**
# <br>
# 
# Redshift
# <br>
# Range: 0.030021<br>
# Variance: 3.730992799430199e-05<br>
# Standard Deviation: 0.0061081853274358<br>
# 
# Velocity(km/s)
# <br>
# Range: 9000<br>
# Variance: 3353223.8917378914<br>
# Standard Deviation: 1831.1810100964599<br>
# 
# Distance(Mpc)
# <br>
# Range: 92<br>
# Variance: 454.9999999999999<br>
# Standard Deviation: 21.33072900770154<br>
# 
# 
# **Distribution**
# <br>
# Redshift
# <br>
# Kurtosis: 4.763820888453366<br>
# Skewness: 1.8870893060226683<br>
# 
# <br>
# Velocity(km/s)
# <br>
# Kurtosis: 4.762848650359467<br>
# Skewness: 1.886913122194997<br>
# <br>
# Distance(Mpc)
# <br>
# Kurtosis: 2.187820711702628<br>
# Skewness: 1.4672968222791198<br>
# 
# 

# In[31]:


pip install scipy


# In[32]:


#check statistics from each column with numerical values
cleaned_lab_data.describe()
#count is the total number of entries
#mean is the average of the column
#std is standard deviation
#min is the smallest value under column
#25% is the 25th percentile
#50% is the 50th percentile or median
#75% is the 75th percentile
#max is the largest value in the column


# In[33]:


#load scipy library for statistical analysis
from scipy import stats
from scipy.stats import kurtosis
from scipy.stats import skew


# In[34]:


#Series 
print('Redshift')
velocity_lab_data = cleaned_lab_data['Redshift']


#Measures of Central Tendency:

#mean using Numpy
velocity_mean_lab = np.mean(velocity_lab_data)
print('Mean:', velocity_mean_lab)

#median using Numpy
velocity_median_lab = np.median(velocity_lab_data)
print('Median:', velocity_median_lab)

#Mode using SciPy
velocity_mode_lab = stats.mode(velocity_lab_data)
print('Mode:', velocity_mode_lab.mode)

#Spread:

#Range using numpy
velocity_range_lab = np.ptp(velocity_lab_data)
print('Range:', velocity_range_lab)

#Variance using numpy
velocity_variance_lab = np.var(velocity_lab_data, ddof=1)
print('Variance:', velocity_variance_lab)

#Standard deviation using numpy
velocity_std_dev_lab = np.std(velocity_lab_data, ddof=1)
print('Standard Deviation:', velocity_std_dev_lab)

#Distribution:

#Kurtosis using scify
velocity_kurtosis_value_lab = kurtosis(velocity_lab_data)
print('Kurtosis:', velocity_kurtosis_value_lab)

#sknewness using scify
velocity_skewness_lab = skew(velocity_lab_data) 
print('Skewness:', velocity_skewness_lab)


# In[35]:


#Series 
print('Velocity(km/s)')
velocity_lab_data = cleaned_lab_data['Velocity(km/s)']


#Measures of Central Tendency:

#mean using Numpy
velocity_mean_lab = np.mean(velocity_lab_data)
print('Mean:', velocity_mean_lab)

#median using Numpy
velocity_median_lab = np.median(velocity_lab_data)
print('Median:', velocity_median_lab)

#Mode using SciPy
velocity_mode_lab = stats.mode(velocity_lab_data)
print('Mode:', velocity_mode_lab.mode)


#Spread:

#Range using numpy
velocity_range_lab = np.ptp(velocity_lab_data)
print('Range:', velocity_range_lab)

#Variance using numpy
velocity_variance_lab = np.var(velocity_lab_data, ddof=1)
print('Variance:', velocity_variance_lab)

#Standard deviation using numpy
velocity_std_dev_lab = np.std(velocity_lab_data, ddof=1)
print('Standard Deviation:', velocity_std_dev_lab)

#Distribution:

#Kurtosis using scify
velocity_kurtosis_value_lab = kurtosis(velocity_lab_data)
print('Kurtosis:', velocity_kurtosis_value_lab)

#sknewness using scify
velocity_skewness_lab = skew(velocity_lab_data) 
print('Skewness:', velocity_skewness_lab)


# In[36]:


#Series 
print('Distance(Mpc)')
distance_lab_data = cleaned_lab_data['Distance(Mpc)']


#Measures of Central Tendency:

#mean using Numpy
distance_mean_lab = np.mean(distance_lab_data)
print('Mean:', distance_mean_lab)

#median using Numpy
distance_median_lab = np.median(distance_lab_data)
print('Median:', distance_median_lab)

#Mode using SciPy
distance_mode_lab = stats.mode(distance_lab_data)
print('Mode:', distance_mode_lab.mode)


#Spread:

#Range using numpy
distance_range_lab = np.ptp(distance_lab_data)
print('Range:', distance_range_lab)

#Variance using numpy
distance_variance_lab = np.var(distance_lab_data, ddof=1)
print('Variance:', distance_variance_lab)

#Standard deviation using numpy
distance_std_dev_lab = np.std(distance_lab_data, ddof=1)
print('Standard Deviation:', distance_std_dev_lab)

#Distribution:

#Kurtosis using scify
distance_kurtosis_value_lab = kurtosis(distance_lab_data)
print('Kurtosis:', distance_kurtosis_value_lab)

#sknewness using scify
distance_skewness_lab = skew(distance_lab_data) 
print('Skewness:', distance_skewness_lab)


# #### **Fixed Magnitude Method**
# <br>
# 
# For this portion, we will only use cleaned_data, which are the galaxies with the fixed magnitude method. 
# 
# 
# **Central Tendency**
# <br>
# 
# Redshift
# <br>
# Mean: 0.007156300788954635<br>
# Median: 0.0053485<br>
# Mode:  0.002322<br>
# 
# Velocity(km/s)
# <br>
# Mean: 2145.408284023669<br>
# Median: 1603.5<br>
# Mode: 696<br>
# 
# Distance(Mpc)
# <br>
# Mean: 36.59994500557494<br>
# Median: 33.728730865886924<br>
# Mode: 39.81071705534969<br>
# 
# 
# Magnitude
# <br>
# Mean: 12.025828402366862<br>
# Median: 12.14<br>
# Mode: 12.5<br>
# 
# 
# **Spread**
# <br>
# 
# Redshift
# <br>
# Range: 0.0493<br>
# Variance: 4.4467395071332046e-05<br>
# Standard Deviation: 0.006668387741525837<br>
# 
# Velocity(km/s)
# <br>
# Range: 14780<br>
# Variance: 3996550.7156667463<br>
# Standard Deviation: 1999.1374929370782<br>
# 
# Distance(Mpc)
# <br>
# Range: 247.89254602918362<br>
# Variance: 538.7477047075126<br>
# Standard Deviation: 23.210939332726554<br>
# 
# 
# Magnitude
# <br>
# Range: 9.41<br>
# Variance: 1.2294721166258753<br>
# Standard Deviation: 1.1088156368963578<br>
# 
# **Distribution**
# <br>
# 
# Redshift
# <br>
# Kurtosis: 13.455070593218338<br>
# Skewness: 3.1669422446545834<br>
# 
# Velocity(km/s)
# <br>
# Kurtosis: 13.455141690456848<br>
# Skewness: 3.1669469019015524<br>
# 
# Distance(Mpc)
# <br>
# Kurtosis: 23.248292147987463<br>
# Skewness: 3.875362999448024<br>
# 
# 
# Magnitude
# <br>
# Kurtosis: 2.458528895768687<br>
# Skewness: -0.13582747964462455<br>
# 

# In[37]:


#check statistics from each column with numerical values
cleaned_galaxy_data.describe()
#count is the total number of entries
#mean is the average of the column
#std is standard deviation
#min is the smallest value under column
#25% is the 25th percentile
#50% is the 50th percentile or median
#75% is the 75th percentile
#max is the largest value in the column


# In[38]:


#Series 
print('Redshift')
redshift_galaxy_data = cleaned_galaxy_data['Redshift']


#Measures of Central Tendency:

#mean using Numpy
redshift_mean_galaxy = np.mean(redshift_galaxy_data)
print('Mean:', redshift_mean_galaxy)

#median using Numpy
redshift_median_galaxy = np.median(redshift_galaxy_data)
print('Median:', redshift_median_galaxy)

#Mode using SciPy
redshift_mode_galaxy = stats.mode(redshift_galaxy_data)
print('Mode:', redshift_mode_galaxy.mode)


#Spread: 

#Range using numpy
redshift_range_galaxy = np.ptp(redshift_galaxy_data)
print('Range:', redshift_range_galaxy)

#Variance using numpy
redshift_variance_galaxy = np.var(redshift_galaxy_data, ddof=1)
print('Variance:', redshift_variance_galaxy)

#Standard deviation using numpy
redshift_std_dev_galaxy = np.std(redshift_galaxy_data, ddof=1)
print('Standard Deviation:', redshift_std_dev_galaxy)

#Distribution:

#Kurtosis using scify
redshift_kurtosis_galaxy = kurtosis(redshift_galaxy_data)
print('Kurtosis:', redshift_kurtosis_galaxy)

#sknewness using scify
redshift_skewness_galaxy = skew(redshift_galaxy_data) 
print('Skewness:', redshift_skewness_galaxy)


# In[39]:


#Series 
print('Velocity(km/s)')
velocity_galaxy_data = cleaned_galaxy_data['Velocity(km/s)']


#Measures of Central Tendency:

#mean using Numpy
velocity_mean_galaxy = np.mean(velocity_galaxy_data)
print('Mean:', velocity_mean_galaxy)

#median using Numpy
velocity_median_galaxy = np.median(velocity_galaxy_data)
print('Median:', velocity_median_galaxy)

#Mode using SciPy
velocity_mode_galaxy = stats.mode(velocity_galaxy_data)
print('Mode:', velocity_mode_galaxy.mode)

#Spread: 

#Range using numpy
velocity_range_galaxy = np.ptp(velocity_galaxy_data)
print('Range:', velocity_range_galaxy)

#Variance using numpy
velocity_variance_galaxy = np.var(velocity_galaxy_data, ddof=1)
print('Variance:', velocity_variance_galaxy)

#Standard deviation using numpy
velocity_std_dev_galaxy = np.std(velocity_galaxy_data, ddof=1)
print('Standard Deviation:', velocity_std_dev_galaxy)

#Distribution:

#Kurtosis using scify
velocity_kurtosis_value_galaxy = kurtosis(velocity_galaxy_data)
print('Kurtosis:', velocity_kurtosis_value_galaxy)

#sknewness using scify
velocity_skewness_galaxy = skew(velocity_galaxy_data) 
print('Skewness:', velocity_skewness_galaxy)


# In[40]:


#Series 
print('Distance(Mpc)')
distance_galaxy_data = cleaned_galaxy_data['Distance(Mpc)']


#Measures of Central Tendency:

#mean using Numpy
distance_mean_galaxy = np.mean(distance_galaxy_data)
print('Mean:', distance_mean_galaxy)

#median using Numpy
distance_median_galaxy = np.median(distance_galaxy_data)
print('Median:', distance_median_galaxy)

#Mode using SciPy
distance_mode_galaxy = stats.mode(distance_galaxy_data)
print('Mode:', distance_mode_galaxy.mode)


#Spread: 

#Range using numpy
distance_range_galaxy = np.ptp(distance_galaxy_data)
print('Range:', distance_range_galaxy)

#Variance using numpy
distance_variance_galaxy = np.var(distance_galaxy_data, ddof=1)
print('Variance:', distance_variance_galaxy)

#Standard deviation using numpy
distance_std_dev_galaxy = np.std(distance_galaxy_data, ddof=1)
print('Standard Deviation:', distance_std_dev_galaxy)

#Distribution:

#Kurtosis using scify
distance_kurtosis_galaxy = kurtosis(distance_galaxy_data)
print('Kurtosis:', distance_kurtosis_galaxy)

#sknewness using scify
distance_skewness_galaxy = skew(distance_galaxy_data) 
print('Skewness:', distance_skewness_galaxy)


# In[41]:


#Series 
print('Magnitude')
magnitude_galaxy_data = cleaned_galaxy_data['Magnitude']


#Measures of Central Tendency:

#mean using Numpy
magnitude_mean_galaxy = np.mean(magnitude_galaxy_data)
print('Mean:', magnitude_mean_galaxy)

#median using Numpy
magnitude_median_galaxy = np.median(magnitude_galaxy_data)
print('Median:', magnitude_median_galaxy)

#Mode using SciPy
magnitude_mode_galaxy = stats.mode(magnitude_galaxy_data)
print('Mode:', magnitude_mode_galaxy.mode)


#Spread: 

#Range using numpy
magnitude_range_galaxy = np.ptp(magnitude_galaxy_data)
print('Range:', magnitude_range_galaxy)

#Variance using numpy
magnitude_variance_galaxy = np.var(magnitude_galaxy_data, ddof=1)
print('Variance:', magnitude_variance_galaxy)

#Standard deviation using numpy
magnitude_std_dev_galaxy = np.std(magnitude_galaxy_data, ddof=1)
print('Standard Deviation:', magnitude_std_dev_galaxy)

#Distribution:

#Kurtosis using scify
magnitude_kurtosis_value_galaxy = kurtosis(magnitude_galaxy_data)
print('Kurtosis:', magnitude_kurtosis_value_galaxy)

#sknewness using scify
magnitude_skewness_galaxy = skew(magnitude_galaxy_data) 
print('Skewness:', magnitude_skewness_galaxy)


# In[ ]:





# ### **Visualisations**

# In[42]:


get_ipython().run_line_magic('pip', 'install matplotlib')


# In[43]:


get_ipython().run_line_magic('pip', 'install seaborn')


# In[44]:


# We need to load libraries like matplotlib to plot data and seaborn for statistical graphs
import matplotlib.pyplot as plt
import seaborn as sns


# #### **Fixed Diameter Method Data Visuals**

# In[45]:


#plotting distributions using Fixed Diameter Method data
#histograms show the frequency of the x values in the y axis

plt.subplot(2, 1, 2)
plt.hist(cleaned_lab_data['Velocity(km/s)'])
plt.title('Velocity km/s Distribution')
plt.show()


# This is a histogram of the recession velocity distribution from the cleaned lab data or the Fixed Diameter Method Data. It shows that most spiral galaxies in this data have a receding velocity of 0 to 3,000 km/s away from Earth, similar to the Fixed Magnitude Method Data, but at a smaller scale due to it being only 27 spiral galaxies. At this scale, it is hard to see curves. 

# In[46]:


plt.subplot(2, 1, 2)
plt.hist(cleaned_lab_data['Redshift'])
plt.title('Redshift Distribution')
plt.show()


# This is a histogram of the redshift distribution from the 27 spiral galaxies in the lab data. Most counts are from 0 to 0.013. This makes sense because the data is from the closest spiral galaxies or the late local universe not the baby universe. 

# In[47]:


plt.subplot(2, 1, 2)
plt.hist(cleaned_lab_data['Distance(Mpc)'])
plt.title('Distance Mpc Distribution')
plt.show()


# This is a histogram of the distance distribution for the lab data. Most of the 27 spiral galaxies are between 1 and 60 Megaparsecs or 60 million x 19.2 trillion miles. There also seems to be one that is 80 to 90 Megaparsecs. 

# In[48]:


# Scatter plot of velocity vs redshift showing linear relationship more clearly

plt.figure()
sns.scatterplot(x='Velocity(km/s)', y='Redshift', data=cleaned_lab_data)
plt.title('Velocity vs Redshift')
plt.show()


# This is a scatter plot of the 27 spiral galaxies from the lab data showing the direct relationship between redshift and velocity more clearly. The higher the velocity, the higher the redshift. 

# In[49]:


# Scatter plot of Distance vs Velocity showing a pre-model of Hubble's Law before we use linear regression

plt.figure()
sns.scatterplot(x = 'Distance(Mpc)', y = 'Velocity(km/s)', data=cleaned_lab_data)
plt.title('Distance vs Velocity')
plt.show()


# This is a scatter plot of distance v velocity from the lab data. With only 27 spiral galaxies in our data, this may lead to a less accurate approximation of Hubble's constant after applying linear refression. 

# #### **Fixed Magnitude Method Data Visuals**

# In[50]:


#plotting distributions using Fixed Magnitude Method data series
#histograms show the frequency of the x values in the y axis


plt.subplot(2, 1, 2)
plt.hist(cleaned_galaxy_data['Velocity(km/s)'])
plt.title('Velocity km/s Distribution')
plt.show()



# This is a histogram for the recession velocity from Earth, from the cleaned NED galaxy data, or the Fixed Magnitude Method Data. Most spiral galaxies in this data have a recession velocity between 0 and 3000 km/s from Earth. With 1014 entries, at this scale, we start to see a curve that starts high and falls quickly. 

# In[51]:


plt.subplot(2, 1, 2)
plt.hist(cleaned_galaxy_data['Redshift'])
plt.title('Redshift Distribution')
plt.show()



# This is a histogram for galaxy redshift. The redshift distribution closely resembles the velocity distribution shown above. This points to a linear relationship between velocity and redshift. This also shows the constraints we set earlier on redshift. To avoid relativistic effects and errors in Hubble's constant, we set the constraint to z < 0.05. 

# In[52]:


plt.subplot(2, 1, 2)
plt.hist(cleaned_galaxy_data['Distance(Mpc)'])
plt.title('Distance Mpc Distribution')
plt.show()



# This histogram shows that most spiral galaxies from the data, 1014 entries, are 0 to 50 Megaparsecs (50,000,000 parsecs) away from Earth. For context, 1 parsec is 3.26 light-years or 19.2 trillion miles. This makes sense because the farthest galaxies are either too dim or outside the redshift constraint z < 0.05. Galaxies with redshifts above 0.05 are not shown. 

# In[53]:


plt.subplot(2, 1, 2)
plt.hist(cleaned_galaxy_data['Magnitude'])
plt.title('Apparent Magnitude Distribution')
plt.show()


# This histogram shows the distribution of galaxies' apparent magnitudes. It shows that most spiral galaxies in this data file, 1014, have an apparent magnitude between 11 and 13. Apparent magnitude goes from brightest to dimmest, lowest to highest values, respectively. For context, the apparent magnitude of the sun is -26.74, really, really bright. Most galaxies are dim between 11 and 13. Our closest spiral galaxy is M31, Andromeda, and it has an apparent magnitude of 3.4 to 3.44. 

# In[54]:


# Scatter plot of velocity vs redshift showing linear relationship more clearly

plt.figure()
sns.scatterplot(x='Velocity(km/s)', y='Redshift', data=cleaned_galaxy_data)
plt.title('Velocity vs Redshift')
plt.show()


# This is a scatter plot of velocity v redshift from the galaxy data with 1014 entries. The higher the velocity, the higher the redshift. This makes sense due to the Doppler effect. Galaxies that recede faster are more redshifted, kind of like how the sound of a horn gets lower and lower as it speeds away from a stationary object. We say redshifted because the longer wavelengths are reddish on the light spectrum. 

# In[55]:


# Scatter plot of Distance vs Velocity showing a pre-model of Hubble's Law before we use linear regression

plt.figure()
sns.scatterplot(x = 'Distance(Mpc)', y = 'Velocity(km/s)', data=cleaned_galaxy_data)
plt.title('Distance vs Velocity')
plt.show()


# This scatter plot shows distance v velocity from the fixed magnitude method data or the 1014 entries from the NED data. With this amount of spiral galaxies, once we use linear regression, it may give a better approximation of Hubble's constant (slope) than the 27 galaxies in the Fixed Diameter Method. 

# In[56]:


#scatter plot with both data series, blue and orange
plt.figure()
sns.scatterplot(x = 'Distance(Mpc)', y = 'Velocity(km/s)', data=cleaned_galaxy_data)
sns.scatterplot(x = 'Distance(Mpc)', y = 'Velocity(km/s)', data=cleaned_lab_data)
plt.title('Distance vs Velocity')
plt.show()


# We can plot both data series in the same scatter plot to compare. We can see that the 27 spiral galaxies are some of the closest galaxies to Earth and don't go beyond 100 Megaparsecs from Earth. Having more data from the NED database gives us a better and bigger picture of our late universe and should lead to a better approximation of Hubble's constant once linear regression is applied. This is the most important visual before we apply machine learning. It gives us a mental model of the motion of the local universe, the galaxies closest to us, all the way to 250 Megaparsecs or 250 million x 19.2 trillion miles away. We can see that there is also a lot of space between our closest galaxies and the farthest ones, and the space between them seems to get bigger the farther the galaxy. 

# ### **Machine Learning Model**

# #### **Linear Regression**
# <br>
# 
# x = distance in Megaparsecs <br>
# y = velocity in kilometers per second <br>
# 
# To find Hubble's constant, we need to make the x values the distance (Mpc) and the y values the velocity km/s). The slope will be the velocity over distance and should approximate 67 to 74 km/s/Mpc. 
# 
# The first scatter plot with a regression line shows us what the model would look like with only 27 spiral galaxies using a fixed diameter and angular size. The slope is 38.8875090868766, which is way off from 67 to 74 km/s/Mpc.
# 
# The second scatter plot with a regression line shows us what the model would look like with 1014 spiral galaxies using the fixed absolute magnitude method. The slope is 60.131705158765094, which is way closer to Hubble's constant than the initial model. We can see that the more data we acquire and analyze, the better our approximation for Hubble's constant is. 
# 
# Our models predicted a constant of 39 and 60 km/s/Mpc. Errors in the angular size measured manually and manual measurements of the light spectra could have contributed to some of the errors in the first model. The biggest factors of error would be the number of entries or data points we have, and the fixed diameter we used for spiral galaxies, 22 kiloparsec. We need lots of data for linear regression to work well, and galaxies come in different shapes and sizes. Constraining galaxy size to only 22 kpc would cause a significant error in the model. 
# 
# The second model also had some error, being almost 10 km/s/Mpc off. This could have been due to the fixed value we used for absolute magnitude -20.5. Like before, galaxies come in different shapes, sizes, and brightness, so using -20.5 for all of them would have caused some error.
# 
# For the age of the universe, we used Hubble's constant to estimate this value. First, we found the inverse of Hubble's constant and then converted it to seconds, and then divided the seconds in a year. The result is in years, so we divided by factors of 10 and got 25 billion years using the fixed diameter and 16 billion years using the fixed magnitude method. Again, the fixed magnitude method gives a better approximation since the universe is estimated to be around 13.8 billion years old. 
# 
# The two main methods scientists use to find Hubble's constant are the Cosmic Microwave Background and the local universe method. This project is similar to what a local universe measurement of Hubble's constant would be. The accepted value of our local universe is around 70-76 km/s/Mpc, and the accepted value of the early universe (CMB) is around 67 km/s/Mpc. This discrepancy is called Hubble's Tension.
# 

# In[57]:


get_ipython().run_line_magic('pip', 'install scikit-learn')


# In[58]:


#loaded the library for linear regression
from sklearn.linear_model import LinearRegression

#defined the x and y series
x = cleaned_lab_data[['Distance(Mpc)']]
y = cleaned_lab_data['Velocity(km/s)']

#called on linear regression and fit()
model = LinearRegression(fit_intercept=True)
model.fit(x, y)


# In[59]:


#called predict, so the model predicts the y values 
yfit =  model.predict(x)

#scatter plot is called with defined colors and labels
plt.scatter( x, y, color='blue', edgecolors= 'white', label='spiral galaxies')

#regression line is plotted using yfit with defined colors and label
plt.plot( x, yfit, color='red', label='Regression line')

#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#titled plot
plt.title('Fixed Diameter, Distance vs Velocity')

#legend for plot is shown
plt.legend()


# In[60]:


H0_1 = model.coef_[0]
print("slope:" , H0_1, "km/s/Mpc")
print("y-intercept:" , model.intercept_, "km/s")
print("predicted velocities:", yfit)


# In[61]:


#defined the x and y series
x = cleaned_galaxy_data[['Distance(Mpc)']]
y = cleaned_galaxy_data['Velocity(km/s)']

#called on linear regression and fit()
model = LinearRegression(fit_intercept=True)
model.fit(x, y)


# In[62]:


#called predict, so the model predicts the y values 
yfit =  model.predict(x)

#scatter plot is called with defined colors and labels
plt.scatter( x, y, color='blue', edgecolors= 'white', label='spiral galaxies')

#regression line is plotted using yfit with defined colors and label
plt.plot( x, yfit, color='red', label='Regression line')

#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#titled plot
plt.title('Fixed Magnitude, Distance vs Velocity')

#legend for plot is shown
plt.legend()


# In[63]:


H0_2 = model.coef_[0]
print("slope:" , H0_2, "km/s/Mpc")
print("y-intercept:" , model.intercept_, "km/s")
print("predicted velocities:", yfit)


# In[64]:


#the predicted Age of the Universe based on Hubble's constant

# We used the Galaxy Lab from the University of Washington for this equation

#to find age, find the inverse of Hubble's constant, 1/H0
#then convert to seconds and cancel distance units with, x 3.09 x 10^19 km/Mpc
#then we converted the seconds to years by dividing by seconds in a year, 3.16 x 10^7 seconds/year

Age_1 = ((1/H0_1)*(3.09*(10**19)))/(3.16 * (10**7))
Age_1 = int(Age_1/(10**9))

Age_2 = ((1/H0_2)*(3.09*(10**19)))/(3.16 * (10**7))
Age_2 = int(Age_2/(10**9))

print("Age of Universe with Fixed Diameter Method:", Age_1, "billion years")
print("Age of Universe with Fixed Magnitude Method:", Age_2, "billion years")


# ### **Validation**

# **Percentage Error**
# <br>
# The accepted value for Hubble's constant is 68 -  74 km/s/Mpc, a range that comes from the early universe and ends in the late universe. We can calculate a percentage erorr using the values from our data analysis and the accepted value. Percentage error = 
# 
# $$\frac{|Experiment - Accepted|}{Accepted} \times 100 $$
# 
# Fixed Diameter Method:
# $$\frac{|38.8875090868766 - (68 -> 74)|}{68 -> 74} \times 100 = 42 -> 47 $$
# 
# Fixed Magnitude Method:
# $$\frac{|60.131705158765094 - (68 -> 74)|}{(68 -> 74)} \times 100 = 12 -> 19  $$
# 
# The percentage error for fixed diameter data is 42 to 47 percent and for the fixed absolute magnitude data it is 12 to 19 percent. The fixed magnitude method is a better predictor of Hubble's constant. The percentage error for the age of the universe using the fixed magnitude data above is (16 billion years - 13.8 billion years) /13.8 billion years = 16 percent when using the accepted value of 13.8 billion years. 
# 
# 
#   

# **Cross Validation**
# <br>
# 
# cross_val_score(mode, x, y, cv = 5):<br>
# The data is split into 5 equal subsets. One subset is used for validation while 4 are used for training. Each subset takes a turn being used for validation while the other 4 are used for training. 
# 
# 
# R^2 Legend: <br>
# R^2 = 1, every galaxy sits on the line. There is no noise or outliers. <br>
# R^2 = 0, every galaxy is random showing no linear relationship <br>
# R^2 = 0.5, 50 percent of the variation in velocites is due to the distance from Earth<br>
# <br>
# 
# **Fixed Diameter Method Data:**
# <br>
# 
# We used the library sklearn and the function cross_val_score() with the parameters model, x, y, and cv = 5 for 5 folds. Each subset is about 7 to 6 galaxies. The R^2 scores for each fold are 0.53611383, -0.03203906, -0.50935448,  0.35165082, -0.25653702, and the average of all of them is 0.02. This means 2 percent of the variation in velocities is due to the distance. There R^2 scores for this model are so bad, there's no justification to keep using this model. We can end the data analysis for this model here. 
# 
# <br>
#   
# **Fixed Magnitude Method Data:**
# <br>
# 
# We set the same parameter with cv = 5 for 5 folds in cross_val_score and got the following R^2 values: 0.52009616, 0.28329054, 0.11595527, 0.53185736, 0.4952887. Each subset is about 202 to 203 galaxiesThe average of all of these is 0.39. This means 39 percent of the variation in velocities is due to the distance. The R^2 scores are better than the previous model and there are no negative scores. An average of 39 means that there is a relationship. 
# 
#     

# In[65]:


##from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_score


#define data vairables
x = cleaned_lab_data[['Distance(Mpc)']]
y = cleaned_lab_data['Velocity(km/s)']


#initialize
model = LinearRegression()

#find scores using 5 fold cross validation
scores = cross_val_score(model, x, y, cv = 5)

#mean of scores above
mean = scores.mean()

#results
print("R^2 scores for each subset:", scores)
print("Average model performance:", mean)


# There are some R^2 values that are negative, 3 out of 5 of them. This suggests poor correlation and an R^2 value closer to 0 than 1. A value closer to 0 suggests random data and noise. This is due to the fact that we manually measured the apparent angular size of the spiral galaxies using images and then we used a fixed diameter of 22 kpc for all 27 spiral galaxies. Galaxies vary in size or diameter significantly. The last thing is that our sample size is way too small at 27 that it increases the influence of error from any outlier in our model. A larger sample size would make any single outlier less and less significant. Overall, the fixed diameter method is highly unreliable and we can stop using it. 

# In[66]:


#define data vairables
x = cleaned_galaxy_data[['Distance(Mpc)']]
y = cleaned_galaxy_data['Velocity(km/s)']


#initialize
model = LinearRegression()


#find scores using 5 fold cross validation
scores = cross_val_score(model, x, y, cv = 5)

#mean of scores above
mean = scores.mean()

#results
print("R^2 scores for each subset:", scores)
print("Average model performance:", mean)


# All of the scores are positive numbers which confirms a positive linear relationship found between distance and velocity and the confirmation of Hubble's Law. The missing percentage is due to outliers and the fact that we used a fixed absolute magnitude of -20.5 knowing that each galaxy varies in brightness. We did this for practical reasons and for easy data modeling. The R^2 value is predicted to be higher or closer to 1 if every galaxy uses the correct absolute magnitude to calculate distance from Earth. 

# ### **Feature Engineering**

# **Using Polynomial Features**
# 
# Hubble's Law is famous for its linear relationship and it's not scientific to assume that it needs polynomial features or curves to fit the data. However, since this is a data analysis project where the data contains noise and peculiar velocities, we used a polynomial feature to see how it might change our model. We will be focused on the fixed magnitude model only. 
# 
# **Fixed Magnitude Method Data:**
# 
# This is the data we want to use for more serious estimation after being cross validated. When we applied a polynomial, the first coefficient came out to 71 km/s/Mpc which is within the official accepted range of Hubble's constant. This is a significant improvement from 60 km/s/Mpc. However, we cannot use a curve to describe Hubble's Law since it's supposed to be a line, the linear relationship between distance and velocity of the galaxies. The slope shows us the rate of expansion and using a curve would be like cheating. Since the first coefficient was 71 km/s/Mpc we make an inference that if we discount outliers or galaxies with peculiar velocities then we can get a better approximation using linear regression. 
# 
# **Fixing the Data**
# 
# After taking out outliers from the dataset and redoing linear regression, we came up with a value lower than before, around 57 km/s/Mpc. This was unexpected because we were expecting the slope to approximate 67 to 74 km/s/Mpc but instead it just got father from that. Then, we tried putting a limit on the distance in our data and we calculated the slope for each model according to the distance limit. We found that there were a few distance limits where we could limit the data to get the best approximations to Hubble's constant. These were at 15 Mpc, 16 Mpc, and 17 Mpc. Then the slope fell down below 60 beyond those distances. Instead of fixing the data, we found that taking out the outliers in velocities beyond 3 standard deviations didn't help. We found that taking out the farthest galaxies didn't help either until 15 to 17 Mpc. The work can be found below. 
# 

# In[67]:


#Fixed Magnitude Method Data Model

#defined the x and y series
x = cleaned_galaxy_data[['Distance(Mpc)']]
y = cleaned_galaxy_data['Velocity(km/s)']

#called on linear regression and fit()
model = LinearRegression(fit_intercept=True)
model.fit(x, y)

#called predict, so the model predicts the y values 
yfit =  model.predict(x)

#scatter plot is called with defined colors and labels
plt.scatter( x, y, color='blue', edgecolors= 'white', label='spiral galaxies')

#regression line is plotted using yfit with defined colors and label
plt.plot( x, yfit, color='red', label='Regression line')

#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#title
plt.title('Fixed Magnitude, Distance vs Velocity')

#legend for plot
plt.legend()


#Hubble's constant, model number 2, fixed magnitude, coefficient 0 
H0_2 = model.coef_[0]
print("slope:" , H0_2, "km/s/Mpc")


# In[68]:


#call library for polynomial features
from sklearn.preprocessing import PolynomialFeatures

#defining polynomial with 2 degrees 
poly = PolynomialFeatures(degree=2, include_bias=False)
#defining x2, 2d array, x and x^2
x2 = poly.fit_transform(x)

#print features
print("Original Features:")
print(x)
print("Polynomial Features:")
print(x2)


# In[69]:


#train model with poly features
model = LinearRegression()
model.fit(x2, y)

#first coefficient is Hubble's constant, model number 2, fixed magnitude 
H0_2 = model.coef_[0]

#second coefficient, negative means downward curve
curve = model.coef_[1]

#print features
print("slope:" , H0_2, "km/s/Mpc")
print("curve:" , curve, "km/s/Mpc")


# In[70]:


#Plotting polynomial features

#to create a smooth curve we need to turn floating numbers in distance column 
#to integers and create 100 equal values in the x axis to plot 
x_int = x.astype(int)
x_plot = np.linspace(x_int.min(), x_int.max(), 100)

#we turn it into a polynomial with x and x^2 and predict y values
x_plot_poly = poly.transform(x_plot)
y_plot = model.predict(x_plot_poly)


#plot data scatter plot
plt.scatter(x,y, color='blue', edgecolors= 'white', label='Spiral Galaxies')

#straight line, regression line, plotted using yfit, blue
plt.plot( x, yfit, color='red', label='Regression Line')

#curve, fitted to data, 2 degrees, green 
plt.plot(x_plot, y_plot, color='green', label='Curve')


#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#title
plt.title('Fixed Magnitude, Distance vs Velocity')

#legend for plot
plt.legend()


#coefficient 1 and 2 in polynomial
print("slope:" , H0_2, "km/s/Mpc")
print("curve:" , curve, "km/s/Mpc")


# In[71]:


#finding residuals manually, actual value minus prediction, y - yfit
model = LinearRegression()
model.fit(x, y)

#create residual 
yfit = model.predict(x)
residual = y - yfit

#plot for residuals
plt.scatter(x, residual, edgecolors= 'white', label='Spiral Galaxies')
plt.axhline(y=0, color='red', linestyle='--')

#x axis is labeled
plt.xlabel('Distance(Mpc)')

#y axis is labeled
plt.ylabel('Residual(km/s)')

#titled plot
plt.title('Distance v. Residuals')

#print out residual values for each spiral galaxy
print("Residual for Velocity:")
print(residual)


# This residual plot shows us how far away each data point or galaxy is from the line or the predicted value. When a predicted value is equal to the actual value then the dot will fall on the dotted line. The more difference there is between values the more residual there is. 

# In[72]:


#Standard Deviation for the Velocity(km/s) Series in Fixed Magnitude Data 
#is Standard Deviation: 1999.1374929370782 or 2000 km/s
#Anything more than 3 standard deviations from the predicted value 
#is an outlier and can be taken out, residual > |6000 km/s|

#we create a standard deviation condition, the absolute value of the residual has to be 
#less than 6000, or 3 Standard Deviations away from the predicted value to be included in data
sd_condition = abs(residual) < 6000

galaxy_data_filtered = cleaned_galaxy_data[sd_condition]

galaxy_data_filtered = galaxy_data_filtered.dropna(subset=['Distance(Mpc)'])

print('Galaxies with Velocity Residuals less than 3 Standard Deviations')
print( galaxy_data_filtered['Velocity(km/s)'])


# In[73]:


# New model without outliers and y intercept of 0. 

#redefine x and y with new filtered data
x = galaxy_data_filtered[['Distance(Mpc)']]
y = galaxy_data_filtered['Velocity(km/s)']

#redefine model
model = LinearRegression(fit_intercept=False)
model.fit(x, y)
yfit =  model.predict(x)

#scatter plot is called with defined colors and labels
plt.scatter( x, y, color='blue', edgecolors= 'white', label='spiral galaxies')

#regression line is plotted using yfit with defined colors and label
plt.plot( x, yfit, color='red', label='Regression line')

#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#titled plot
plt.title('Fixed Magnitude, Distance vs Velocity')

#legend for plot is shown
plt.legend()

#print slope and intercept and velocities
H0 = model.coef_[0]
print("slope:" , H0, "km/s/Mpc")
print("y-intercept:" , model.intercept_, "km/s")
print("predicted velocities:", yfit)


# In[74]:


#define distance
x = galaxy_data_filtered['Distance(Mpc)']

#set condition, we find that a distance limit of 16 Mpc
#gives a better approximation for Hubble's constant, 71 km/s/Mpc 
distance_condition = x < 16

#filter with condition
galaxy_distance_filtered = galaxy_data_filtered[distance_condition]

#redefine x and y with new filtered data
x = galaxy_distance_filtered[['Distance(Mpc)']]
y = galaxy_distance_filtered['Velocity(km/s)']

#redefine model
model = LinearRegression(fit_intercept=False)
model.fit(x, y)
yfit =  model.predict(x)

#scatter plot is called with defined colors and labels
plt.scatter( x, y, color='blue', edgecolors= 'white', label='spiral galaxies')

#regression line is plotted using yfit with defined colors and label
plt.plot( x, yfit, color='red', label='Regression line')

#x axis is labeled
plt.xlabel('Distance (Mpc)')

#y axis is labeled
plt.ylabel('Velocity (km/s)')

#titled plot
plt.title('Fixed Magnitude, Distance vs Velocity')

#legend for plot is shown
plt.legend()

#print slope and intercept and velocities
H0 = model.coef_[0]
print("slope:" , H0, "km/s/Mpc")
print("y-intercept:" , model.intercept_, "km/s")
print( galaxy_distance_filtered['Distance(Mpc)'])


# In[75]:


#new plot to find at what distances slope is equal to 70km/s/Mpc or above

y_slopes = []
x_distance = []


for i in range(251):
    x = galaxy_data_filtered['Distance(Mpc)']

    distance_condition = x < i

    #filter with condition
    galaxy_distance_filtered = galaxy_data_filtered[distance_condition]


    #check for enough data for slope
    #redefine x and y with new filtered data
    if len(galaxy_distance_filtered) > 1:
        x = galaxy_distance_filtered[['Distance(Mpc)']]
        y = galaxy_distance_filtered['Velocity(km/s)']

        #redefine model
        model = LinearRegression(fit_intercept=False)
        model.fit(x, y)
        yfit =  model.predict(x)

        y_slopes.append(int(model.coef_[0]))
        x_distance.append(i)

print(y_slopes)
print(x_distance)


# In[76]:


# new x and y for plot for slopes
x = x_distance
y = y_slopes

#simple plot
plt.plot( x, y, color='blue', label='slope')

#x axis is labeled
plt.xlabel('Distance Limit (Mpc)')

#y axis is labeled
plt.ylabel('Slope (km/s/Mpc)')

#titled plot
plt.title('Distance Limit vs Slope')

#for loop prints out the distance limit and the slope calculated at that distance limit
#it also plots in red dots where the best approximation of Hubble's constant is at
#the closest approximation of Hubble's constant is at the distance limit from 15 to 17. 
for i in range(len(y)):
    if 67 <= y[i] <= 74 :
        print("Distance Limit: ", x[i], "Mpc,", "Slope:" ,y[i], "km/s/Mpc")
        plt.plot( x[i], y[i],'ro')



# In this plot we can see exactly where the best approximation of Hubble's constant is. It shows 3 dots at different distance limits. The 3 best are at distance limits, 15, 16, and 17. They gives us 73, 70, and 68 km/s/Mpc for Hubble's constant within the accepted parameters. Looking at the rest of the graph, we can also see where most of the line sits, between 55 and 60 km/s/Mpc. There seems to be something affecting the slope after 25 Mpc since it falls down quickly from 75 km/s/Mpc. 

# ### **Evaluation**

# **Conclusion and Evaluation**
# <br>
# We tested both models for finding Hubble's constant but we confirmed that significant error was caused by using a fixed value for galaxy diameter and absolute magnitude. Galaxies come in many different sizes and brightnesses. Additionally, when measuring magnitudes we have to acknowledge that there is systemic bias in measuring the magnitudes of galaxies because the dimmest, farthest, and more redshifted galaxies are less likely to be found or detected. 
# 
# Many experiments done in college with easy to use small sample sizes to do manually, like the fixed diameter lab from the University of Washington showed us huge potential for error. It is much better to use large datasets and python than to handle data manually. Even if the data is messy like it was in the beginning, python gives us so many libraries and functions to preprocess. Using python and machine learning models like linear regression on astronomy data proves to be successful in large datasets. 
# 
# The fixed magnitude method proved to be the superior model. Even though we used a fixed absolute value for all 1014 spiral galaxies, there were enough entries that the noise was less significant. There was still significant error which we thought was due to noise when we added a polynomial feature where it identified non-linearities caused by systemic bias. After this, we tried taking out the velocity outliers beyond 6000 km/s from the line but this proved to be unhelpful and just made the slope decrease farther from Hubble's constant. Then, we tried taking out the farthest galaxies and recalculating the slope for every distance range from Earth. We found that the slopes with the best estimates were at the distance limit of 15, 16, and 17 Mpc. After this, the slope falls below 60 km/s/Mpc. 
# 
# This project also highlights the current tension in the science community with Hubble's constant. The two main methods used are with the cosmic microwave background(early universe) and the distance ladder method(the universe closest to us). The early universe gives us a value around 67-70 km/s/Mpc and the late universe gives us 70-74 km/s/Mpc. Scientists suggest that there might be external forces affecting Hubble's constant, like dark energy. If the universe was expanding slower during early universe, there could be a force like dark energy affecting late expansion.

# ### **References**
# <br>
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-g). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/6
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-f). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/5
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-e). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/4
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-d). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/3
# 
# Wikipedia contributors. (2026, January 28). Cosmic distance ladder. Wikipedia.
# >https://en.wikipedia.org/wiki/Cosmic_distance_ladder
# 
# Wikipedia contributors. (2025, September 2). Distance modulus. Wikipedia.
# >https://en.wikipedia.org/wiki/Distance_modulus
# 
# GeeksforGeeks. (2026, February 20). How to calculate skewness and kurtosis in Python? GeeksforGeeks. 
# >https://www.geeksforgeeks.org/data-science/how-to-calculate-skewness-and-kurtosis-in-python/
# 
# Linear regression in Python - Sustainability Methods. (n.d.).
# >https://sustainabilitymethods.org/index.php/Linear_Regression_in_Python#:~:text=Linear%20regression%20implementation%20in%20Python%20First%20of,with%20the%20linear%20regression%20line%2C%20using%20matplotlib.
# 
# PolynomialFeatures. (n.d.). Scikit-learn. 
# >https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-c). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/7
# 
# Bobbitt, Z. (2020, September 7). How to plot a smooth curve in Matplotlib. Statology.
# >https://www.statology.org/matplotlib-smooth-curve/#:~:text=Often%20you%20may%20want%20to,BSpline()
# 
# GeeksforGeeks. (2025, July 23). How to create a residual plot in Python. GeeksforGeeks.
# >https://www.geeksforgeeks.org/python/how-to-create-a-residual-plot-in-python/
# 
# W3Schools.com. (n.d.). 
# >https://www.w3schools.com/python/python_for_loops.asp
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.-b). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/10
# 
# CouRseRa | Online courses & credentials from top educators. Join for free | CourseRA. (n.d.). Coursera. 
# >https://www.coursera.org/learn/uol-cm3005-data-science/home/module/9
# 
# scikit-learn developers. (2019). sklearn.linear_model.LinearRegression — scikit-learn 0.22 documentation. Scikit-Learn.org. 
# >https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# Unveiling Measures of Centrality: A Descriptive Statistics Journey with Python. (n.d.). CodeSignal Learn. 
# >https://codesignal.com/learn/courses/descriptive-and-inferential-statistics-with-python/lessons/unveiling-measures-of-centrality-a-descriptive-statistics-journey-with-python
# 
# Python - Measuring central tendency. (n.d.).
# >https://www.tutorialspoint.com/python_data_science/python_measuring_central_tendency.htm
# 
# Wikipedia Contributors. (2022, January 29). Tully–Fisher relation. Wikipedia; Wikimedia Foundation.
# >https://en.wikipedia.org/wiki/Tully%E2%80%93Fisher_relation
# 
# ‌Distance from absolute and apparent magnitude. (2023). VCalc. 
# >https://www.vcalc.com/wiki/sspickle/Distance-from-absolute-and-apparent-magnitude
# 
# Vogel, T., & NASA. (2025, August 4). Hubble Constant and Tension. NASA Science. 
# >https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-constant-and-tension/
# 
# Grokipedia. (1970, January 21). Galaxy rotation curve. Grokipedia. 
# >https://grokipedia.com/page/Galaxy_rotation_curve
# 
# AstroPages | Hubble’s Law - Activity Lab | Western Washington University. (2026). Wwu.edu.
# >https://astro101.wwu.edu/a101_hubble_lab.html
# 
# ‌Solve For a Variable Calculator - Symbolab. (2017). Symbolab.com. 
# >https://www.symbolab.com/solver/solve-for-equation-calculator‌
# 
# josue.e.morejon. (2026). Astronomy and Astrophysics Formula Sheet. Scribd.
# >https://www.scribd.com/document/870215640/Astronomy-and-Astrophysics-Formula-Sheet‌
# 
# The Hubble Law: Measurements of Velocities and Distances. (n.d.). Depts.washington.edu.
# >https://depts.washington.edu/astroed/HubbleLaw/measurements.html‌
# 
# Far, Far Away: Just How Distant Is That Galaxy? (n.d.). National Radio Astronomy Observatory.
# >https://public.nrao.edu/news/far-far-away-just-how-distant-is-that-galaxy/
# 
# Astronomy Simulations and Animations. (n.d.). Astro.unl.edu. 
# >https://astro.unl.edu/animationsLinks.html
# 
# By Parameters | NASA/IPAC Extragalactic Database. (2018). Caltech.edu. 
# >https://ned.ipac.caltech.edu/byparams
# 
# How Far Away is That Galaxy? Vast Catalog Has Answers. (2017, January 5). NASA Jet Propulsion Laboratory (JPL).
# >https://www.jpl.nasa.gov/news/how-far-away-is-that-galaxy-vast-catalog-has-answers/‌
# 

# In[77]:


pip freeze > requirements.txt


# In[ ]:


#my code ends here

