# YOUR CODE HERE
import pandas as pd
df = pd.read_csv('data.csv')

male = df[(df['Sex']=='male') & (df['Age']>40)]
m_df1 = len(male[male['Pclass']==1].value_counts().to_dict())
m_df2 = len(male[male['Pclass']==2].value_counts().to_dict())
m_df3 = len(male[male['Pclass']==3].value_counts().to_dict())

female = df[(df['Sex']=='female') & (df['Age']>40)]
f_df1 = len(female[female['Pclass']==1].value_counts().to_dict())
f_df2 = len(female[female['Pclass']==2].value_counts().to_dict())
f_df3 = len(female[female['Pclass']==3].value_counts().to_dict())

print('male (age>40)')
print(f'Pclass 1: {m_df1}')
print(f'Pclass 2: {m_df2}')
print(f'Pclass 3: {m_df3}')
print('female (age>40)')
print(f'Pclass 1: {f_df1}')
print(f'Pclass 2: {f_df2}')
print(f'Pclass 3: {f_df3}')
