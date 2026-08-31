
# Uppslagstabell: tillverkarprefix -> namn.
# Fyll på med de prefix du hittar i switchens MAC-tabell.
vendors = {
    "00:0A:95": "Apple",
    "00:1A:11": "Google",
    "00:50:56": "VMware"
}

# Adresserna du vill slå upp. Byt ut mot dina egna.
addresses = [
    "00:0A:95:9D:68:16",
    "00:1A:11:FF:AC:22",
    "00:50:56:C0:00:08",
    ]

for address in addresses:
    # De första åtta tecknen är tillverkarprefixet.
    prefix = address[0:8]
    
    # Finns prefixet i tabellen? Annars skriver vi "okänd".
    if prefix in vendors:
        name = vendors[prefix]
    else:
        name = "okand tillverkare"
        
    print(f"{address} -> {name}")