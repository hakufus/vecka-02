Fel:1
Observation
När man kollar på switchen så ser man inte att lampan blinkar och att man får ingen signal på den porten.

Hypotes.
Eftersom det inte blinkar vid porten på switchen kan det vara avstängt i interface eller att sladden är trasig. Jag vet vilken enhet det är så jag går och sätter på den först.

Åtgärd: Jag loggar in på switchen och går in i den portens interface och kollar om den är på eller inte. Det visar sig att någon har stängt av den. Jag skriver int g0/1 och på nästa rad no shutdown. 
Jag sparar min ändring.
Kontrollerar min config så att den sparades innan jag loggar ut.
Porten börjar blinka och den får signal. 

Fel:2
Observation:
Du har ett fungerande nätverk men på ett ställe går det lite långsamt.

Hypotes:
Det är olika hastigheter på portarna.

Åtgärd:
Jag går in i switchen och tar show interfaces och mycket riktigt det är olika en med full duplex och en med halv duplex. Jag går in i portens interface som har halvduplex och sätter den på full duplex. (conf-if)# duplex full

Fel:3
Observation:
Signalen kommer igenom switchen då den lär sig mac addressen. Men datorn som dom kopplade in får ej tillgång till nätverket.

Hypotes:
Datorns mac adress kommer upp men den får ingen connection. Först får man kolla om det är i samma vlan inställning. 

Åtgärd:
Loggar in på switchen och gör en show mac adress-table. Där ser jag datorns mac address som jag noterade innan vid felsökningen. Men jag ser med att den är på vlan 50 istället för 20. Jag går in i portens interface och skriver i (config-if)# switchport access vlan 20, exit, exit write memory
kollar sedan att det stämmer i mac adress-table och får ett samtal av användaren att det fungerar nu.

Fel:4

Observation:
Efter en ARP -a så kommer ej mac addressen upp på ipnummret.

Hypotes:
Datorn kan ligga i ett annat nätverk eller så är det gatewayen om enheten ligger i ett annat nätverk, eller så är den avstängd.

Åtgärd:
Rätta till IP-addressen och ta reda på varför enheten inte svarar. Den kan vara avstängd.
Sätter på enheten och får ett svar.
