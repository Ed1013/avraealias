!alias grpdmg <drac2>
#applies damage to a group
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

!alias multidmg 
<drac2>
#!multidmg -dmg <damage to apply> -t <list of members to apply damage to>
args = argparse(&ARGS&)
damage = args.get("dmg")[0]
string = ''
if combat():
  for member in args.get("t"):
    combatmem = combat().get_combatant(member) 
    if combatmem is None:
      string += f'{member} is not in the combat.\n'
    else:
      string += f'{combatmem.name} takes {damage} damage! '
      combatmem.set_hp(combatmem.hp - int(damage))
      string +=f'{combat().get_combatant(combatmem.name).hp_str()}\n'

else:
  string = f'Not in combat...'

string = 'embed -desc \"' + string + '\" -color #fc3503'

return string
</drac2>