import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="About",
        page_icon=":cricket:",
        layout = "centered",
        initial_sidebar_state = "auto", 
    )
     
    st.title("Hi, welcome to the official website of Wholesale Beef Bulls Cricket team.  ")
    st.subheader("Your one stop shop for all the WBBC Team from the latest team news to all cricket updates")
    st.subheader("This is an online hub that is created by WBBC for all cricket enthusiasts in Bulawayo and Zimbabwe over")
    st.image('beefbulls.jpg', caption='Motto')
    
    st.sidebar.success("Navigation Panel.")

    st.markdown(
        """
        We are a new but rapidly growing cricket team that is located in the City of Kings and Queens that is Bulawayo
        Our main mission is to have a team that is full of talented individuals who are full of nothing but 
        passion and love for the beautiful gentlemens game
        This website will provide you with all the latest news and updates of the WBBC team
        with the main objective of exposing our raw talent. 
        We will also provide you will live ball to ball coverage of all WBBC games. 
        YES! Thats right, you can now watch WBBC Team games in ral time and stay up to
        date with the game from any device.
        """)  
    
    st.subheader('#learn more')
    st.write('Check out our [(Youtube Channel)](https://streamlit.io)')
    st.write('Jump into our [(Documentation)](https://docs.streamlit.io+)')
    st.write('Ask a question in our [(Community Address)](supremecrow999@gmail.com)')
    
if __name__ == "__main__":
    run()



def app():

    st.write('About')