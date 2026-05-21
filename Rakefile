require 'openc3/utilities/rake_helper'
task :require_version do
  unless ENV['VERSION']
    puts "VERSION is required: rake build VERSION=X.X.X"; exit 1
  end
end
task :build => [:require_version] do
  _, platform, *_ = RUBY_PLATFORM.split("-")
  if platform == 'mswin32' || platform == 'mingw32'
    puts `rake.cmd build VERSION=#{ENV['VERSION']}`
  else
    puts `rake build VERSION=#{ENV['VERSION']}`
  end
end
