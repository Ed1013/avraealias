!serveralias atk 
<drac2>
if combat():
    if combat().round_num == 0 or combat().current.name != get('name'):
        return f'echo No es tu turno para atacar ❌'
    argarray = &ARGS&    
    args = argparse(&ARGS&)
    strcommand = "&*&"

    if character().hp <= 0:
        return f'echo No puedes atacar, estas desmayado ☠️'
    
    targets = args.get("t")
    if len(targets) == 0:
        return f'echo Necesitas al menos un target para tu ataque, utiliza **-t** para indicar cual monstruo atacar.\nUtiliza **!areas** o **!init list** para ver que monstruos estan en combate.\nPara ver tus ataques utiliza **!attack list** y para ver hechizos **!spellbook**'
    
    ATK = ""
    if "-" in argarray[0]:
        N = character().name.lower()
        #set attack string
        if "venz" in N:
            ATK = "Longbow -rr 2"
        elif "akta" in N:
            ATK = "Spitfire -c 10 -rr 2 magical"
        elif "túrin" in N:
            ATK = "Sol -rr 2 magical"
        elif "hiro" in N:
            ATK = "Hexen magical"
        elif "andem" in N:
            ATK = "Eldritch -rr 2 magical"

    command = f'i attack {ATK} {strcommand}'
else:
    command = f'echo Not in combat...'

return f'{command}'
</drac2>


"""
        for TAR in targets:
            op = any(mon.name == TAR for mon in combat().combatants)
            if op == False:
                command = f'echo **__{TAR}__ no esta en la lista de monstruos del combate!**'
                return command

#
"""  