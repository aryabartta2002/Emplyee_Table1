## imporing required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## connect dataset
df = pd.read_csv(r"C:\Users\User\Desktop\DS practice MAY_16_2026\dataset\Employers_data.csv")

## checking data types of all colomns
df.dtypes

## total columns
df.columns

## gives the description of int data
df.describe()

## gives first 5 rows
df.head()

## gives last 5 rows
df.tail()

## gives all the information of a dataset
df.info()

## gives UNIQUE values of all columns

'''
for col in df.columns:
    print(col)
    print(df[col].unique())
    print("----------------")
'''
for col in df.columns:
    print("Column Name:", col)
    print("Unique Values:", df[col].unique())
    print("Count of Unique Values:", df[col].nunique())
    print("----------------------")
    
    
'''   
for col in df.columns:
    print(f"Column Name: {col}")
    print(f"Unique Values:{df[col].unique()}")
    print(f"Count of Unique Values:{df[col].nunique()}\n\n")
'''
   
##----------------------------------------------------------------
## First Moment Business Decision - Measure of Central Tendency (Continuous: Mean, Median, Mode ; Discrete : Mode )
##----------------------------------------------------------------


df.Employee_ID.mean() # 5000.5
df.Employee_ID.median() # 5000.5 
df.Employee_ID.mode() # Name: Employee_ID, Length: 10000, dtype: int64
# Employee_ID is an identifier column, so measures like mean, median, mode, and 
# skewness are not meaningful for interpretation.

df.Name.mode()
df["Name"].value_counts().head()  # frequently occuring name and howmany times it is coming 
df["Name"].value_counts()["James Smith"] # howmany times James Smith is coming 


df.Age.mean() # 35.4559
df.Age.median() # 34.0
df.Age.mode() # 0   30   30 came means, the age 30 count is more
df.Age.value_counts().head() # 5 most frequent Age came and the age 30 count is 550
df.Age.value_counts()[21]  # 116

'''
 Insights : Age is positively skewed or right skewed
            Company may have more early-career or mid-career employees
            Fewer highly experienced senior employees
            Training and career-growth programs may be important
            Future leadership succession planning could matter if senior employees are limited
'''

df.Gender.mode() # Male came so male came frequently
df.Gender.value_counts() # Male: 5108, Female: 4892 
df.Gender.value_counts()['Female']  # 4892

# Insights : Gender has 2 clusters are present


df.Department.mode() # Product
df.Department.value_counts() # All the department came with most frequent number
df.Department.value_counts()['Product'] # 1724    

# Insights : Department has 6 clusters are present

df.Job_Title.mode() # MANAGERs are present more in the company
df.Job_Title.value_counts() # All the 5 job titles with frequency came
df.Job_Title.value_counts()['Manager'] #3325

# Insights : Job_Title column has 5 different clusters and manager position or in the company managers are present most

df.Experience_Years.mean() # 12.3709
df.Experience_Years.median() # 10.0
df.Experience_Years.mode() # 0   1
'''
Insights : Right skewed
           Company may be hiring fresher or mid-level talent more frequently
           Training and mentorship programs may be important
           Senior expertise may be concentrated among a small group of employees
           Workforce growth may be recent or expanding rapidly
'''

df.Education_Level.mode() # Master
df.Education_Level.value_counts() # It has 3 clusters and Master has most data points among Master, Bachelor, PhD
df.Education_Level.value_counts()['PhD'] # 1689

# Insights : Education_Level has 3 clusters and Masters done employees are more in the company 

df.Location.mode() # Austin
df.Location.value_counts() # It has 5 clusters

# Insight : Employees from Austin are more in the company
#           Employees are coming from 5 different location among them Austin location emplyees are more

df.Salary.mean() # 115381.5
df.Salary.median() # 120000.0
df.Salary.mode() # 0     70000

'''
Insights : Salary is right skewed
           Average salary of employees is 115381
           Most employees are getting 70000
'''

##----------------------------------------------------------------
## Second Moment Business Decision - Measure of Dispersion (Only on Continuous data)
##----------------------------------------------------------------

# Age

age_range = max(df.Age) - min(df.Age) 
print(age_range) # 39
print(df.Salary.std()) # 46066.139046664925
print(df["Salary"].var()) # 2122089166.6666667

'''
Businss Insights :
 1. Range: The employee age span covers 39 years, indicating a diverse workforce consisting of both younger and older 
           employees.
    Company has mixed experience levels.
    Multiple career stages are represented.
    Diversity in workforce maturity.
    
 2. Standard Deviation: The high standard deviation in salary indicates significant variation in employee compensation 
                        across the organization.
             Different job roles
             Seniority differences
             Executive vs entry-level pay gap
             Multiple departments/pay grades
  3. Variance: The large salary variance confirms that employee salaries are widely dispersed around the average salary.
  
'''

# Experience_Years

exp_range = max(df['Experience_Years']) - min(df['Experience_Years'])
print(exp_range) # 37
print(df["Experience_Years"].var()) # 83.70330352035253
print(df['Experience_Years'].std()) # 9.148950951904405


'''
Businss Insights :
 1. Range: The organization has employees with a wide range of experience levels, from freshers to highly experienced professionals.
    Workforce includes both junior and senior employees
    Good mix of new talent and experienced staff
    Supports mentorship and knowledge transfer
    
 2. Standard Deviation: The variance indicates noticeable differences in employee experience levels across the organization.
             Uneven distribution of expertise
             Employees belong to different career stages
  3. Variance: The standard deviation shows that employee experience levels vary considerably around the average experience.
              Some employees have very low experience
              Some have significantly higher experience
              Organization may have layered hierarchy levels
  
'''

# Salary

sal_range = max(df.Salary) - min(df.Salary)
print(sal_range) # 190000
print(df.Salary.var()) # 2122089166.6666667
print(df.Salary.std()) # 46066.139046664925


'''
Businss Insights :
 1. Range: There is a very large gap between the lowest-paid and highest-paid employees.
     Multiple hierarchy levels exist
     Entry-level and senior/executive salaries differ greatly
     Compensation structure is broad
  
  2. Standard Deviation: Employee salaries are widely dispersed around the average salary.
    Salary distribution is not uniform
    Employees are paid differently based on:
            role
            department
            experience
            seniority
            
   3. Variance: Salary variability is very high within the organization.    
    
    
Note:
=============
When you see:
Large Range
High Std Dev
High CV

Our immediate thought should be: The data is highly spread out and inconsistent.

'''

##----------------------------------------------------------------
## Third Moment Business Decision - Measure of Asymmetric in Distribution(Continuous Data only)
##----------------------------------------------------------------

print(df.Age.skew()) # 0.49513133304106416
print(df.Experience_Years.skew()) # 0.5939387562590371
print(df.Salary.skew()) # 0.14510089316802435

'''
Insights: 

Age: Approximately Symmetric but slightly right skewed
    Most employees are concentrated around middle age groups
    Few older employees slightly increase the right tail
Experience: Moderate Symmetric but right skewed
    Majority of employees have lower to moderate experience
    Smaller number of highly experienced employees create the right tail
Salary: Nearly symmetric with slight positive skewed
    Salaries are relatively balanced across employees
    Few higher salaries slightly pull the distribution to the right
    Extreme salary imbalance is not very strong
'''  

##----------------------------------------------------------------
## Forth Moment Business Decision - Measure of Peakness or Tailness in Distribution(Continuous Data only)
##----------------------------------------------------------------

print(df.Age.kurt()) # -0.7478628787409352 ----> Platykurtic
print(df.Experience_Years.kurt()) # -0.5413713923239771 ----> Platykurtic
print(df.Salary.kurt()) # -0.9753936933812883 ----> Platykurtic


## The distribution is flatter than a normal distribution and contains fewer extreme outliers.


'''
Insights: 
    
Age: Employee ages are relatively evenly distributed without extreme age outliers.
Experience: Employee experience levels are fairly spread out with limited extreme experience values.
Salary: Salary distribution is relatively flat and does not show strong extreme salary outliers.

'''


##----------------------------------------------------------------
## Graphical Representation
##----------------------------------------------------------------

# Continuous Data ---> Bell Curve, Box plot
# Discrete Data ---> Bar Graph

'''

Column			           Type			     	         Recommended Graph
Employee_ID		         Identifier			               Usually no graph
Name			      Categorical/Text		               Usually no graph
Age			         Continuous Numerical	            	Histogram, Boxplot
Gender			        Categorical			               Bar graph
Department		        Categorical			               Bar graph
Job_Title		        Categorical			               Bar graph
Experience_Years	  Continuous Numerical		        Histogram, Boxplot
Education_Level		    Categorical			              Bar graph
Location		       Categorical		              	   Bar graph
Salary			   Continuous Numerical		         Histogram, Boxplot
'''

## Univariate

### Age

sns.histplot(df.Age, kde = True)
plt.show()

#plt.hist(df.Age); plt.show()

plt.boxplot(df.Age)
plt.show()

### Experience

sns.histplot(df.Experience_Years, kde = True)
plt.show()

plt.boxplot(df.Experience_Years)
plt.show()

### Salary

sns.histplot(df.Salary, kde = True)
plt.show()

sns.boxplot(df.Salary)
plt.show()

## Gender

sns.barplot(df.Gender); plt.show()
sns.barplot(df.Department); plt.show()
sns.barplot(df.Job_Title); plt.show()
sns.barplot(df.Education_Level); plt.show()
sns.barplot(df.Location); plt.show()
    

## Bivariate


##  Heat Map


sns.heatmap(df[["Age", "Experience_Years", "Salary"]].corr(),
            annot=True)

plt.show()

## Scatter Plot

sns.scatterplot(x=df["Age"], y=df["Salary"]); plt.show()
sns.scatterplot(x=df["Age"], y=df["Experience_Years"]); plt.show()
sns.scatterplot(x=df["Experience_Years"], y=df["Salary"]); plt.show()
