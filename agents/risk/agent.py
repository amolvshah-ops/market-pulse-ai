def evaluate_risk(symbol: str):
    return {
        "agent": "risk",
        "symbol": symbol,
        "allowed": True,
        "risk_per_trade": 0.02,
        "reason": "Risk control placeholder"
    }
