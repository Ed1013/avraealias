!alias mon <drac2>
#Args: !mon <name> <number> <location>
args = &ARGS&
monster = args[0]

if len(args) < 3:
  command = f'echo needs 3 arguments  <name> <number> <location>'
else:
  if args[1].isnumeric():
    command = f'i madd "{monster}" -n {args[1]} -note "Note: {monster} | Location: {args[2]}" -group "Monsters"'
  else:
    command = f'echo Second argument should be number'
return command
</drac2>
