import streamlit as st

from streamlit_option_menu import option_menu

from modules import login

import about, account, home, news, your_posts

st.set_page_config(
    page_title="Wholesale Beefbulls",
    page_icon=":cricket:",
    layout = "centered",
    initial_sidebar_state = "auto", 
)

class MultiApp:
    def __init__(self):
        self.apps = []
        def add_app(self, tittle, func):

            self.apps.append({
                "tittle": tittle,
                "function": func
            })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_tittle='Menu',
                options=('Home','Account','News','Your Posts','About'),
                icons=('house-fill','personal-circle','chat-fill','trophy-fill'),
                menu_icon='cricket',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-colour": 'gray', "boarder-coloure": 'white'},
                    "icon": {"color":"white","font-size": "23px"},
                    "nav-link": {"color":"gray","font-size": "20px", "text-align": "left", "margin":"0px"},
                    "nav-link-selected": {"background-colour": "#ebebebe"},})
            
            if app== 'Home':
                home.app()
            if app== 'Account':
                account.app()   
            if app== 'News':
                news.app()
            if app== 'About':
                about.app()
            if app== 'Your Posts':
                your_posts.app()     

    run()               
                 
        