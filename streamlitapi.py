import pickle 
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), 'Student_Performance_Prediction_Model.pkl') 
model = pickle.load(open(model_path, 'rb'))

def main():
    st.title('Student Performance Prediction')

    #input variables
    Age = st.text_input('Age of student (year)')
    Library = st.text_input('Hours in the library per week')
    Class = st.text_input('Hours of class attendance per week')
    Extracurricular = st.text_input('Hours of extra-curricular activities per week')
    
    if st.button('Predict'):
        makeprediction = model.predict([[Age,Library,Class,Extracurricular]])
        score = makeprediction[0]
        st.success(f'This student is expected to score {score:.0f} in their upcomming exam')

if __name__ == '__main__':
    main()