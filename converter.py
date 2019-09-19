import os
os.mkdir('PythonProjects')

parser = argparse.ArgumentParser(
    description='''NIfTI_converter
            Convert files from mnc,ima or mha formats to the universally accepted NIfTI format.
            -i or --input-file: Input MRI ima folder / mnc or mha file path
            -o or --output-dir: A filepath to the output directory. 
            -m or --model-file: model file to be used
            -gpu: GPU id to be used for computation
            --output-soft: Probabilistic output image is saved
            -p or --patch-dim: patch size to be used

                ''')
parser.add_argument('-i', '--input-file', type=str, required=True)
parser.add_argument('-o', '--output-dir', type=str, required=True)
parser.add_argument('-pre', '--preprocess', action='store_true')
parser.add_argument('-m', '--model-file', type=str, required=False)
parser.add_argument('-c', '--contrast', type=str, required=False)
parser.add_argument('-gpu', nargs='?', const=0, default=0, type=int)
# parser.add_argument('-os', '--output-soft', action='store_true')
parser.add_argument('-p', '--patch-size', type=int, choices=[64, 96], default=96)
# parser.add_argument('-b', '--batch-size', type=int, required=False, default=4)
args = parser.parse_args()
print(args)
for argname in ['input_file']:
    setattr(args, argname, os.path.abspath(os.path.expanduser(getattr(args, argname))))
    if not os.path.exists(getattr(args, argname)):
        raise RuntimeError('%s: %s does not exist. Exiting.' % (argname.replace('_', ' ').title(),
                                                                getattr(args, argname)))
