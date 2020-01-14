import nibabel
import numpy as np
import matplotlib.pyplot as plt

T1_path = 'IXI012-HH-T1/mri/norm.mgz'
T2_path = 'IXI012-HH-T2/mri/nu.mgz'

T1_file = nibabel.load('BraTS19/BraTS19_2013_3_1_t1.nii.gz')
T2_file = nibabel.load('BraTS19/BraTS19_2013_ 3_1_t2.nii.gz')

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


print(T1_file.affine)
print(T2_file.affine)

T1_file,T1_orientation = orient_correctly(T1_file)
T2_file,T2_orientation = orient_correctly(T2_file)



plt.subplot(1,2,1)
plt.imshow(T1_file[:,120,:])
plt.subplot(1,2,2)
plt.imshow(T2_file[:,153,:])

plt.show()