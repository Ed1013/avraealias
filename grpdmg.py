!alias grpdmg <drac2>
#!grpdmg <group> <damage>
args = &ARGS&

string = '\n'
if combat():
  for mon in combat().combatants:
      if mon.group == args[0]:
          string += f'{mon.name} takes {args[1]} damage!\n'
          mon.set_hp(mon.hp - int(args[1]))

else:
  string = f'Not in combat...'

string = 'embed -desc \"' + string + '\" -color #fc3503'

return string
</drac2>
