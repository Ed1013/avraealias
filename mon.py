!alias mon multiline <drac2>
#Args: !mon <name> <number> [token] [size]
args = &ARGS&
pargs = argparse(&ARGS&)
monster = args[0]
command = ''
embeds = ''

if len(args) < 2:
  command = f'echo needs 2 arguments and 2 optional <name> <number> -img [monster image]'
else:
  if args[1].isnumeric():
    i=1
    while i <= int(args[1]):
        command += f'{ctx.prefix}i madd "{monster}" -group "Monsters"\n'
        i+=1
  else:
    command = f'echo Second argument should be number'

embeds += f'{ctx.prefix}embed -title ":crossed_swords: Nuevo Contrincante :imp:" -desc "{monster}" entra a la batalla!'
if pargs.last("img",default=None) is not None:
  embeds += f' -image {pargs.last("img")}'
embeds += "\n"
return command + "\n" + embeds
</drac2>