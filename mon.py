!alias mon multiline <drac2>
#Args: !mon <name> <number> [token] [size]
args = &ARGS&
monster = args[0]
command = ''

if len(args) < 2:
  command = f'echo needs 2 arguments and 2 optional  <name> <number> [token] [size]'
else:
  if args[1].isnumeric():
    locs = ['o','p','q']
    i=1
    if len(args) == 2:
        while i <= int(args[1]):
            location = f'{randchoice(locs)}{randint(4,11)}'
            command += f'{ctx.prefix}i madd "{monster}" -note "Note: {monster}{i} | Location: {location}" -group "Monsters"\n'
            i+=1
    elif len(args) == 3:
        while i <= int(args[1]):
            location = f'{randchoice(locs)}{randint(4,11)}'
            command += f'{ctx.prefix}i madd "{monster}" -note "Note: {monster}{i} | Location: {location} | Token: {args[2]}" -group "Monsters"\n'
            i+=1
    elif len(args) == 4:
        while i <= int(args[1]):
            location = f'{randchoice(locs)}{randint(4,11)}'
            command += f'{ctx.prefix}i madd "{monster}" -note "Note: {monster}{i} | Location: {location} | Token: {args[2]} | Size: {args[3]}" -group "Monsters"\n'
            i+=1
  else:
    command = f'echo Second argument should be number'
return command
</drac2>
