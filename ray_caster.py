import sys
import commandline
import cast
import collisions
import vector_math
import data

defaults = {"min_x": -10, "max_x": 10, "min_y": -7.5, "max_y":7.5,
            "width": 1024, "height": 768, "eye_point": data.Point(0, 0, -14),
            "ambient_color": data.Color(1, 1, 1),
            "light": data.Light(data.Point(-100, 100, -100),
            data.Color(1.5, 1.5, 1.5)), "outfile": "image.ppm"}



def main(argv):
   argument_errors = commandline.argment_errors(defaults, argv)

   if not argument_errors[0]:
      print "Argument Error, a valid .in file is needed as the first argument."
      exit(1)
   sphere_list = commandline.get_sphere_list(argv[1])
   
   arg_dict = commandline.find_cast_args(defaults, argv)





   cast.cast_all_rays(defaults["min_x"], defaults["max_x"], defaults["min_y"],
         defaults["max_y"], defaults["width"], defaults["height"],
         defaults["eye_point"], sphere_list, defaults["ambient_color"], 
         defaults["light"], defaults["outfile"])

      

def process_line(line):
   val_list = line.strip().split()
   float_list = []
   if len(val_list) != 11:
      raise RuntimeError("The input file is not properly formatted")
   for i in range(len(val_list)):
      float_list.append(float(val_list[i]))
   return data.Sphere(data.Point(float_list[0], float_list[1], float_list[2]),
      float_list[3], data.Color(float_list[4], float_list[5], float_list[6]),
      data.Finish(float_list[7], float_list[8], float_list[9], float_list[10]))



      
      

      
if __name__ == "__main__":
   main(sys.argv)
