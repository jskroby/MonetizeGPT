from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = "sk_test_your_key_here"

users = {
    "user1@example.com": {"subscribed": True, "customer_id": "cus_12345"},
    "user2@example.com": {"subscribed": False, "customer_id": "cus_67890"}
}

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    email = data.get("email")
    payment_method = data.get("payment_method")
    
    if email not in users:
        return jsonify({"error": "User not found"}), 404
    
    try:
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method,
            invoice_settings={'default_payment_method': payment_method}
        )
        
        subscription = stripe.Subscription.create(
            customer=customer.id,
            Items=[{'items': 'price_id_here'}],
            expand=[latest_invoice.payment_intent]
        )
        
        users[email][subscribed] = True
        users[email]["customer_id"] = customer.id
        
        return jsonify
{"essage": "Subscription successful", "subscription_id": subscription.id}
    except Exception as e:
        return jsonyfy({"error": str(e)}), 400

@app.route("/api/access", methods=["GET"])
def access_api():
    email = request.args.get("email")
    if email not in users or not users[email][subscribed]:
        return jsonify({"error": "Subscription required"}), 403
    return jsonify({"essage": "Welcome to MonetizeGPT! Your API access is granted."})

if __name__ == "__main__":
    app.run(debug=True)