
# coding: utf-8

# In[297]:


import pandas as pd
import numpy as np

#Define path to schools complete CSV file
schools_complete = "schools_complete.csv"

#Read data into pandas
schools_df=pd.read_csv(schools_complete)
schools_df


# In[298]:


#Define path to students complete CSV file
students_complete = "students_complete.csv"

#Read data into pandas
students_df=pd.read_csv(students_complete)
students_df


# In[299]:


#Calculate total schools
total_schools=len(schools_df['name'].unique().tolist())
total_schools


# In[300]:


#Calculate number of students
total_students=len(students_df['name'].tolist())
total_students


# In[301]:


#Calculate total budget
total_budget=schools_df['budget'].sum()
total_budget


# In[302]:


#Calculate per student budget
budget_per_student=total_budget/total_students
budget_per_student


# In[303]:


#Calculate district average math score
district_avg_math_score=students_df['math_score'].mean()
district_avg_math_score


# In[304]:


#Calculate average reading score
district_avg_reading_score=students_df['reading_score'].mean()
district_avg_reading_score


# In[305]:


#Determine if each student earned passing math score;returns boolean answer
#Assumes passing score is >=70
district_students_pass_math=students_df['math_score']>=70
district_students_pass_math


# In[306]:


#Count number of students in school that passed math
#.sum() function works since False = 0 and True = 1
district_cnt_pass_math=district_students_pass_math.sum() 
district_cnt_pass_math


# In[307]:


#Percentage of students passing math
district_percent_pass_math=district_cnt_pass_math/total_students*100
district_percent_pass_math


# In[308]:


#Determine if each student earned passing reading score; return boolean answer
#Assumes passing score is >=70
district_students_pass_reading=students_df['reading_score']>=70
district_students_pass_reading


# In[309]:


#Count number of students in school that passed reading
#.sum() function works since False = 0 and True = 1
district_cnt_pass_reading=district_students_pass_reading.sum()
district_cnt_pass_reading


# In[310]:


#Percentage of students passing reading
district_percent_pass_reading=district_cnt_pass_reading/total_students*100
district_percent_pass_reading


# In[311]:


#Percentage of students overall passing rate
district_overall_pass_rate=(district_percent_pass_math+district_percent_pass_reading)/2
district_overall_pass_rate


# In[312]:


school_group=students_df.groupby(["school"])
school_group


# In[313]:


#Create data dictionary for district
d = {'Total Schools in District': [total_schools],
     'Total Students': [total_students],
     'Total District Budget': [total_budget],
     'Average Math Score':[district_avg_math_score],
     'Average Reading Score':[district_avg_reading_score],
     '%Passing Math': [district_percent_pass_math],
     '%Passing Reading': [district_percent_pass_reading],
     '%Overall Passing Rate': [district_overall_pass_rate]}


# In[315]:


#Arrange columns
district_summary = district_summary[['Total Schools in District',
                                     'Total Students',
                                     'Total District Budget',
                                     'Average Math Score',
                                     'Average Reading Score',
                                     '%Passing Math',
                                     '%Passing Reading',
                                     '%Overall Passing Rate']]


# In[ ]:


#Generated dataframe using above dictionary
district_summary = pd.DataFrame(d)
district_summary

