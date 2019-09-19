import os
import argparse


parser = argparse.ArgumentParser(
    description='''NIfTI_converter
            Convert files from mnc,ima or mha formats to the universally accepted NIfTI format.
            -i or --input-file: Input MRI ima folder / mnc or mha file path
            -o or --output-dir: A filepath to the output directory. 
                ''')
parser.add_argument('-i', '--input-file', type=str, required=True)
parser.add_argument('-o', '--output-dir', type=str, required=False, default='NIfTI')
args = parser.parse_args()


def check_file_type(input_file):
    if input_file[-4] != '.':
        return ('ima')
    elif(input_file[-4:] == '.nii'):
        print('This is already a NIfTI file.')
        exit()
    else:
        return input_file[-3:]    


def check_directory(output_dir):    
    if(os.path.exists(output_dir)):
        print('no directory created')
        return True
    else:
        os.mkdir(output_dir)
        print('created directory')
        return True

#####Conversion Functions#####
def convert_ima(input_dir,output_dir):
    import dicom2nifti
    import dicom2nifti.settings as settings

    settings.disable_validate_orthogonal()
    settings.enable_resampling()
    settings.set_resample_spline_interpolation_order(1)
    settings.set_resample_padding(-1000)

    dicom2nifti.convert_directory(input_dir, output_dir)    


print(args.output_dir)
print(args.input_file)
check_directory(args.output_dir)
check_file_type(args.input_file)

'''
for argname in ['input_file']:
    setattr(args, argname, os.path.abspath(os.path.expanduser(getattr(args, argname))))
    if not os.path.exists(getattr(args, argname)):
        raise RuntimeError('%s: %s does not exist. Exiting.' % (argname.replace('_', ' ').title(),
                                                                getattr(args, argname)))
'''