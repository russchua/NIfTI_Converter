import nibabel
import numpy as np
import matplotlib.pyplot as plt

# T1_path = 'IXI_Freesurfer/T1_files/norm.mgz'
# T2_path = 'IXI_Freesurfer/T2_files/nu.mgz'

T1_path = 'IXI_Basic/subject_1/IXI002-Guys-0828-T1.nii.gz'
T2_path = 'IXI_Basic/subject_1/IXI002-Guys-0828-T2.nii.gz'

def opening_mgz_file(mgz_file):
    mgz_file = nibabel.MGHImage.from_filename(mgz_file)
    return mgz_file

def opening_NIfTI_file(nii_file):
    nii_file = nibabel.load(nii_file)
    return nii_file

def open_file(any_file):
    if '.mgz' in any_file:
        return opening_mgz_file(any_file)
    else:
        return opening_NIfTI_file(any_file)

T1_file = open_file(T1_path)
T2_file = open_file(T2_path)

def orient_correctly(img_nii):
    orientation = nibabel.io_orientation(img_nii.affine)
    try:
        img_new = nibabel.as_closest_canonical(img_nii, True).get_data().astype(float)
    except:
        img_new = nibabel.as_closest_canonical(img_nii, False).get_data().astype(float)
    img_trans = np.transpose(img_new, (0,2,1))
    img_flip = np.flip(img_trans,0)
    img_flip = np.flip(img_flip,1)
    return img_flip, orientation


T1_midpoint = (np.array(T1_file.shape) - 1) / 2.
T2_midpoint = (np.array(T2_file.shape) - 1) / 2.

new_T1_midpoint = nibabel.affines.apply_affine(T1_file.affine,T1_midpoint)
new_T2_midpoint = nibabel.affines.apply_affine(T2_file.affine,T2_midpoint)

difference = new_T1_midpoint - new_T2_midpoint

print(difference)


T1_file,T1_orientation = orient_correctly(T1_file)
T2_file,T2_orientation = orient_correctly(T2_file)

plt.subplot(1,2,1)
plt.imshow(T1_file[:,100,:])
plt.subplot(1,2,2)
plt.imshow(T2_file[:,88,:])



# plt.subplot(1,2,1)
# plt.imshow(T1_file[:,120,:],cmap='jet')
# plt.imshow(T2_file[:254,153,11:],alpha=0.6,cmap='gist_earth')

# plt.subplot(1,2,2)
# plt.imshow(T1_file[:,120,:],cmap='jet')
# plt.imshow(T2_file[:,153,:],alpha=0.6,cmap='gist_earth')

plt.show()