server ENV['DEPLOY_PRODUCTION_SERVER'], user: ENV['DEPLOY_PRODUCTION_USER'], roles: %w{app db web}
if "#{fetch(:branch)}" == "master"
	set :current_domain, "#{fetch(:application)}." + ENV['DEPLOY_PRODUCTION_DOMAIN']
else
	set :current_domain, "#{fetch(:application)}-#{fetch(:branch)}." + ENV['DEPLOY_PRODUCTION_DOMAIN']
end
set :default_domain, "#{fetch(:application)}." + ENV['DEPLOY_PRODUCTION_DOMAIN']
set :default_deploy_to, "/webapps/octavia/#{fetch(:default_domain)}"
set :deploy_to, "/webapps/octavia/#{fetch(:current_domain)}"
set :keep_releases, 1