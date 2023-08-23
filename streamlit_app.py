import pandas as pd
import streamlit as st
import numpy as np
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('gcs', type=FilesConnection)
df = conn.read("anzac723/2023_expenses.csv", input_format="csv", ttl=600)

# Print results.
st.dataframe(df)


