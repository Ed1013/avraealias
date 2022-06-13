!alias mon <drac2>
args = &ARGS&

if len(args) == 1:
  command = f'i madd %1% -name Monster1 -note %1%'
else:
  if args[1].isnumeric():
    command = f'i madd %1% -n {args[1]} -name Monster# -note %1%'
  else:
    command = f'echo Second argument should be number'
return command
</drac2>
