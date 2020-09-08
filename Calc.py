num = input("Enter superchat amount and hit ENTER> ").replace(',', '')
superchats = float(num)
#print("superchats: %d" % superchats)
afterYoutube = superchats - (superchats * 0.3)
#print("afterYoutube: %d" % afterYoutube)
afterHoloLive = afterYoutube / 2
print("The superchat amount after Youtube and HoloLive cuts is $%s" % "{:,.2f}".format(afterHoloLive))