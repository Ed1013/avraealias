!serveralias atk <drac2>
if combat():
    if combat().round_num == 0 or combat().current.name != "Heroes":
        return f'echo No es tu turno para atacar ❌'
    args = &ARGS&
    N = character().name.lower()

    if character().hp <= 0:
        return f'echo No puedes atacar, estas desmayado ☠️'

#set attack string
    if "venz" in N:
        ATK = "Longbow -rr 2"
    elif "akta" in N:
        ATK = "Cimitarra -c 10 -rr 2 magical"
    elif "túrin" in N:
        ATK = "Sol -rr 2 magical"
    elif "hiro" in N:
        ATK = "Hexen magical"
    elif "andem" in N:
        ATK = "Eldritch -rr 2 magical"
    else:
        ATK = ""

#choose random target
    if len(args) == 0:
        #check combatants and make non 0 possible targets
        targets = []
        for mon in combat().combatants:
            if mon.name != 'Map' and mon.name != 'DM' and mon.name.lower() != N:
                if mon.hp > 0 and mon.group != 'Heroes':
                    targets.append(mon.name)
        if not targets:
            TAR = ""
        else:
            TAR = randchoice(targets)
#target specified
    else:
        if "-t" in args[0]:
            TAR = args[1]
        else:
            TAR = args[0]
	op = any(mon.name == TAR for mon in combat().combatants)
	if op == False:
		command = f'echo **__{TAR}__ no esta en la lista de monstruos del combate!**\nNo puedes elegir arma con este comando, usa !attack <nombre de arma> -t <monstruo> para poder elegir con que arma atacar.'
        return command

    command = f'a {ATK} -t {TAR}'
else:
    command = f'echo Not in combat...'

return command
</drac2>
