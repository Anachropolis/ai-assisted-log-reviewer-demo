from collections.abc import Callable
import streamlit as st


class InterfaceFeatures:

    def __init__(self) -> None:
        self.dropdown = None
        self.button = None
        self.no_sidebar_style = """
            <style>
                div[data-testid="stSidebarNav"] {
                    display: none;
                }
            </style>
        """



    def create_button(self, label: str) -> None:
        with st.sidebar:
            st.markdown(self.no_sidebar_style, unsafe_allow_html=True)

            self.button = st.button(label, on_click=self.clicked)


    def create_dropdown(self, label: str, options: list[str]) -> None:

        with st.sidebar:
            st.markdown(self.no_sidebar_style, unsafe_allow_html=True)

            self.dropdown = st.selectbox(label = label, options = options)


    def get_selection(self) -> str:
        return self.dropdown


    def get_clicked(self) -> bool:
        return self.button


    def clicked(self) -> None:
        st.session_state.clicked = True





