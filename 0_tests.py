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
