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

![Captura de Pantalla 2022-06-09 a la(s) 19 30 24](https://user-images.githubusercontent.com/60671532/172968099-47743c83-d285-4969-ac6d-767be93f4f19.png)

![AlejandroMarquezCaballero_Joy](https://user-images.githubusercontent.com/60671532/172968154-e1a238b5-0a35-4893-9490-8ef46c1ee4a8.png)

![AlejandroMarquezCaballero_Sadness](https://user-images.githubusercontent.com/60671532/172968302-3c4e4be0-35fc-4fe2-8ae0-0acb32b5c1d5.png)

![AlejandroMarquezCaballero_Anger](https://user-images.githubusercontent.com/60671532/172968315-654e1cf4-f41e-46f3-af31-12ec9a7297fb.png)

![AlejandroMarquezCaballero_Fear](https://user-images.githubusercontent.com/60671532/172968320-131f72e9-9e21-4c3b-a92b-c11ef37c1623.png)

![AlejandroMarquezCaballero_Neutral](https://user-images.githubusercontent.com/60671532/172968326-2d1395a4-cf93-45a8-9354-af4234fc6a24.png)

![AlejandroMarquezCaballero_Objects](https://user-images.githubusercontent.com/60671532/172968346-d20fd6a3-1530-4981-b419-4fe4d9c038b1.png)





*** The purpose of this repository is to show the main file and the results we obtained after running it.
    All the codes were programmed in Python.
    
    Due to the code license, we did not make a continuous versioning 
    in the repository
