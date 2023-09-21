!alias matk multiline
#attack as a monster an include image
#Arguments: !matk <normal !i aoo arguments>
<drac2>
argstr = "&*&"
mon = &ARGS&[0]
monimgs=load_json(combat().get_metadata("monImgs"))

command = ''
mon_img = monimgs.get(mon)
if mon_img is not None:
    command += f'{ctx.prefix}i aoo {argstr} -thumb {mon_img}'
else:
    command += f'{ctx.prefix}i aoo {argstr} -thumb https://i.imgur.com/qOTuihZ.png'

return command
</drac2>




#Old matk with random
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
