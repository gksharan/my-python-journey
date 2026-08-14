def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(areYouPlayingBanjo("Rohit"))   # Rohit plays banjo
print(areYouPlayingBanjo("rohan"))   # rohan plays banjo
print(areYouPlayingBanjo("Karan"))   # Karan does not play banjo
