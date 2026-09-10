import numpy as np
from pymatgen.core import Structure,Lattice
##############################step1_get_input
setting_R=5.0
setting_element="Fe"
setting_file_cif="./example_Fe3O4/Fe3O4_icsd20596_P1.cif"#CIF文件

setting_Sample_N=1000
setting_Sample_range_xyz=[-0.3,0.3]
setting_Sample_low_abc=[8.2,8.2,8.2,90,90,90]
setting_Sample_high_abc=[8.6,8.6,8.6,90,90,90]
setting_Sample_absorber=[0,23]#absorber index from 0
##############################step3 finetune model
setting_nepoch=3
setting_file_original_model="ASESc2Zn_unconv_best256_3_0.0005_5_2_82_5.pt"
setting_file_finetune_model="ASE_Fe3O4_1.pt"
##############################step4 fitting 
setting_fit_initial_cif="./example_Fe3O4/Fe3O4_icsd20596_P1.cif"
setting_fit_f_exp="./example_Fe3O4/Fe3O4.nor"#"JT.exp"
setting_fit_using_model="ASE_Fe3O4_1.pt"
setting_fit_ifvalid=False
setting_fit_R=5.0
setting_fit_absorber=range(24)
setting_fit_maxeval=3
setting_fit_maxsec=60*10
setting_fit_inner_maxeval=2000  #default 2000
# setting_fit_mode="Structure_lattice_xyz"#"self_define"
# setting_fit_rel_x_a=-0.3
# setting_fit_rel_x_b= 0.3
# setting_fit_rel_x_0=0.0
# setting_fit_abs_lattice_a=[8.3,8.3,8.3,90,90,90]
# setting_fit_abs_lattice_b=[8.5,8.5,8.5,90,90,90]
# setting_fit_abs_lattice_0=[8.4,8.4,8.4,90,90,90]
setting_fit_mode="self_define"#"self_define"
setting_fit_self_define_npar=6+3*56
setting_fit_self_define_xa=-0.3*np.ones(setting_fit_self_define_npar)
setting_fit_self_define_xa[0:6]=[8.3,8.3,8.3,90,90,90]
setting_fit_self_define_xb=0.3*np.ones(setting_fit_self_define_npar)
setting_fit_self_define_xb[0:6]=[8.5,8.5,8.5,90,90,90]
setting_fit_self_define_x0=0*np.ones(setting_fit_self_define_npar)
setting_fit_self_define_x0[0:6]=[8.4,8.4,8.4,90,90,90]
def change_structure_self_define(x,structure0,frac0,cart0,abc0,species,natom):
    # print("IN change_structure_self_define")
    # natom=56#number of atoms defination deirectly
    ipar = x[6:]
    ipar = ipar.reshape(natom, 3)  # HERE not i id
    icart_coords = cart0 + ipar
    lattice=Lattice.from_parameters(x[0],x[1],x[2],x[3],x[4],x[5])
    istructure = Structure(lattice, species, icart_coords, coords_are_cartesian=True)  # coords_are_cartesian=True
    return istructure