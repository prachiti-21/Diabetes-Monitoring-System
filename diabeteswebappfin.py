import streamlit as st
import pickle

log_model=pickle.load(open('log_diabetes_model.pkl', 'rb'))
def classify(num):
    if num==0:
        return "The patient is not predicted to be diabetic"
    else:
        return "The patient is predicted to be diabetic"
def main():
    st.title("DIABETES MONITORING SYSTEM")
    html_temp ="""
    <div style ="background-color:teal ; padding:10px">
    <h2 style =" color: white;text-align:center;">Diabetes Prediction</n2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    activities=['Logistic Regression']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    st.spinner("Hello")
    sg=st.number_input('Select gender',0.0,2.0)
    sa=st.number_input('Select age',0.0,100.0)
    sbp=st.slider('Select blood pressure',0.0,180.0)
    shd=st.number_input('Select heart disease',0.0,1.0)
    ssh=st.number_input('Select smoking history',0.0,5.0)
    sbmi=st.slider('Select bmi ',0.0,50.0)
    slevel=st.slider('Select hba1c level',0.0,20.0)
    sbg=st.slider('Select blood glucose level',0.0,500.0)
    #sd=st.slider('Select diabetes',0.0,1.0)
    inputs=[[sg,sa,sbp,shd,ssh,sbmi,slevel,sbg ]]
    if st.button('Classify'):
       if option=='Logistic Regression':
          st.success(classify(log_model.predict(inputs)))
if __name__=='__main__':
    main()