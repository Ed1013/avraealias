!alias mon_add multiline <drac2>
#Args: !mon_add <name> -img <url for image>]
args = &ARGS&
pargs = argparse(&ARGS&)
monster = args[0]
command = ''
embeds = ''

if "notSet" in combat().get_metadata("combatAreas","notSet"):
    return f'{ctx.prefix}echo Areas not initialized, use initialize_areas'

#create short name
array = monster.split()
short = ''
for m in array:
  short+=m[0]
monindex = 0
for mon in combat().combatants:
    if short in mon.name:
      monindex+=1
monindex+=1
short+=monindex

command += f'{ctx.prefix}i madd "{monster}" -name {short} -group "Monsters"\n'

#enter in random area
areaInfo = load_json(combat().get_metadata("combatAreas"))
indexArea = randint(len(areaInfo))
areaInfo[indexArea].members.append(short)
combat().set_metadata("combatAreas",dump_json(areaInfo))


embeds += f'{ctx.prefix}embed -title ":crossed_swords: Nuevo Contrincante :imp:" -desc "{monster} ({short})" entra a la batalla! -footer "Entra en el area ({indexArea+1}) {areaInfo[indexArea].name}"'
if pargs.last("img",default=None) is not None:
  embeds += f' -image {pargs.last("img")}'
  #add image to monster metadata
  c=load_json(combat().get_metadata("monImgs"))
  c[short]=pargs.last("img")
  combat().set_metadata("monImgs",dump_json(c))
embeds += "\n"

return command + "\n" + embeds
</drac2>