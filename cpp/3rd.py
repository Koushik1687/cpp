good_price = int(input ("tell Goods price:"))
gst = int(input ("tell gst percentage:"))
srv_tax = int(input ("tell service tax percentage:"))
gst_on_goods=good_price*(gst/100)
srv_on_goods=good_price*(srv_tax/100)
print("Goods price = ",good_price)
print("gst on goods = ",gst_on_goods)
print("service tax on goods = ",srv_on_goods)
print("after gst and serivce tax Goods price = ",gst_on_goods+srv_on_goods+good_price)