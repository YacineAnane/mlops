import time
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, AgGridTheme
from st_aggrid.shared import GridUpdateMode

# def aggrid_table(df: pd.DataFrame):
#     """Creates an st-aggrid interactive table based on a dataframe.
#     Args:
#         df (pd.DataFrame]): Source dataframe
#     Returns:
#         dict: The selected row
#     """

#     gd = GridOptionsBuilder.from_dataframe(df)
#     gd.configure_pagination(enabled=True)
#     gd.configure_default_column(editable=True, groupable=True)

#     gridoptions = gd.build()
#     grid_table = AgGrid(df, gridOptions=gridoptions,
#                     # update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
#                     update_mode=GridUpdateMode.MODEL_CHANGED,
#                     height=500,
#                     allow_unsafe_jscode=True,
#                     # enable_enterprise_modules = True,
#                     reload_data=False,
#                     theme=AgGridTheme.ALPINE)

#     return grid_table


# st.set_page_config(
#     layout="centered", page_icon="🖱️", page_title="View count predictions"
# )
# st.title("🖱️ View count predictions")
# st.write(
#     """This app displays youtube vidos view count predictions"""
# )

# Update grid
data = pd.read_csv("../data/train.csv")
data = data.astype(float)

df = data.iloc[:3,:]
table = st.table(df)
for i in range(len(df), len(data)):
    new_line = pd.DataFrame([data.iloc[i,:].values], columns=df.columns)
    table.add_rows(new_line)
    time.sleep(1)