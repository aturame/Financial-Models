# Flat yield curve discounting

def bond_price(face,coupon, rate, T):
    return sum([(coupon + face)/ (1 + rate) **t for t in range(1,T+1)]) + face/(1 + rate)**T


bond_price(1000,0.05,0.04,5)