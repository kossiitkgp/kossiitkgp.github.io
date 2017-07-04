require 'html-proofer'
options =  { :assume_extension => true, :empty_alt_ignore => true, :checks_to_ignore =>["ImageCheck"], :http_status_ignore => [999]}
HTMLProofer.check_directory("./",options).run
