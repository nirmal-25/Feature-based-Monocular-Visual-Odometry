import os
from os import listdir, system
from os.path import isfile, join

GroundTruth = {"00": "../data/dataset/poses/00.txt",
      "01": "../data/dataset/poses/01.txt",
      "02": "../data/dataset/poses/02.txt",
      "03": "../data/dataset/poses/03.txt",
      "04": "../data/dataset/poses/04.txt",
      "05": "../data/dataset/poses/05.txt",
      "06": "../data/dataset/poses/06.txt",
      "07": "../data/dataset/poses/07.txt",
      "08": "../data/dataset/poses/08.txt",
      "09": "../data/dataset/poses/09.txt"
               }
output_dir = join(os.getcwd(), "../data/output")

if not os.path.isdir(output_dir):
      os.mkdir(output_dir)
for dir in listdir(output_dir):
      if dir[0] == "T":

            current = join(os.getcwd(), dir)
            out = join(output_dir, dir)
            out_ate = join(out, "ate")
            out_rpe = join(out, "rpe")
            if not os.path.isdir(out):
                  os.mkdir(out)
            if not os.path.isdir(out_ate):
                  os.mkdir(out_ate)
            if not os.path.isdir(out_rpe):
                  os.mkdir(out_rpe)
            files = [os.path.splitext(f)[0] for f in listdir(current) if isfile(join(current, f))]
            for file in files:

                  gt = GroundTruth[file]
                  txt_file = join(dir, file + ".txt")

                  out_name = dir[3:] + file
                  out_txt = out_name + ".txt"
                  out_ate_name = join(out_ate, out_name)
                  out_ate_txt =  join(out_ate, out_txt)
                  out_rpe_name = join(out_rpe, out_name)
                  out_rpe_txt =  join(out_rpe, out_txt)

                  system("evo_rpe kitti {} {} --save_plot {} > {}".format(gt, txt_file, out_rpe_name, out_rpe_txt))
                  system("evo_ape kitti {} {} --save_plot {} > {}".format(gt, txt_file, out_ate_name, out_ate_txt))

