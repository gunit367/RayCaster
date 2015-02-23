def find_cast_args(defaults, argv):
   return defaults
   
   
def included_file(argv):
   if len(argv) < 2:
      return False
   filename = argv[1]
   if ".in" in filename:
      return True
   else:
      return False
     
     
def get_sphere_list(filename):
   sphere_list = []
   try:
      file = open(filename, "rb")
      for line in file:
         sphere_list.append(process_line(line))
   except:
      print "EEEE"
      exit(1)

   return sphere_list   
   
