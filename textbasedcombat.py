#print the areas information
!alias areas <drac2>
if combat():
    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        return f'echo Areas not initialized, use initialize_areas'
    areas = load_json(combat().get_metadata("combatAreas"))
    areaInfo = ''
    areaCounter = 1
    for area in areas:
        areaInfo+=f'**({areaCounter}) {area.get("name")}**\n'
        for m in area.get("members"):
            mstats = combat().get_combatant(m)
            if mstats.monster_name is None:
                areaInfo+=f'*{m}* - HP {mstats.hp}/{mstats.max_hp}\n'
            else:
                areaInfo+=f'{m} - ({mstats.monster_name})\n'
        areaInfo+=f'---\n'
        areaCounter+=1

    areaEmbed = f'embed -title "__:crossed_swords: Areas del Combate :crossed_swords:__" -desc "{areaInfo}" -color #42adf5'

else:
    areaEmbed = f'echo Not in combat...'

return areaEmbed

</drac2>

###Initialize the areas metadata
!alias initAreas <drac2>
mons = []
grouped =  combat().get_group("Monsters").combatants
for mon in grouped:
    mons.append(mon.name)
combat().set_metadata("combatAreas", dump_json([{"name":"area1","members":[]},{"name":"area2","members":[]},{"name":"area3","members":mons}]))
</drac2>

###Move to the specified area
!alias move1 <drac2>
def findMember(member,areasInfo):
    i = 0
    for area in areasInfo:
        for m in area.get("members"):
            if m == member:
                return i
        i+=1
    return None

#start
toMove = &1&
areas = load_json(combat().get_metadata("combatAreas"))
if toMove is None:
    return f'echo Debes incluir al numero de area al que te quieres mover'
elif toMove > len(areas) or toMove-1 < 0:
    return f'echo el area numero {toMove} no existe'

if combat():
    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        return f'echo Areas not initialized, use initialize_areas'
    #remove from current location
    index = findMember(character().name,areas)
    if index is None:
        return f'echo your character is not in combat, use !join to start'
    areas[index].members.remove(character().name)
    output = f'echo Moving to area {areas[toMove-1].name}'
    areas[toMove-1].members.append(character().name)
    combat().set_metadata("combatAreas",dump_json(areas))

else:
    output = f'echo Not in combat...'


return output

</drac2>