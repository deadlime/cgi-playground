#!/usr/bin/ruby
require 'pp'

puts "Content-Type: text/plain\n\nHello World!"

puts "\nEnvironment:"
puts ENV.pretty_inspect

puts "\nInput:"
puts STDIN.read.pretty_inspect
