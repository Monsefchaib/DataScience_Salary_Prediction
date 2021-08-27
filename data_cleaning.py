import pandas as pd

df=pd.read_csv('Uncleaned_DS_jobs.csv')




#salary parsing
df=df[df['Salary Estimate'] != '-1']

#get rid of text in salary

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#hadik le3bda li foust apply b7ala definina fonction foust la methode, w dik la methode bach takhed l'element louwel li
#avant l'espace li mouraha dik lketba f tableau 
minus_Kd=salary.apply(lambda x: x.replace('K','').replace('$',''))
df['min_salary']=minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary']=minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']=(df.min_salary+df.max_salary)/2

#company name text only 
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis =1)

# hadchi : lambda x: (return) x['Company Name'] if x['Rating'] < 0 else (return) x['Company Name'][:-3], axis =1
#means : daba f tableau 3ndna douk les columns li fihoum rating -1 f company name dialhum mazaydch 7dah ra9m w lkhrin zayd
#fihum 3 tles caracteres flkhr
#so return company name nit ila kan la column dyal rating <0 sinon return company name - 3 caracteres lkhrin 

#state field
df['state']= df['Location'].apply(lambda x: x.split(',')[-1])
df['Remote'] = df['state'].apply(lambda x: 1 if 'Remote' in x else 0) #hadi bach les rows li fihoum Remote f location ndir lihoum column jdida feha 1 si remote 0 sinon
cl_state=df['state'].apply(lambda x: x.replace('Remote','').replace('United States','').replace('California','CA').replace('New Jersey','NJ').replace('Texas',' TX').replace('Utah','UT'))
cl_state=cl_state.apply(lambda x: x.replace(' ', ''))
df['job_state']=cl_state
del df['state']

df['same_state']=df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

#age of company

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2021-x)

#parsing of job description (python, powerBI, etc...)

#python
df['python_yn']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#r studio
df['rstudio_yn']=df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.rstudio_yn.value_counts()
#spark
df['spark']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
#aws
df['aws']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
#excel
df['excel']=df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()
#power BI
df['powerBI']=df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() or 'power-bi' in x.lower() or 'powerbi' in x.lower()  else 0)
df.powerBI.value_counts()

del df['index']

df.columns

df.to_csv('salary_data_cleaned.csv', index=False)
