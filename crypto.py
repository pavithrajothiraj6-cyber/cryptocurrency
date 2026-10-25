import requests
import csv
import time
from datetime import datetime


def fetch_top_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params=params)
    return response.json()



def display(coins):
    print("\n" + "=" * 60)
    print("📊 LIVE CRYPTOCURRENCY TRACKER")
    print("=" * 60)

    for i, coin in enumerate(coins, start=1):
        name = coin["name"]
        price = coin["current_price"]
        change = coin["price_change_percentage_24h"]

        print(f"{i}. {name}")
        print(f"   💰 Price: ${price}")
        print(f"   📈 24h Change: {change:.2f}%")
        print("-" * 60)



def save_to_csv(coins):
    with open("crypto_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        for coin in coins:
            writer.writerow([
                datetime.now(),
                coin["name"],
                coin["current_price"],
                coin["price_change_percentage_24h"]
            ])



while True:
    try:
        coins = fetch_top_coins()

        display(coins)
        save_to_csv(coins)

        print("\n🔄 Updating again in 10 seconds...\n")

        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
        input("Press enter to exit...")