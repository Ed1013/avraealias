#Rewards after combat
#ARGS <XP>
!alias rewards embed -title "Recompensa del coliseo! :stadium:" -desc “@everyone XP: {%1%/4} ⬆️ y Monedas: {{roll("(100 + 2d6 * 300) / 4")}} 🪙 cada quien” -color #4AFF33

#Sold items in shop
#ARGS <Text> <Monedas>
!alias vender embed -title "Casa de empeños" -desc %1% -footer "Ganancia: +%2% GP" -thumb https://i.imgur.com/5Y7t79u.png

#instead of box embed use single `  to encase single line code
