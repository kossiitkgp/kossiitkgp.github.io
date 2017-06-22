require 'html-proofer'
options =  { :assume_extension => true, :empty_alt_ignore => true, :checks_to_ignore =>["ImageCheck"]}
HTMLProofer.check_directory("./",options).run
