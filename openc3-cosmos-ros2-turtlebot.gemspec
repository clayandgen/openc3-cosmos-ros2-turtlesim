Gem::Specification.new do |s|
  s.name        = "openc3-cosmos-ros2-turtlebot"
  s.version     = ENV['PLUGIN_VERSION'] || '0.0.1'
  s.summary     = "OpenC3 COSMOS plugin for TURTLEBOT (ROS2 via rosbridge)"
  s.description = "Generated from openc3-cosmos-ros2 scaffolding."
  s.authors     = ['You']
  s.license     = 'AGPL-3.0-only'
  s.files       = Dir['plugin.txt','requirements.txt','LICENSE.txt','README.md','targets/**/*']
end
