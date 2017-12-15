# https://kite.trade/connect/login?api_key=noigj9bflpwesql0

from kiteconnect import KiteConnect

kite = KiteConnect(api_key="noigj9bflpwesql0")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.request_access_token("request_token_here", secret="k0qb58ntbk1mpe8ohp392ym8768jnou9")
kite.set_access_token(data["access_token"])

# Place an order
try:
	order_id = kite.order_place(tradingsymbol="INFY",
					exchange="NSE",
					transaction_type="BUY",
					quantity=1,
					order_type="MARKET",
					product="NRML")

	print("Order placed. ID is", order_id)
except Exception as e:
	print("Order placement failed", e.message)

# Fetch all orders
kite.orders()

# Get instruments
kite.instrume
