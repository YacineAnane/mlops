import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    '''
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )
    
    options.configure_side_bar()

    options.configure_selection("single")
    ''' 
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
   #     gridOptions=options.build(),
   #     theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


st.set_page_config(
    layout="centered", page_icon="🖱️", page_title="Interactive table app"
)
st.title("🖱️ Interactive table app")
st.write(
    """This app shows how you can use the [streamlit-aggrid](STREAMLIT_AGGRID_URL) 
    Streamlit component in an interactive way so as to display additional content 
    based on user click."""
)


st.write("Go ahead, click on a row in the table below!")
data = pd.read_csv("../data/train.csv")
df = data.iloc[0,:]
for i in range(1, len(data)):
    selection = aggrid_interactive_table(df)
    if selection:
        st.write("You selected:")
        st.json(selection["selected_rows"])

    new_line = data.iloc[i,:]
    df = df.append({df.columns[j]:new_line[j] for j in range(len(df.columns))})

    
