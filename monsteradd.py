!alias mon <drac2>
args = &ARGS&
monster = args[0]

if len(args) == 1:
  command = f'i madd "{monster}" -name "{monster}"'
else:
  if args[1].isnumeric():
    command = f'i madd "{monster}" -n {args[1]} -name "{monster+"#"}"'
  else:
    command = f'echo Second argument should be number'
return command
</drac2>
