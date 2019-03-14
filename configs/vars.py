import datetime, os
#---------------------------------------------------------------------------------->
####### PORTFOLIO: #########
coins = [
    'ethereum-classic', 'binancecoin', 'litecoin', 'ethereum',
    # 'dash', 
    'nano', 
    # 'zcash', 
    'eos',
    #  'neo', 
    # 'theta-token',
    # 'stellar', 'ripple', 'tron', 'icon', 
    'cardano', 
    # 'nexus',
    # 'ravencoin', 'etherparty', '0x', 'omisego'
]
days = '120'
currency = 'btc'
#---------------------------------------------------------------------------------->
####### MARKET PARAMETERS: #########
wallet = 3000.00
n_orders = 500
fees = 3
#---------------------------------------------------------------------------------->
####### HYPERPARAMETERS: #########
epochs = 1
batch_size = 32 # 4, 8, 16, 32...
gamma = 0.95
epsilon = 0.1
epsilon_min = 0.01
epsilon_decay = 0.995
#---------------------------------------------------------------------------------->
####### CONSTANTS (DO NOT CHANGE) #########
n_features = 3 # price, caps, vol
keys = ['prices', 'market_caps', 'total_volumes'] # if change this, change configs/function.py:22
todays_month = datetime.datetime.now().month
todays_day = datetime.datetime.now().day
terminal_width = os.get_terminal_size().columns
PATH_TO_CORRELATION_FILE = 'datasets/' + str(todays_day) + '-' + str(todays_month) + '_correlation_' + str(days) + '_' + currency + '.csv'
PATH_TO_WEIGHTS_FILE = 'datasets/' + str(todays_day) + '-' + str(todays_month) + '_weighs_' + str(days) + '_' + currency + '.csv'
PATH_TO_PCT_CORRELATION_FILE = 'datasets/' + str(todays_day) + '-' + str(todays_month) + '_pct_correlation_' + str(days) + '_' + currency + '.csv'
PATH_TO_COIN_FILE = ['datasets/' + str(todays_day) + '-' + str(todays_month) + '_' + coin + '_'+str(days) + '_' + currency + '.csv' for coin in coins]