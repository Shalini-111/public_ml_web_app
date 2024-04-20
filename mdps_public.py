# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:19:04 2024

@author: SHALINI SEKAR
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('Diabetes_model_sav', 'rb'))


heart_disease_model = pickle.load(open('heart_disease_sav', 'rb'))


parkinson_model = pickle.load(open('parkinson_model_sav' , 'rb'))



# sidebar for Navigation 

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           
                           icons =['activity','heart-pulse','person'],
                           
                           default_index=0)
    
    
# Diabetic Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title("Diabetes Prediction Using ML")
    # getting the Input data from the users 
    #columns for input field
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of pregencies")
        
    with col2:
        Glucose = st.text_input("Glucose Level")
        
    with col3:   
        BloodPressure = st.text_input("BloodPressure Level")
        
    with col1:
        SkinThickness = st.text_input("SkinThickness level")
        
    with col2:
        Insulin = st.text_input("Insulin Value")
        
    with col3:
        BMI = st.text_input("BMI Value")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
        
    with col2:
        Age = st.text_input("Age of the Person")
    

    #code for Prediction 
    diab_diagnosis = ""
    # creating a button for prediction 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]) 
        
        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is Non-Diabetic"
    st.success(diab_diagnosis) # display the result =>text bar
            
    
    
# Heart Disease page
if(selected ==  'Heart Disease Prediction'):
    # page title
    st.title("Heart Disease Prediction Using ML")
    
    
    # getting the Input data from the users 
    #columns for input field
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age =  st.text_input("Age of the Person")
        
    with col2:   
        sex =  st.text_input("Gender of the Person")
        
    with col3:
        cp =  st.text_input("Chest Pain Types")
        
    with col1:
        trestbps =  st.text_input("Resting Blood Pressure")
        
    with col2:
        chol =  st.text_input("Serum Cholestrol in mg/dl")
        
    with col3:
        fbs =  st.text_input("Fasting blood sugar")
        
    with col1:
        restecg =  st.text_input("Resting electrocardiographic results")
        
    with col2:
        thalach =  st.text_input("Maximum heart rate achieved")
        
    with col3:
        exang =  st.text_input("Exercise induced angina")
        
    with col1:
        oldpeak =  st.text_input("ST depression induced by exercise relative to rest")
        
    with col2:
        slope =  st.text_input("The slope of the peak exercise ST segment")
        
    with col3:
        ca =  st.text_input("Number of major vessels colored by flourosopy ")
        
    with col1:
        thal =  st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        
    
 
    if '' in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            st.error("Please fill all the input fields.")
    else:
            # Convert input to floats
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
    # code for prediction
    heart_diagnosis = ""
    # creating a button for prediction 
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([user_input]) 
        
        
        if(heart_prediction[0]==1):
            heart_diagnosis =  "The person has Heart Disease"
           
            
        else:
            heart_diagnosis ="The person does not have heart Disease"
    st.success(heart_diagnosis)
        
    

# Parkinsons Disease Page
if(selected == 'Parkinson Prediction'):
    # Page title
    st.title("Parkinsons Prediction Using ML")
    
    # getting the Input data from the users 
    #columns for input field
    
    col1, col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVPFo(Hz)")
        
    with col2:
        fhi = st.text_input("MDVPFhi(Hz)")
        
    with col3:
       flo = st.text_input(" MDVPFlo(Hz)")
       
    with col4:
        Jitter_percent = st.text_input("MDVPJitter(%)") 
        
    with col5:
        Jitter_Abs= st.text_input(" MDVPJitter(Abs)") 
        
    with col1:
        RAP = st.text_input("MDVPRAP")
        
    with col2:
        PPQ= st.text_input("MDVPPPQ")
        
    with col3:
        DDP= st.text_input("JitterDDP") 
        
    with col4:
        Shimmer= st.text_input("MDVPShimmer") 
        
    with col5:
        Shimmer_dB= st.text_input("MDVPShimmer(dB)")
        
    with col1:
        APQ3 = st.text_input("ShimmerAPQ3")
        
    with col2:
        APQ5 = st.text_input("ShimmerAPQ5")
        
    with col3:
        APQ = st.text_input("MDVPAPQ")
        
    with col4:
        DDA = st.text_input("ShimmerDDA")
        
    with col5:
        NHR= st.text_input("NHR")
        
    with col1:
        HNR= st.text_input("HNR")
        
    with col2:
        RPDE = st.text_input("RPDE")
        
    with col3:
        DFA = st.text_input("DFA")
        
    with col4:
        spread1 = st.text_input("spread1") 
        
    with col5:
        spread2 = st.text_input("spread2") 
        
    with col1:
        D2= st.text_input("D2") 
        
    with col2:
        PPE = st.text_input("PPE") 
        
    user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    
        
    # code for prediction
    parkinson_diagnosis =""
    # creating button for prediction
    if st.button("Parkinson Test Result"):
        parkinson_prediction = parkinson_model.predict([user_input])
        
        if(parkinson_prediction[0]==1):
            parkinson_diagnosis="The person has Parkinson Disease"
        
        else:
            parkinson_diagnosis ="The person does not have Parkinson Disease "
            
    st.success(parkinson_diagnosis)
    