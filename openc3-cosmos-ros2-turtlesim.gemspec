# encoding: ascii-8bit

# Create the overall gemspec
Gem::Specification.new do |s|
  s.name = 'openc3-cosmos-ros2-turtlesim'
  s.summary = 'ROS2 Turtlesim'
  s.description = <<-EOF
    ROS2 Plugin to interact with a TurtleSim
  EOF
  s.license = 'MIT'
  s.authors = ['Clay Kramp']
  s.email = ['clay@openc3.com']
  s.homepage = 'https://github.com/clayandgen/openc3-cosmos-ros2-turtlesim'
  s.platform = Gem::Platform::RUBY
  s.required_ruby_version = '>= 3.0'
  s.metadata = {
    'openc3_store_keywords' => 'ROS2, TurtleSim, Sim',
    'source_code_uri' => 'https://github.com/clayandgen/openc3-cosmos-ros2-turtlesim',
    'openc3_store_access_type' => 'public',
    "openc3_cosmos_minimum_version" => "7.0.0",
  }

  if ENV['VERSION']
    s.version = ENV['VERSION'].dup
  else
    time = Time.now.strftime("%Y%m%d%H%M%S")
    s.version = '0.0.0' + ".#{time}"
  end
  s.files = Dir.glob("{targets,lib,public,tools,microservices}/**/*") + %w(Rakefile README.md LICENSE.txt plugin.txt requirements.txt)
end
