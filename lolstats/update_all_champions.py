from app.RequestInterface import RequestInterface

path = "/lol/static-data/v3/champions?locale=en_US&tags=all&dataById=true"
all_champions = interface.get(path)

if all_champions.status_code == 200 and all_champions.text:
    file = open('all_champions.txt', 'w')
    file.write(all_champions.text)
    file.close()
    print("Champion data written to file.")
else:
    print("Error! Could not write champion data!")
    print(all_champions.status_code)
