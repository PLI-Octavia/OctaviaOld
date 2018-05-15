<-! octavia.register 'config_see'

throw new Error("no form config") unless form-config?
throw new Error("no current config") unless current-config?
handler = (key, value) ->
  current-config[key] = value
  gEBI 'inputconf' .value = JSON.stringify current-config
render-form-to gEBI('settings-form'), form-config, current-config, handler

