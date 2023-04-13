!alias matk <drac2>
args = &ARGS&

targets = []
for tar in combat().combatants:
    if tar.group == 'Heroes':
        targets.append(tar.name)

if not targets:
	TAR = ""
else:
	TAR = randchoice(targets)

#ARGS !matk <monster name> <attack name> <no. of attacks>
if len(args)<=3 and len(args)>=1:
    if len(args) == 1:
        command = f'i aoo {args[0]}'
    elif len(args) == 2:
        command = f'i aoo {args[0]} {args[1]}'
    elif len(args) == 3:
        command = f'i aoo {args[0]} {args[1]} -rr {args[2]}'
    command += f' -t {TAR} -thumb https://i.imgur.com/ZjDpFlO.jpg'
else:
    command = f'echo invalid number of arguments'

return command
</drac2>

#include monster image
!snippet monimg -thumb https://www.dndbeyond.com/avatars/thumbnails/30836/551/1000/1000/638063939544338029.png