#!/bin/sh

input_dir=/data

output_dir=/data

surf_dir=$input_dir/001/surf

temp_dir=/tmp

echo ==================
echo running freesurfer
echo ==================

SUBJECTS_DIR=$input_dir

recon-all -subjid 001 -all -i $input_dir/*.nii*

cp $surf_dir/lh.pial $temp_dir/
cp $surf_dir/rh.pial $temp_dir/

echo ==================
echo converting meshes
echo ==================

mris_convert $temp_dir/lh.pial $temp_dir/lh.stl
mris_convert $temp_dir/rh.pial $temp_dir/rh.stl


echo ===================================
echo copying outputs to output directory
echo ===================================

cp $temp_dir/lh.stl $output_dir
cp $temp_dir/rh.stl $output_dir






