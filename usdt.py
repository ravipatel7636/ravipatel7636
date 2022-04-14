import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
from datetime import datetime
import plotly.express as px
import statsmodels.api as sm



def get_usdt():
            USDT = yf.download("USDT-CAD")
            USDT = USDT.drop(columns=['Open','High','Low','Close','Volume'])
            modelhigh = sm.tsa.statespace.SARIMAX(USDT['Adj Close'],
                                                  order=(1, 0, 1),
                                                  seasonal_order=(0, 0, 0, 12),
                                                  enforce_stationarity=False,
                                                  enforce_invertibility=False)
            resultshigh = modelhigh.fit()
            pred = resultshigh.get_prediction(start=datetime(2019, 1, 1), dynamic=False)
            pred_ci = pred.conf_int()
            ax = USDT['2017':].plot(label='observed')
            pred.predicted_mean.plot(ax=ax, label='Forecasted', alpha=.2, figsize=(14, 7))
            pred_uc = resultshigh.get_forecast(steps=30)
            pred_ci = pred_uc.conf_int()
            ax = USDT.plot(label='observed',color='Grey', figsize=(20, 8))
            One_week_values = pred_uc.predicted_mean[:7]
            One_week_values = round(One_week_values, 2)
            pred_uc.predicted_mean.plot(ax=ax, color='green', label='Forecast')
            ax.set_xlabel('Date')
            ax.set_ylabel('CAD price')
            ax.patch.set_facecolor('white')
            plt.legend()
            with st.expander(" 👁 (All time graph + predicted graph)"):
                st.pyplot(plt, use_container_width=True)

                # printing one week values
            st.header("One Week Forecasting")
            fig = px.line(x=One_week_values.index, y=One_week_values.values,
                              labels={'x': 'Date', 'y': 'Canadian Dollars'}, title="USDT forecasting",
                              markers=True)
            fig.update_traces(line_color='#76D714', line_width=5)
            with st.expander(" 👁 ", True):
                    st.plotly_chart(fig, use_container_width=True)
            #printing 6 months values
            st.header("1 Month Forecasting")
            fig = px.line(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean.values,
                          labels={'x': 'Date', 'y': 'Canadian Dollars'}, title="USDT forecasting",
                          markers=True)
            fig.update_traces(line_color='#76D714', line_width=5)
            with st.expander(" 👁 ",True):
                st.plotly_chart(fig, use_container_width=True)
