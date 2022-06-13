!serveralias atk <drac2>
if combat():
	args = &ARGS&
	ch=character()
	N = ch.name.lower()
	monsters = combat().combatants

#set attack string
	if "venz" in N:
		ATK = "Longbow"
	elif "akta" in N:
		ATK = "Cimitarra -c 10 -rr2 magical"
	elif "túrin" in N:
		ATK = "Sol -d 1d8 -rr 2 magical"
	elif "hiro" in N:
		ATK = "Hexen magical"
	elif "andem" in N:
		ATK = "Eldritch magical"
	else:
		ATK = ""

#choose random target
	if len(args) == 0:
		#check combatants and make non 0 possible targets
		targets = []
		for mon in combat().combatants:
			if mon.hp > 0 and mon.name.lower() != N:
				targets.append(mon.name)
		if not targets:
			TAR = ""
		else:
			TAR = randchoice(targets)
	else:
		TAR = args[0]

	command = f'a {ATK} -t {TAR}'
else:
	command = f'echo Not in combat...'

return command
</drac2>
