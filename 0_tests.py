!test <drac2>
command = ""
for mon in combat().combatants:
	command += f'{mon.name} and {mon.hp}'
return command
</drac2>

!test <drac2>
command = f'{combat().round_num}'
return command
</drac2>

!test <drac2>
tokens = load_json(get_svar('charTokens'))
return tokens['akta']
</drac2>

!test <drac2>
locs = ['e','f','g']
command = f'{randchoice(locs)}{randint(5,10)}'
return command
</drac2>

!test <drac2>
N = character().name.lower()
ATK = ''
if "venz" in N:
	ATK = "'Longbow' -rr 2"
return ATK
</drac2>

!test <drac2>
string = ""
i=1
while i<= 3:
	string += f'{ctx.prefix} Line {i}\n'
	i+=1
</drac2>
{{string}}

#Check if monster name is in list of combatants
!test <drac2>
op = any(mon.name == "GO3" for mon in combat().combatants)
if op == True:
	return "it's there"
else:
	return "not in battle"
</drac2>


#putting combatants in array
!test <drac2>
mons = []
grouped =  combat().get_group("Monsters").combatants
for mon in grouped:
	mons.append(mon.name)
return mons
</drac2>

#return combat metadata
!test {{combat().get_metadata("combatAreas","notSet")}}

#reset combat metadata
#!test {{combat().set_metadata("combatAreas","notSet")}}

#get inside object
!test <drac2>
areas = load_json(combat().get_metadata("combatAreas"))
string = ''
for area in areas:
	string+=f'this is {area[0]} \n'
return string
</drac2>

#get length of metadata object
!test <drac2>
areas = load_json(combat().get_metadata("combatAreas"))
string=f'echo length of area {len(areas)} \n'
return string
</drac2>

#testing argparse -area ArenaCentral -area "Arena Sur" -area "Arena Este" -img http://imgur.com/
!alias testy <drac2>
args =argparse(&ARGS&)
return f'echo {args}'
</drac2> 

#testing splitting arguments from |
# -monster Xorn|3|https://www.dndbeyond.com/avatars/thumbnails/30836/551/1000/1000/638063939544338029.png -monster Kobold|4|https://www.dndbeyond.com/avatars/thumbnails/30832/207/1000/1000/638063832924455756.png

!alias testy <drac2>
args =argparse(&ARGS&)
mons = args.get('monster')
monsters = []
for mon in mons:
	monster = mon.split('|')
	monsters.append({"name":monster[0],"number":monster[1],"image":monster[2]})
return f'echo {monsters}'
</drac2> 


#testing arguments
!alias testy <drac2>
strarg = "&*&"
return f'echo {strarg}'

</drac2>

!alias testy <drac2>
args = argparse(&ARGS&)
result = args.get('True')
return f'echo {result}'

</drac2>