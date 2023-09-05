#!/usr/bin/env ruby

input_string = ARGV[0]

sender_regex = /from:([\w\s-]+)/
receiver_regex = /to:([\w\s-]+)/
flags_regex = /flags:([0-9:-]+)/

sender = ''
receiver = ''
flags = ''

sender_match = input_string.match(sender_regex)
receiver_match = input_string.match(receiver_regex)
flags_match = input_string.match(flags_regex)

sender = sender_match[1] if sender_match
receiver = receiver_match[1] if receiver_match
flags = flags_match[1] if flags_match

puts "#{sender},#{receiver},#{flags}"
