import streamlit as st
import pickle
from PIL import Image

def main():
   background="""  <div style='background-color:#f54269; padding:13px'>
                    <h1 style='color:white'>Model Deployment Heart Disease</h1>
                    <h2 style='color:white'>By: Reynaldy Aries Ariyanto</h2>
                    </div> """ 
   st.markdown(background,unsafe_allow_html=True)
   left,right = st.columns((2,2))
   bmi = left.number_input('BMI',value=0)
   smoke = right.selectbox('Are You Smoking ?',('Yes','No'))
   alcohol = left.selectbox('Are you drink alcohol ?',('Yes','No'))
   physic = right.number_input('What is your Physical Health Score ?',value=0)
   mental = left.number_input('What is Your Mental Health Score ?',value=0)
   walk = right.selectbox('Are you usually walking ?',('Yes','No'))
   sex = left.selectbox('Your Gender',('Male','Female'))
   age = right.selectbox('What is your age ?',('18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'))
   race = left.selectbox('What is your race ?',('White','Black','Asian','American Indian/Alaskan Native','Hispanic','Other'))
   sport = right.selectbox("Are you usually do sport ?",('Yes','No'))
   health = left.selectbox("What is your gen health ?",('Excellent','Very Good','Good','Fair','Poor'))
   sleep = right.number_input("How long you usually sleep ? (hour)",value=0)
   button = st.button('Predict')
   smo = 1 if smoke == 'Yes' else 0
   alc = 1 if alcohol == 'Yes' else 0
   wlk = 1 if walk == 'Yes' else 0
   sx = 1 if sex == 'Male' else 0
   if age == '18-24' :
      ag = 0
   elif age == '25-29':
      ag = 1
   elif age == '30-34':
      ag = 2
   elif age == '35-39':
      ag = 3
   elif age == '40-44':
      ag = 4
   elif age == '45-49':
      ag = 5
   elif age == '50-54':
      ag = 6
   elif age == '55-59':
      ag = 7
   elif age == '60-64':
      ag = 8
   elif age == '65-69':
      ag = 9
   elif age == '70-74':
      ag = 10
   elif age == '75-79':
      ag = 11
   else : 
      ag = 12
   if race == 'American Indian/Alaskan Native':
      ras = 0
   elif race == 'Asian':
      ras = 1
   elif race == 'Black':
      ras = 2
   elif race == 'Hispanic':
      ras = 3
   elif race == 'Other':
      ras = 4
   else :
      ras = 5
   sp = 1 if sport == 'Yes' else 0
   if health == 'Excellent':
      hlt = 0
   elif health == 'Fair':
      hlt = 1
   elif health == 'Good':
      hlt = 2
   elif health == 'Poor':
      hlt = 3
   else :
      hlt = 4
   if button:
      result = pred(bmi,smo,alc,physic,mental,wlk,sx,ag,ras,sp,hlt,sleep)
      if result == 'Healthy':
         img_healthy = Image.open('Image/Healthy.png')
         st.image(img_healthy)
         st.success(f'Your Heart is {result}')
      else:
         img_not_healthy = Image.open('Image/Not Healthy.jpg')
         st.image(img_not_healthy)
         st.success(f'Your Heart is {result}')


with open('Model/heart_model_xgb.pkl','rb') as file1:
   rf = pickle.load(file1)

def pred(bmi,smo,alc,physic,mental,wlk,sx,ag,ras,sp,hlt,sleep):
   predict = rf.predict([[bmi,smo,alc,physic,mental,wlk,sx,ag,ras,sp,hlt,sleep]])
   verdict = 'Healthy' if predict == 0 else 'Not Healthy'

   return verdict

if __name__=="__main__":
    main()