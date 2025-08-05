def total_calc(bill_total,tip_perc):
    total=bill_total*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"please pay ${total}")
total_calc(150,20)