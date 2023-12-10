def nanavai():
    nan_dict = {
        "barbary 1000$": 1000,
        "lavash 1500$": 1500,
        "buget 2000$": 2000,
        "taftoon 2500$": 2500,
        "sangak 3000$": 3000
    }
    
    print("salam be nanvaii khosh amadid")
    print("ma in nan hara dar nanvaii pokht mikonim")
    
    for nan in nan_dict:
        print(nan)
    
    total_price = 0
    
    while True:
        customer_choice = input("(baraye khoroj NA ra begoyid)che nani mikhahid?")
        if customer_choice == "NA":
            break
        if customer_choice in nan_dict:
            nan_price = nan_dict[customer_choice]
            total_price += nan_price
            print("bazam nan mikhahid?")
        else:
            print("moteasefim ma in kalame shoma ra nafahmidim")
    print("hazine nan ", total_price, "tooman shood")

nanavai()
