!alias coliseo 
multiline <drac2>
command = f'{ctx.prefix}i begin\n'
coliseoSchema = load_json(get_uvar('planColiseo'))
monsters = coliseoSchema.monsters

for mon in monsters:
  command += f'{ctx.prefix}i madd "{mon.name}" -n {mon.number} -group "Monsters"\n'
  command += f'{ctx.prefix}embed -title ":japanese_ogre: Nuevo Contrincante :japanese_ogre:" -desc "*{mon.name}*" -image {mon.image} -color "#780c37"\n'

command += f'{ctx.prefix}embed -title "¡Inicia la batalla!" -desc "Suenan las trompetas del coliseo de batallas, donde los guerreros prueban sus habilidades 🎺. Utiliza **!join** para unirte 🏟️" -color "#f8ff1f"'
return command
</drac2>

#Despues usar !initAreas

#-------------------------------------------

##For planning, setting the uvar before 
!alias planColiseo 
embed <drac2>
args = argparse(&ARGS&)
coliseoSchema = {}
coliseoSchema.update({"arena":{"name":args.last("arenaname"),"img":args.last("arenaimg")}})

#Add the areas in each -area argument
areas = args.get("area")
if len(areas) < 1:
    return 'echo Necesitas al menos 1 area, agrega con -area'
allAreas = []
for area in areas:
    allAreas.append({"name":area,"members":[]})

coliseoSchema.arena.update({"areas":allAreas})

mons = args.get("monster")
if len(mons) < 1:
    return 'echo Necesitas al menos 1 monstruo agrega con -monster name|number|img'
allMonsters = []
for mon in mons:
	monster = mon.split('|')
	allMonsters.append({"name":monster[0],"number":monster[1],"image":monster[2]})

coliseoSchema.update({"monsters":allMonsters})

set_uvar('planColiseo',dump_json(coliseoSchema))
</drac2>
-desc "Final var content {{coliseoSchema}}"

"""
Template for  planning uvar planColiseo
{
  "arena": {
    "name": "string",
    "img": "image url",
    "areas": [
      {
        "name": "areaN",
        "members": []
      }
    ]
  },
  "monsters": [
    {
      "name": "string",
      "number": 0,
      "image":"url string"
    },
    {
      "name2": "string2",
      "number": 0,
      "image":"url string"
    }
  ]
}
"""
##json used by combatAreas metadata  [{"name": "test1", "members": []}, {"name": "test2", "members": []}, {"name": "test3", "members": ["KO1", "KO2", "KO3"]}]

#teststring
!planColiseo -arenaname Lorastir -arenaimg https://64.media.tumblr.com/78a9548e24a5d0dea1a6d149436fdee0/tumblr_p25s2gYY6o1r8ue9qo2_r1_400.png -area "Agua pantanosa" -area "Pasto lodos" -area "Arboles" -monster Xorn|3|https://www.dndbeyond.com/avatars/thumbnails/30836/551/1000/1000/638063939544338029.png -monster Kobold|4|https://www.dndbeyond.com/avatars/thumbnails/30832/207/1000/1000/638063832924455756.png
!test {{get_uvar("planColiseo")}}

"""
JSON for monster images
{
  "combatName":"XO1",
  "monImage":"HTTPS:///"
}
"""