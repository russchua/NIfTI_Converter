import nibabel
import numpy as np
import matplotlib.pyplot as plt

T1_path = 'IXI012-HH-T1/mri/norm.mgz'
T2_path = 'IXI012-HH-T2/mri/nu.mgz'

T1_file = nibabel.MGHImage.from_filename(T1_path)
T2_file = nibabel.MGHImage.from_filename(T2_path)

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

print(new_T1_midpoint,new_T2_midpoint)

print(T1_file.affine)
print(T2_file.affine)

T1_file,T1_orientation = orient_correctly(T1_file)
T2_file,T2_orientation = orient_correctly(T2_file)



plt.subplot(1,2,1)
plt.imshow(T1_file[:,120,:],cmap='jet')
plt.imshow(T2_file[:254,153,11:],alpha=0.6,cmap='gist_earth')

plt.subplot(1,2,2)
plt.imshow(T1_file[:,120,:],cmap='jet')
plt.imshow(T2_file[:,153,:],alpha=0.6,cmap='gist_earth')

plt.show()