!serveralias join multiline
<drac2>
if combat():
    lr=get_svar('longrest')
    command = f'{ctx.prefix}init join -group Heroes \n'

    if "notSet" in combat().get_metadata("combatAreas","notSet"):
        command += f'echo combatAreas not initialized'
    else:
        areaInfo = load_json(combat().get_metadata("combatAreas"))
        areaInfo[0].members.append(character().name)
        combat().set_metadata("combatAreas",dump_json(areaInfo))

        if lr == 'true':
            command += f'{ctx.prefix}game longrest \n'
        else:
            command += f'{ctx.prefix}game shortrest \n'
else:
    command = f'echo Not in combat...'

return command
</drac2>


!alias welcome embed -title "¡Inicia la batalla!" -desc "Suenan las trompetas del coliseo de batallas, donde los guerreros prueban sus habilidades :trumpet:. Utiliza **!join** para unirte :stadium:"