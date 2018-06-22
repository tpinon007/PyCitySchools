
# coding: utf-8

# In[110]:


import pandas as pd
import numpy as np

#Define path to schools complete CSV file
schools_complete = "schools_complete.csv"

#Read data into pandas
schools_df=pd.read_csv(schools_complete)
schools_df


# In[111]:


#Define path to students complete CSV file
students_complete = "students_complete.csv"

#Read data into pandas
students_df=pd.read_csv(students_complete)
students_df


# In[112]:


#Calculate total schools
total_schools=len(schools_df['name'].unique().tolist())
total_schools


# In[113]:


#Calculate number of students
total_students=len(students_df['name'].tolist())
total_students


# In[114]:


#Calculate total budget
total_budget=schools_df['budget'].sum()
total_budget


# In[115]:


#Calculate per student budget
budget_per_student=total_budget/total_students
budget_per_student


# In[116]:


#Calculate district average math score
district_avg_math_score=students_df['math_score'].mean()
district_avg_math_score


# In[117]:


#Calculate average reading score
district_avg_reading_score=students_df['reading_score'].mean()
district_avg_reading_score


# In[118]:


#Determine if each student earned passing math score;returns boolean answer
#Assumes passing score is >=70
district_students_pass_math=students_df['math_score']>=70
district_students_pass_math.head() #can delete .head() to show all data


# In[119]:


#Count number of students in school that passed math
#.sum() function works since False = 0 and True = 1
district_cnt_pass_math=district_students_pass_math.sum() 
district_cnt_pass_math


# In[120]:


#Percentage of students passing math
district_percent_pass_math=district_cnt_pass_math/total_students*100
district_percent_pass_math


# In[121]:


#Determine if each student earned passing reading score; return boolean answer
#Assumes passing score is >=70
district_students_pass_reading=students_df['reading_score']>=70
district_students_pass_reading.head() #can delete .head() to show all data


# In[122]:


#Count number of students in school that passed reading
#.sum() function works since False = 0 and True = 1
district_cnt_pass_reading=district_students_pass_reading.sum()
district_cnt_pass_reading


# In[123]:


#Percentage of students passing reading
district_percent_pass_reading=district_cnt_pass_reading/total_students*100
district_percent_pass_reading


# In[124]:


#Percentage of students overall passing rate
district_overall_pass_rate=(district_percent_pass_math+district_percent_pass_reading)/2
district_overall_pass_rate


# In[125]:


school_group=students_df.groupby(["school"])
school_group


# In[126]:


#Create data dictionary for district
d = {'Total Schools': [total_schools],
     'Total Students': [total_students],
     'Total Budget': [total_budget],
     'Average Math Score':[district_avg_math_score],
     'Average Reading Score':[district_avg_reading_score],
     '%Passing Math': [district_percent_pass_math],
     '%Passing Reading': [district_percent_pass_reading],
     '%Overall Passing Rate': [district_overall_pass_rate]}


# In[127]:


#Generate data frame
district_summary = pd.DataFrame(d)


# In[128]:


#Arrange columns
district_summary = district_summary[['Total Schools',
                                     'Total Students',
                                     'Total Budget',
                                     'Average Math Score',
                                     'Average Reading Score',
                                     '%Passing Math',
                                     '%Passing Reading',
                                     '%Overall Passing Rate']]


# In[129]:


#Display dataframe shwoing district summary
district_summary


# In[130]:


#School summary dataframe
schools_df.drop('School ID',1)
schools_df['Per Student Budget']=schools_df['budget']/schools_df['size']


# In[136]:


#Calculate average math score by school
sch_ave_pass_math_df=students_df.groupby(['school'])['math_score'].mean()
sch_ave_pass_math_df


# In[147]:


#Sort schools according to math score in descending order
sorted_schools_math_df=students_df.sort_values("math_score",ascending=False)
sorted_schools_math_df.head()


# In[134]:


#Calculate average reading score by school
sch_ave_pass_reading_df=students_df.groupby(['school'])['reading_score'].mean()
sch_ave_pass_reading_df


# In[138]:


#Sort schools according to reading score in descending order
sorted_schools_reading_df=students_df.sort_values("reading_score",ascending=False)
sorted_schools_reading_df.head()


# In[ ]:


#Locate students that passed math (score >=70)
passing_math_studs_df=students_df.loc[students_df["math_score"]>=70,["Student ID","name","school","math_score"]]
passing_math_studs_df


# In[ ]:


#Locate students that passed reading (score >=70)
passing_reading_studs_df=students_df.loc[students_df["reading_score"]>=70,["Student ID","name","school","reading_score"]]
passing_reading_studs_df


# In[ ]:


#Count number of students that passed math for school
groupbyschool_math_df=students_df.loc[students_df["math_score"]>=70]
groupbyschool_math_df.head()


# In[ ]:


#Count number of students that passed reading for school
sch_pass_reading_count=students_df.loc['school','reading_score']>=70
sch_pass_reading_count


# In[ ]:


#Merge school summary dataframe with average reading scores
schools_df=schools_df.merge(sch_ave_pass_reading,on='school',how='outer')
schools_df


# In[ ]:


#Calculate percent passing reading for school
#Assume passing score is >=70
passing_reading = sch_ave_pass_reading['reading_score']>= 70
sch_percent_passing_reading=passing_reading/schools_df['size']*100
sch_percent_passing_reading


# In[ ]:


#Calculate percent passing math for school
#Assume passing score is >=70
criteria_passing_math = students_df['math_score']>= 70

#Count number of students in school that passed math
#.sum() function works since False = 0 and True = 1
school_cnt_pass_math=criteria_passing_math.sum() 
school_cnt_pass_math

#sch_percent_passing_math=passing_math/schools_df['size']*100
#sch_percent_passing_math


# In[ ]:


#Calculate overall passing rate for school
revised_schools_df['% Overall Passing Rate'] = (schools_df['% Passing Math']+schools_df['% Passing Reading'])/2
revised_schools_df


# In[ ]:


#rename columns for reading and math scores to average reading and average math scores 
revised=schools_df.rename({'reading_score':'Average Reading Score',
                               'math_score': 'Average Math Score'},axis= 1 , inplace= True)
revised

