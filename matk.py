!alias matk <drac2>
args = &ARGS&
monster = combat().current

targets = []
for tar in combat().combatants:
    if tar.group == 'Heroes':
        targets.append(tar.name)

if not targets:
	TAR = ""
else:
	TAR = randchoice(targets)

if len(args) == 0:
    ATK = randchoice(combat().current.attacks).name
    command = f'i attack {ATK} -t {TAR} -thumb https://i.imgur.com/ZjDpFlO.jpg'
elif len(args) == 1:
    command = f'i attack {args[0]} -t {TAR} -thumb https://i.imgur.com/ZjDpFlO.jpg'
elif len(args) == 2:
    command = f'i attack {args[0]} -t {TAR} -thumb https://i.imgur.com/ZjDpFlO.jpg -rr {args[1]}'
else:
    command = f'echo invalid number of arguments'

return command
</drac2>
