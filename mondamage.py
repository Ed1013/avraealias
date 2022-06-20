!alias mondam <drac2>
#!mondam <damage>
args = &ARGS&

string = '\n'
if combat():
  for mon in combat().combatants:
      if mon.group == 'Monsters':
          string += f'{mon.name} takes {args[0]} damage!\n'
          mon.set_hp(mon.hp - int(args[0]))

else:
  string = f'Not in combat...'

string = 'echo ' + string

return string
</drac2>
