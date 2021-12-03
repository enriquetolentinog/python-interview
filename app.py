from flask import Flask, jsonify, request
import pandas as pd
import helpers

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    '''Return a message if service is already up.'''
    return jsonify({"message": "pong!"})

@app.route("/customerorders/status", methods=['POST'])
def get_customerorders_status():
    '''Check and return the actual status in each costumer order received.
    Receive a list of dicts with structure {str:"order_number", str:"item_name", str:"status"}.
    The status accepted are "PENDING","SHIPPED" and "CANCELLED".
    '''

    # Structure the data
    df_customer_ord_lines = pd.DataFrame(request.json)
    gp_customer_ord_lines = df_customer_ord_lines.groupby('order_number')

    # Get each order status
    return_data = [{"order_number": name, "status": helpers.get_status_order(orders)} for name, orders in gp_customer_ord_lines]
    return jsonify(return_data)


@app.route("/customerorders/season", methods=["POST"])
def get_customerorders_season():
    '''Classify customer orders in seasons accord the order date.
    Receive a list of dicts with structure {str:"ORD_ID", str:"ORD_DT", int:"QT_ORDD"}. 
    The ORD_DT attribute is received as string, but represent a date. That's why needs to have the %m/%d/%y format.
    
    '''
    # Structure the data
    df_customer_orders = pd.DataFrame(request.json)
    df_customer_orders['ORD_DT'] = pd.to_datetime(df_customer_orders['ORD_DT'], format = '%m/%d/%y')

    # Get each order seasonreturn 
    df_customer_orders['SEASON'] = df_customer_orders['ORD_DT'].apply(lambda x: helpers.get_season(x))

    return jsonify(df_customer_orders[['ORD_ID', 'SEASON']].to_dict('records'))

@app.route("/weather/detectchanges", methods=["POST"])
def detect_weather_changes():
    '''Return the dates where the weather changed to rainy.
    Receive a list of dicts with structure {str:"date", boolean:"was_rainy"}. 
    The date attribute is received as string, but represent a date. That's why needs to have the %m/%d/%y format.
    '''
    weather_history = request.json
    return jsonify(helpers.detect_changes(weather_history))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
