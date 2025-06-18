print("👋 Hey there, I’m CryptoBuddy – your AI-powered crypto sidekick!")
print("🌟 Let’s find coins that are trending and sustainable!")


crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}


def respond_to_query(user_query):
    user_query = user_query.lower()
    
    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {recommend}! It's eco-friendly and has long-term potential!")
    
    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"🚀 Trending cryptos: {', '.join(trending)}")
    
    elif "long-term" in user_query or "growth" in user_query:
        long_term = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 0.7]
        if long_term:
            print(f"🔮 For long-term growth, consider: {', '.join(long_term)}")
        else:
            print("⚠️ No strong long-term candidates found.")
    
    else:
        print("🤖 I'm still learning! Try asking about trending or sustainable cryptos.")


print("🧠 Ask me about trending or sustainable cryptos!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye! Remember to DYOR – Do Your Own Research!")
        break
    respond_to_query(user_input)


print("⚠️ Disclaimer: Crypto is risky—always do your own research before investing.")
