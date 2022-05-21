# EEG-Signal-Processing-Related-to-Emotions

This project aimed to analyze and characterize an electroencephalographic signal of 19 electrodes using 
the frequency, amplitude, absolute and relative power in two states: awake and sleep.

I developed a method to select the bad segments related to movement artifacts, filter the signal, and 
select the close eyes segment in the awake state, and the sleep segment in the other case. Once the 
segment is selected and cropped, the Independent Component Analysis Algorithm (ICA) is used to identify 
the artifacts related to eye movement and heartbeats. It is important to mention that the selection of 
the components related to these artifacts is automatic and, in the same way, removed to clean the signal.

Later, with the signal without noise and artifacts, it continues with amplitude, frequency, absolute, and 
relative power calculation in six analysis areas: front, central, posterior, left, medium, and right.

To visualize the results, graphs are shown with the amplitude and absolute power values in each channel, 
and another one with the maps of the spectral power in the frequency bands: delta, theta, alpha, beta 1, 
beta 2, and gamma. Further, all the calculated values ​​are printed in the console.

Finally, when the program ends, an excel file was created with the patient information and all the data 
printed in the console.


*** The purpose of this repository is to show the main file and the results we obtained after running it.
    All the codes were programmed in Python.
    
    Due to the code license, we did not make a continuous versioning 
    in the repository
