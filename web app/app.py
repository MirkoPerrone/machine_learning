import pandas as pd
import streamlit as st
from sklearn.externals import joblib

model = joblib.load('model.pkl')

# predictor function
def predictor(box1, box2, box3, box4):
    
    new_instance = [box1, box2, box3, box4]
    new = pd.DataFrame(new_instance, index=['spore-print-color', 'gill size', 'stalk-surface-below-ring', 'population']).T
    prediction= model.predict(new)
   
    
    if prediction[0] == 0:
        result = 'edible'
    elif prediction[0] == 1:
        result = 'poisonous'
    
    return result


st.title('The mushroom project')
st.write('Determine whether a a mushroom is edible or poisonous.')
st.write('')
st.write('')

st.write('Please check each option then click submit.')


def main():
    box1 = st.selectbox('Spore print color',
                        ['black', 'brown', 'purple', 'chocolate', 'white', 'green', 'orange', 'yellow','buff'])
    
    box2 = st.selectbox('gill size', ['broad', 'narrow'])
    box3 = st.selectbox('stalk-surface-below-ring', ['smooth', 'silky', 'fibrous', 'scaly'])
    box4 = st.selectbox('population', ['scattered' ,'several', 'numerous', 'abundant', 'solitary', 'clustered'])
    result = ""
    
    if st.button('submit'):
        result = predictor(box1, box2, box3, box4)
        
    st.success('Mushroom is '+str(result))
    
    
    
    
if __name__=='__main__':
    main()

