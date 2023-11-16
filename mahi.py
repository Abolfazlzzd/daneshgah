#mahigir

vaznmahi_pond = float(input("vazn mahi ke daryaft kardid ra vared konid :")) #meghdar vazn daryaft shode
vaznmahi_kilogram = vaznmahi_pond * 0.453592 #vazn mahi be kilogram
print("vazn mahi" , vaznmahi_kilogram , "kilogram ast")
poole_mahi = vaznmahi_kilogram * 2 #vazn mahi be dollar
print("pople mahi" , poole_mahi , "dollar ast")

if poole_mahi > 3:
    print("shoma mahi ziadi daryaft kardid dorod jayeze shoma chips ast! ")
elif poole_mahi < 3:
    print("shoma kheyli kam mahi gereftid ekhrajid!")

