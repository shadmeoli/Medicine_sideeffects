# using machine learnig and stats to predict kids bloodtype
# import os
import json
# import time
# from datetime import datetime

import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
# import numpy as np


# error page
def error404():

    # render lottie animation
    def anim(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    col1, col2 = st.columns(2)

    with col1:
        # redering the lottie file inside the dashboard
        lottie_file = anim("Assets/404-notfound.json")
        st_lottie(lottie_file, speed=1, reverse=False,
                  loop=True, quality="high", key=None, width="80%")

    with col2:
        st.title("Internal Server Error")
        st.write("Please be patient")


# the main class
class Dash:

    # constructor
    def __init__(self):

        # page configuration
        st.set_page_config("Medicine side Effects", layout="wide")

    # render lottie animation
    def anim(self, filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    # the hero section
    def hero_section(self):


        
        # columns
        col1, col2 = st.columns(2)
        

        # explanation
        with col1:
            # redering the lottie file inside the dashboard
            lottie_file = self.anim("Assets/medicine-in-pot.json")
            st_lottie(lottie_file, speed=0.5, reverse=False,
                        loop=True, quality="high",
                        width="100%", key=None)

        # lottie svg video
        with col2:
            st.title("Medicine side effects")
            

            st.markdown(
                "##### Discover the Side Effects of Your Medications: Empowering You to Make Informed Health Decisions"
                )
            st.markdown("""

                    Knowing the side effects of a medicine 
                is essential to make informed decisions 
                about your health. Understanding the potential 
                side effects of a medication can help you prepare 
                for any adverse reactions that may occur 
                and take appropriate steps to manage or mitigate them. 
                By being aware of the potential risks associated 
                with a medication, you can make informed decisions 
                about whether it is the right treatment option for you 
                and discuss any concerns with your healthcare provider. 


                
                
                > Knowing the side effects of a medication can ultimately help you achieve the best possible outcome for your health.

				""")


    # * showing medicines
    def medicine_selection(self):

        file = pd.read_csv('medicine_dataset.csv')
        df = pd.DataFrame(file)

        col1, col2 = st.columns(2)

        with col1:
            medicine_name = st.sidebar.multiselect(
                "Select medicine name",options=df["name"].unique(), 
                default=df["name"].unique())

        with col2:
            pass
        
        return st.dataframe(df)

    def main(self):

        # * displaying the hero scetion
        self.hero_section()
        # * the medicine selection
        self.medicine_selection()


# runner 
if __name__ == '__main__':
    try:
        dash = Dash()
        dash.main()
    except Exception as e:
        error404()
        raise e