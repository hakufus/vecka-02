27 aug 2027
Idag har jag kört packettracer och fått ihop dhcp så att mina 2 clienter får automatiskt ip.
Svarat på 2 frågor om mac adressen och vad är arp.
Fixat så att skriptet fungerar och även testat att byta ut mot nya mac o vendors.
Gjort kontroll frågorna i kapitel 2
Installerat wireshark
Fixat filerna som skall vara redo för dokumentation.
Screenshotat bevis för det man har åstadkommit.
Dokumenterat.

28 aug 2027
repeterat packetracer och kontroll frågor.

31. Gjorde en broadcast på en av datorer för att alla skall gå igenom switchen för att få en mac address. ping 192.168.1.255 för att göra en broadcast. fick svar av alla. gjorde sen en ipconfig för att ta reda på min egen mac adress.
Gjorde en show mac address-table och hittade den i listan. 
Min router kör dhcp så den delar ut ip addresser till vlan1

1/9 Lärt mig mer om subnetting och gått igenom vad jag kan och inte kan på kap2.
Praktikmöte klockan 12 om praktikplats
Läst igenomn boken och skrivit ner vad jag behöver träna mer på.

2/9 lärt mig confa en switch och router med dhcp utan hjälp av böcker eller ai.

Vilka tre lägen finns på en Cisco-switch, och hur ser du i prompten
vilket du är i? 
Svar: User exec mode för grundläggande kontroller av switch
      Privileged mode att ha full kontroll över switchen/routen för att göra inställningar eller se fler status för att se config eller att felsöka
      Config: Där du gör inställningar i din switch/router.

Vad händer med din konfiguration om du stänger av switchen
utan att spara, och vilket kommando sparar den?
Svar: Allt som du har ställt in på routen/switchen försvinner om du inte har skrivit write memory. 
      Då är det föregående inställningar och du kommer få göra om det.

Räkna upp de sju OSI-lagren i ordning. Vilket lager arbetar en
switch på?
Svar: 1 signalen till nätverkskortet/wlan.
      2 Signalen åker vidare till switchen
      3 Signalen åker vidare till routen
      4 Signalen åker vidare ut till internet
      5 Uppkopplingen är gjord mellan hårdvaran
      6 en som översätter så att appen/programmet skall förstå varandra.
      7 port och protokoll.
