# Brain-MRI-Analysis
This project focuses on the brain fMRI scans of patients of degenerative nerve diseases (e.g. Alzheimer's disease, Parkinson's disease) and healthly controls.

# Data Preprocessing
1. The raw fMRI scan sequences are loaded and exported as DICOM images by [RadiAnt](https://www.radiantviewer.com/).
2. Use [MRIcron](http://people.cas.sc.edu/rorden/mricron/index.html) to converting DICOM images to 3D NIfTI format (for T1 scans) or 4D NIfTI format (BOLD and DTI scans). In this project, the **reoriented** T1 NIfTi files are used in the next step. Please refer to [dcm2nii](http://people.cas.sc.edu/rorden/mricron/dcm2nii.html) for details of the output NIfTI files.
3. The brain features from a T1 NIfTi file is extracted by [BrainSuite](http://brainsuite.org/). The [Surface-Volume Registration](http://brainsuite.org/processing/svreg/) (SVReg) procedure using BrainSuiteAtlas1 then generates a tab-deliminated text file (fileprefix.roiwise.stats.txt) containing the volume (mm3) and (where applicable) average cortical thickness (mm) of labeled structures.
4. The text file from step 3 is loaded and exported as a csv file (fileprefix_stat.csv) for further use.

# Scripts
After data preprocessing, each subject in the study is associated with a csv file that contains features in each brain ROI (region of interest).
