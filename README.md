# NIfTI_Converter
>*Convert (ima/mha/mnc) file formats to the universally accepted NIfTI format for Brain MRI.*

### Documentation and Support
To run: 
$>python3 converter.py -i DICOM -o NIfTI

-i: input DICOM Folder(.ima)/MetaImage(.mha)/MINC(.mnc)

-o: specify output directory (optional)

### Required Libraries 
dicom2nifti (DICOM     .ima)  Tested Version: 2.1.7
nibabel     (MINC      .mnc)  Tested Version: 2.5.0
SimpleITK   (MetaImage .mha)  Tested Version: 1.2.2 
