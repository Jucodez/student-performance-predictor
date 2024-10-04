import pickle 
import streamlit as st
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'Student_Performance_Prediction_Model.pkl') 
model = pickle.load(open(model_path, 'rb'))

def main():
    st.title('Student Performance Prediction')

    # Input variables with placeholders
    Age = st.text_input('Age of student (years)', placeholder="e.g., 18")
    Library = st.text_input('Hours in the library per week', placeholder="e.g., 5")
    Class = st.text_input('Hours of class attendance per week', placeholder="e.g., 20")
    Extracurricular = st.text_input('Hours of extra-curricular activities per week', placeholder="e.g., 10")
    
    # Initialize error tracking
    error = False

    # Validation for each input (ensure they are integers)
    try:
        Age = int(Age)
    except ValueError:
        st.error("Please enter a valid integer for Age.")
        error = True

    try:
        Library = int(Library)
    except ValueError:
        st.error("Please enter a valid integer for Library weekly hours.")
        error = True

    try:
        Class = int(Class)
    except ValueError:
        st.error("Please enter a valid integer for Class weekly attendance hours.")
        error = True

    try:
        Extracurricular = int(Extracurricular)
    except ValueError:
        st.error("Please enter a valid integer for Extra-curricular weekly hours.")
        error = True

    # Only proceed with prediction if there are no errors
    if st.button('Predict') and not error:
        # Perform the prediction
        makeprediction = model.predict([[Age, Library, Class, Extracurricular]])
        score = makeprediction[0]
        
        # Display the result
        st.success(f'This student is expected to score {score:.0f} in their upcoming exam')

if __name__ == '__main__':
    main()
