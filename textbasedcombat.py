!alias areas <drac2>
def initialize_areas():
    mons = []
    grouped =  combat().get_group("Monsters").combatants
    for mon in grouped:
	    mons.append(mon.name)
    combat().set_metadata("combatAreas", dump_json({"area1":{"name":"","members":[]},"area2":{"name":"","members":[]},"area3":{"name":"","members":[mons]}}))

#Begins
if combat():
    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        initialize_areas()
    areaEmbed = f'echo {load_json(combat().get_metadata("combatAreas"))}'

else:
    areaEmbed = f'echo Not in combat...'

return areaEmbed

</drac2>