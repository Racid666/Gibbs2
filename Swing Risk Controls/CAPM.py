def capm(rf, beta, market_return):
    return rf + beta * (market_return - rf)

rf = 0.02  # 2% risk-free rate
beta = 1.2  # beta coefficient of the asset
market_return = 0.08  # 8% expected return of the market portfolio
expected_return = capm(rf, beta, market_return)
print(f"The expected return of the asset is {expected_return:.2%}")