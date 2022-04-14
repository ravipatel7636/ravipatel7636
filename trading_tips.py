
import streamlit as st
import requests
from streamlit_lottie import st_lottie_spinner
import ada_trading
import bch_trading
import bit_trading
import doge_trading
import dot_trading
import eth_trading
import ltc_trading
import shib_trading
import usdt_trading
import xlm_trading


def trading_tips():

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets3.lottiefiles.com/private_files/lf30_h4qnjuax.json"
    lottie_json = load_lottieurl(lottie_url)

    st.warning("NOTE :-  The Predicted values of cryptocurrencies are forecasted by machine learning algorithm and are for your "
               "reference only, it doesn't guarantee future exact values."
               "Please do a research before taking any further decision based on this forecasted values.")

    with st.form(key='my_form'):
            crypto = st.selectbox('Select Cryptocurrency',
                              ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Stellar (XLM)', 'Tether (USDT)', 'Bitcoin Cash (BCH)',
                               'Litecoin (LTC)', 'Polkadot (DOT)', 'Dogecoin (DOGE)', 'Cardano (ADA)', 'Shiba Inu (SHIB)'])
            submit_button = st.form_submit_button(label='Submit')

    if submit_button:

        if crypto == "Bitcoin (BTC)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    bit_trading.get_bit_trading()

        if crypto == "Ethereum (ETH)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    eth_trading.get_eth_trading()

        if crypto == "Stellar (XLM)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    xlm_trading.get_xlm_trading()

        if crypto == "Tether (USDT)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    usdt_trading.get_usdt_trading()

        if crypto == "Bitcoin Cash (BCH)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    bch_trading.get_bch_trading()

        if crypto == "Litecoin (LTC)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    ltc_trading.get_ltc_trading()

        if crypto == "Polkadot (DOT)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    dot_trading.get_dot_trading()


        if crypto == "Dogecoin (DOGE)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    doge_trading.get_doge_trading()


        if crypto == "Cardano (ADA)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    ada_trading.get_ada_trading()


        if crypto == "Shiba Inu (SHIB)":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                with st_lottie_spinner(lottie_json):
                    shib_trading.get_shib_trading()
