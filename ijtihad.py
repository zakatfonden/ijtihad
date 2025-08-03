import streamlit as st
import pandas as pd
import numpy as np

# Arabiske overskrifter fra dit billede, men med unikke navne
kolonne_overskrifter = [
    'رقم',
    'الاسم',
    'الكتاب المعاصر',
    'اسم المؤلف (معاصر)', # Unikt navn for forfatteren af den moderne bog
    'الكتاب القديم',
    'اسم المؤلف (قديم)'    # Unikt navn for forfatteren af den klassiske bog
]

# Initialiser data til 14 rækker med tomme strenge
# Vi bruger session_state til at gemme data, så ændringer bevares ved genindlæsning
if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(
        np.full((14, len(kolonne_overskrifter)), '', dtype=object),
        columns=kolonne_overskrifter
    )
    # Sætter kolonnen 'رقم' med tal fra 1 til 14
    st.session_state['df']['رقم'] = [str(i) for i in range(1, 15)]

st.title("Tabel til redigering")
st.write("Dobbeltklik på en celle for at redigere dens indhold.")
st.write("Kolonnenavnene 'اسم المؤلف' er blevet ændret for at være unikke, som krævet af Streamlit.")

# Viser data-editoren
redigeret_df = st.data_editor(st.session_state['df'], num_rows="fixed")

# Opdater session_state med de ændrede data
st.session_state['df'] = redigeret_df

st.write("Ændringer gemmes automatisk og bevares ved genindlæsning af siden.")
