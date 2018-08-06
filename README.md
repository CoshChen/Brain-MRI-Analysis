# Brain-MRI-Analysis
This project focuses on the brain fMRI scans of patients of degenerative nerve diseases (e.g. Alzheimer's disease, Parkinson's disease) and healthly controls.

# Data Preprocessing
1. The raw fMRI scan sequences are loaded and exported as DICOM images by [RadiAnt](https://www.radiantviewer.com/).
2. Use [MRIcron](http://people.cas.sc.edu/rorden/mricron/index.html) to converting DICOM images to 3D NIfTI format (for T1 scans) or 4D NIfTI format (BOLD and DTI scans). In this project, the **reoriented** T1 NIfTi files are used in the next step. Please refer to [dcm2nii](http://people.cas.sc.edu/rorden/mricron/dcm2nii.html) for details of the output NIfTI files.
3. The brain features from a T1 NIfTi file is extracted by [BrainSuite](http://brainsuite.org/). The [Surface-Volume Registration](http://brainsuite.org/processing/svreg/) (SVReg) procedure using BrainSuiteAtlas1 then generates a tab-deliminated text file (fileprefix.roiwise.stats.txt) containing the volume (mm3) and (where applicable) average cortical thickness (mm) of labeled structures.
4. The text file from step 3 is loaded and exported as a csv file (fileprefix_stat.csv) for further use.


# Python Scripts
After data preprocessing, each subject in the study is associated with a csv file that contains features of every brain ROI (region of interest). Below is an example of the csv file for a subject. Note that the numbers shown here are not from the real world dataset.

![](https://github.com/CoshChen/Brain-MRI-Analysis/blob/master/HC%20T1/Example_DataFormat.png)


* ## DataScript.py
  This script goes through csv files for all subjects in a particular group and produces 5 csv files with each row corresponds to one subject and each column corresponds to a brain ROI:
  
  - groupprefix_mean_thickness.csv (value = mean thickness)
  - groupprefix_gm_vol.csv (value = volume of gray matter)
  - groupprefix_csf_vol.csv (value = volume of cerebrospinal fluid)
  - groupprefix_wm_vol.csv (value = volume of white matter)
  - groupprefix_cortical_area.csv (value = cortical area)
  
  
  Here is the format of all output csv files. It shows two subjects (ID = H001, H002) from the group 'HC' and brain regions 120, 121, 130, 131, and 142. Note that the numbers are not from the real world dataset.
  
  ![](https://github.com/CoshChen/Brain-MRI-Analysis/blob/master/Example_DataScript_Output.png)


* ## TTestScript.py
  This script helps to find the ROI features that have significant difference between two subject groups. It summarizes the brain ROI features for each group and performs t-test. The output is a single csv file (ROI_two_groups_summary.csv) with columns: ROI', Group_1 Mean, Group_1 Sd, Group_2 Mean, Group_2 Sd, T Value, P value. The rows of the table are sorted by the P value in ascending order. An example output is shown below:
  
  ![](https://github.com/CoshChen/Brain-MRI-Analysis/blob/master/Example_TTtestScript_Output.png)
