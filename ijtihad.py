import streamlit as st
import pandas as pd
import numpy as np

# Arabiske overskrifter fra dit billede
kolonne_overskrifter = [
    'رقم',
    'الاسم',
    'الكتاب المعاصر',
    'اسم المؤلف',
    'الكتاب القديم',
    'اسم المؤلف'
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

# Viser data-editoren
# 'key' er nødvendig for at bevare ændringer korrekt med session_state
redigeret_df = st.data_editor(st.session_state['df'], num_rows="fixed")

# Opdater session_state med de ændrede data
st.session_state['df'] = redigeret_df

st.write("Ændringer gemmes automatisk og bevares ved genindlæsning af siden.")

# Du kan tilføje yderligere kode her, hvis du vil gemme data permanent
# For eksempel til en CSV-fil, database osv.
# st.download_button(...)
