!serveralias join multiline
<drac2>
if combat():
    lr=get_svar('longrest')
    command = ''

    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        command += f'echo combatAreas not initialized, wait for GM to initialize'
    else:
        areaInfo = load_json(combat().get_metadata("combatAreas"))
        indexArea = randint(len(areaInfo))
        areaInfo[indexArea].members.append(character().name)
        combat().set_metadata("combatAreas",dump_json(areaInfo))

        command = f'{ctx.prefix}init join -f "Random starting area"|"{areaInfo[indexArea].name}" \n'

        if lr == 'true':
            command += f'{ctx.prefix}game longrest \n'
        else:
            command += f'{ctx.prefix}game shortrest \n'
            command += f'{ctx.prefix}game hp max \n'
else:
    command = f'echo Not in combat...'

return command
</drac2>