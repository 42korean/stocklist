from pykrx import stock
import streamlit as st


# 오늘 날짜 기준 전체 상장 종목 리스트 가져오기 (주식 + ETF 포함)
@st.cache_data
def get_market_all_items():
  today = "20260306"  # 또는 최신 영업일 자동 계산 로직 적용
  # 코스피, 코스닥, ETF 전체 종목의 이름과 코드를 가져옴
  df_kospi = stock.get_market_ticker_list(today, market="KOSPI")
  df_kosdaq = stock.get_market_ticker_list(today, market="KOSDAQ")

  stock_dict = {}
  for ticker in list(df_kospi) + list(df_kosdaq):
    name = stock.get_market_ticker_name(ticker)
    stock_dict[name] = ticker

  return stock_dict


# 웹 화면에서 selectbox나 autocomplete에 전체 종목 연동
all_stocks = get_market_all_items()
selected_stock_name = st.selectbox(
    "전체 시장 종목/ETF 검색", options=list(all_stocks.keys())
)
selected_code = all_stocks[selected_stock_name]

st.write(f"선택한 종목명: {selected_stock_name} (종목코드: {selected_code})")