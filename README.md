# NIfTI_Converter
>*Convert (ima/mha/mnc) file formats to the universally accepted NIfTI format for Brain MRI.*

### Documentation and Support
To run: 
$>python3 converter.py -i DICOM -o NIfTI

-i: input DICOM Folder(.ima)/MetaImage(.mha)/MINC(.mnc)

-o: specify output directory (optional)

### Examples
Example1:
$>python3 converter.py -i DICOM -o NIfTI

Example2:
$>python3 converter.py -i subject04_t1w_p4.mnc.gz -o Subject4

Example3:
$>python3 converter.py -i SimTumor00T_T1.mha -o TumorSim

### Required Libraries 
dicom2nifti (DICOM     .ima)  Tested Version: 2.1.7
nibabel     (MINC      .mnc)  Tested Version: 2.5.0
SimpleITK   (MetaImage .mha)  Tested Version: 1.2.2 

### Sample Files
DICOM: [NCIGT Intra-operative MRT Glioma Resection](https://central.xnat.org/app/action/DisplayItemAction/search_element/xnat%3AprojectData/search_field/xnat%3AprojectData.ID/search_value/IGT_GLIOMA)
MINC: [BrainWeb](https://brainweb.bic.mni.mcgill.ca/brainweb/anatomic_normal_20.html)
MetaImage: [TumorSim](https://www.nitrc.org/projects/tumorsim/)
