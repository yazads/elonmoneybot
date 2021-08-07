import alpaca_trade_api as tradeapi


API_Key = "PKE8QOREDJNY1INB5JQM"
API_Secret_Key = "a07fvfV44EsgADLR7D3K256sufh0uUuZ3G7SfzE5"
api = tradeapi.REST(API_Key, API_Secret_Key, base_url='https://paper-api.alpaca.markets')


        
def Alpaca_func(TCKER, quantity):
    clock = api.get_clock()
    api.submit_order(
        symbol= TCKER,
        side='buy',
        type='market',
        qty= quantity,
        time_in_force='gtc',
    )
    
    if clock.is_open:
        api.submit_order(
            symbol= TCKER,
            side='sell',
            type='trailing_stop',
            qty= quantity,
            trail_percent = 3.5,
            time_in_force='gtc',
        )
        
#Alpaca_func("AMZN", 1)