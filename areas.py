#print the areas information
!alias areas 
<drac2>
if combat():
    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        return f'echo Areas not initialized, use initAreas'
    areas = load_json(combat().get_metadata("combatAreas"))
    areaInfo = ''
    areaCounter = 1
    for area in areas:
        areaInfo+=f'**({areaCounter}) {area.get("name")}**\n'
        for m in area.get("members"):
            mstats = combat().get_combatant(m)
            if mstats is None:
                areaInfo+=f'*{m}*\n'
                #combatant without corresponding entity in combat(), hasn't joined
            elif mstats.monster_name is None:
                areaInfo+=f'*{m}* - HP {mstats.hp}/{mstats.max_hp}\n'
            else:
                areaInfo+=f'{m} - ({mstats.monster_name})\n'
        areaInfo+=f'---\n'
        areaCounter+=1

    areaEmbed = f'embed -title "__:crossed_swords: Areas del Combate :crossed_swords:__" -desc "**{combat().get_metadata("combatName")}:**\n{areaInfo}" -color #42adf5'
    imgCombat = combat().get_metadata("combatImg",default=None)
    if imgCombat is not None:
        areaEmbed +=f' -image "{imgCombat}"'

else:
    areaEmbed = f'echo Not in combat...'

return areaEmbed

</drac2>

###Initialize the areas and monster image combat metadata
!alias initAreas <drac2>
if combat():
    coliseoSchema = load_json(get_uvar('planColiseo'))
    areasInfo = coliseoSchema.arena.areas

    mons = []
    grouped =  combat().get_group("Monsters").combatants
    for mon in grouped:
        mons.append(mon.name)
    last = len(areasInfo)-1
    name = areasInfo[last].name
    areasInfo[last] = {"name":name,"members":mons}

    #Create array for monster to images
    monstersInfo = coliseoSchema.monsters
    monImgs = {}
    for mon in monstersInfo:
        for m in grouped:
            if mon.name == m.monster_name:
                monImgs.update({m.name:mon.image})
    
    
    combat().set_metadata("combatImg",coliseoSchema.arena.get("img"))
    combat().set_metadata("combatName",coliseoSchema.arena.get("name"))
    combat().set_metadata("combatAreas", dump_json(areasInfo))
    combat().set_metadata("monImgs", dump_json(monImgs))

    return f'embed -desc "Arena de combate preparada, utiliza **!areas** para localizar a todos los combatientes" -color "#3271a8" -image {coliseoSchema.arena.get("img")} -footer "Campo de batalla: {coliseoSchema.arena.get("name")}"'


else:
    return f'echo not in combat...'
</drac2>

###Move to the specified area
!alias areas move 
multiline <drac2>
def findMember(member,areasInfo):
    i = 0
    for area in areasInfo:
        for m in area.get("members"):
            if m == member:
                return i
        i+=1
    return None

def showAreas(whoMove,where):
    areas = load_json(combat().get_metadata("combatAreas"))
    areaInfo = ''
    areaCounter = 1
    for area in areas:
        areaInfo+=f'**({areaCounter}) {area.get("name")}**\n'
        for m in area.get("members"):
            mstats = combat().get_combatant(m)
            if mstats.monster_name is None:
                areaInfo+=f'*{m}* - HP {mstats.hp}/{mstats.max_hp}'
            else:
                areaInfo+=f'{m} - ({mstats.monster_name})'
            if m == whoMove:
                areaInfo+=f' :arrow_backward:'
            areaInfo+="\n"
        areaInfo+=f'---\n'
        areaCounter+=1

    areaEmbed = f'{ctx.prefix}embed -title "__:crossed_swords: Areas del Combate :crossed_swords:__" -desc ":arrow_forward: __{whoMove} se mueve a {where}!__\n\n{areaInfo}" -color #42adf5'
    imgCombat = combat().get_metadata("combatImg",default=None)
    if imgCombat is not None:
        areaEmbed +=f' -image "{imgCombat}"'

    return areaEmbed
#start
toMove = &1&
areas = load_json(combat().get_metadata("combatAreas"))
if toMove is None:
    return f'{ctx.prefix}echo Debes incluir el numero del area al que te quieres mover'
elif toMove > len(areas) or toMove-1 < 0:
    return f'{ctx.prefix}echo el area numero {toMove} no existe'

if combat():
    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        return f'{ctx.prefix}echo Areas not initialized, use initialize_areas'
    #remove from current location
    index = findMember(character().name,areas)
    if toMove-1 > index+2 or toMove-1 < index-2:
        return f'\n{ctx.prefix}embed -desc "No puedes moverte mas de 2 areas!" -color "#cc0e1e" '
    if index is None:
        return f'{ctx.prefix}echo your character is not in combat, use !join to start'
    areas[index].members.remove(character().name)
    areas[toMove-1].members.append(character().name)
    combat().set_metadata("combatAreas",dump_json(areas))
    output = showAreas(character().name,areas[toMove-1].name)
    if toMove-1 == index+2 or toMove-1 == index-2:
        output += f'\n{ctx.prefix}embed -desc "Haz utilizado tu accion DASH para moverte 2 areas!" -color "#cc0e1e" -thumb "https://i.pinimg.com/originals/14/2a/4c/142a4c52619597f299b046fbffcf2e57.jpg"'

else:
    output = f'{ctx.prefix}echo Not in combat...'


return output

</drac2>

###Move other combatants
!alias mvother <drac2>
GMname = "ed1013"
def findMember(member,areasInfo):
    i = 0
    for area in areasInfo:
        for m in area.get("members"):
            if m == member:
                return i
        i+=1
    return None

def showAreas(whoMove,where):
    areas = load_json(combat().get_metadata("combatAreas"))
    areaInfo = ''
    areaCounter = 1
    for area in areas:
        areaInfo+=f'**({areaCounter}) {area.get("name")}**\n'
        for m in area.get("members"):
            mstats = combat().get_combatant(m)
            if mstats.monster_name is None:
                areaInfo+=f'*{m}* - HP {mstats.hp}/{mstats.max_hp}'
            else:
                areaInfo+=f'{m} - ({mstats.monster_name})'
            if m == whoMove:
                areaInfo+=f' :arrow_backward:'
            areaInfo+="\n"
        areaInfo+=f'---\n'
        areaCounter+=1

    areaEmbed = f'embed -title "__:crossed_swords: Areas del Combate :crossed_swords:__" -desc ":arrow_forward: __{whoMove} se mueve a {where}!__\n\n{areaInfo}" -color #42adf5'
    imgCombat = combat().get_metadata("combatImg",default=None)
    if imgCombat is not None:
        areaEmbed +=f' -image "{imgCombat}"'

    return areaEmbed


#start
if GMname == ctx.author.name:
    args = &ARGS&
    whoMove = args[0]
    toMove = int(args[1])
    areas = load_json(combat().get_metadata("combatAreas"))
    if toMove is None:
        return f'echo Debes incluir al numero de area al que te quieres mover'
    elif toMove > len(areas) or toMove-1 < 0:
        return f'echo el area numero {toMove} no existe'

    if combat():
        if "notSet" in combat().get_metadata("combatAreas","notSet"):
            return f'echo Areas not initialized, use initialize_areas'
        #remove from current location
        index = findMember(whoMove,areas)
        if index is None:
            return f'echo This member {whoMove} is not in combat'
        areas[index].members.remove(whoMove)
        areas[toMove-1].members.append(whoMove)
        combat().set_metadata("combatAreas",dump_json(areas))
        output = showAreas(whoMove,areas[toMove-1].name)

    else:
        output = f'echo Not in combat...'
return output
</drac2>

!alias areas remove
<drac2>
def findMember(member,areasInfo):
    i = 0
    for area in areasInfo:
        for m in area.get("members"):
            if m == member:
                return i
        i+=1
    return None
toRemove = &ARGS&
GMname = "ed1013"
if GMname == ctx.author.name:
        if combat():
            if "notSet" in combat().get_metadata("combatAreas","notSet"):
                return f'echo Areas not initialized, use initialize_areas'
            areas = load_json(combat().get_metadata("combatAreas"))
            for tR in toRemove:
                index = findMember(tR,areas)
                areas[index].members.remove(tR)
            combat().set_metadata("combatAreas",dump_json(areas))
            output = f'echo Removed {toRemove} from combat arena'
            return output
        else:
            output = f'echo Not in combat...'

</drac2>

!alias areas add
<drac2>
args = &ARGS&
newMember = args[0]
areaNo = int(args[1])-1
GMname = "ed1013"
if GMname == ctx.author.name:
        if combat():
            if "notSet" in combat().get_metadata("combatAreas","notSet"):
                return f'echo Areas not initialized, use initialize_areas'
            areas = load_json(combat().get_metadata("combatAreas"))
            areas[areaNo].members.append(newMember)
            combat().set_metadata("combatAreas",dump_json(areas))
            output = f'echo Added {newMember} to area {areas[areaNo].name}'
            return output
        else:
            output = f'echo Not in combat...'

</drac2>