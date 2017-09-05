set :application, "octavia"
set :branch, ENV['BRANCH'] || 'master'
set :exclude_dir, [".svn", ".git", ".gitignore", "Capfile", "README.md", "readme.txt", "README.txt", "Changelog.txt", "CHANGELOG.txt", "CHANGELOG.md", "cache", "logs", "sessions"]
set :include_dir, '.'
# set :linked_dirs, ["var/logs","var/sessions","var/tmp","web/media","web/uploads"]
set :log_level, :error
set :repo_url, "git@github.com:PLI-Octavia/Octavia.git"
set :scm, :copy
set :stages, %w(Production)
set :use_sudo, false

namespace :deploy do
	before :starting, :preparehosting
	before :publishing, :install
	before :finishing, :clean
end