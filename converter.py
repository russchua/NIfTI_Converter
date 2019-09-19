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
parser.add_argument('-t', '--file-type', type=str, required=False)
args = parser.parse_args()

#####Create a folder of it doesn't exist, to store the converted NIfTI files#####
def check_file_type(input_file):
    if('.mnc' in input_file):
        return('mnc')
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

def convert_mnc(input_file,output_dir):
    from nibabel import load, save, Nifti1Image
    import numpy as np
    minc = load(input_file)
    basename = minc.get_filename().split(os.extsep, 1)[0]
    affine = np.array([[0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 1]])
    out = Nifti1Image(minc.get_data(), affine=affine)
    save(out, output_dir+'/'+basename + '.nii.gz')    

def convert_mha(input_file,output_dir):
    import SimpleITK as sitk
    img = sitk.ReadImage(input_file)
    sitk.WriteImage(img,output_dir + '/' + input_file[:-4] + '.nii')

#####Choose the right conversion function#####
def choose_convert(file_type,input_dir,output_dir):
    if (file_type == 'ima'):
        convert_ima(input_dir,output_dir)
    elif (file_type == 'mnc'):
        convert_mnc(input_dir,output_dir)
    elif (file_type == 'mha'):
        convert_mha(input_dir,output_dir)
    else:
        print('Unidentified file type')



check_directory(args.output_dir)
file_type = check_file_type(args.input_file)
choose_convert(file_type,args.input_file,args.output_dir)


print(file_type)

'''
for argname in ['input_file']:
    setattr(args, argname, os.path.abspath(os.path.expanduser(getattr(args, argname))))
    if not os.path.exists(getattr(args, argname)):
        raise RuntimeError('%s: %s does not exist. Exiting.' % (argname.replace('_', ' ').title(),
                                                                getattr(args, argname)))
'''