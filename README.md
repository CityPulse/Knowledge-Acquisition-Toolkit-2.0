# KAT (Knowledge Acquisition Toolkit) version 2

 The Knowledge Acquisition Tool (KAT) is a software toolkit that implements the state-of-the-art machine learning and data analytic methods for sensors data. The algorithms and methods implemented in KAT are used for processing and analysing the smart city data in the CityPulse project in the Data aggregation and Event processing components.  

To run KAT go to src folder and run MainGUI.py

KAT follows a simple processing approach. We use a general workflow that has been extracted by observing several different solutions for information abstraction. The existing solutions either follow the steps shown in the figure below or implement some parts of it. We identified the following main steps: Pre-processing to bring the data into shape for further processing, Dimensionality Reduction to either compress the data or reduce its feature vectors, Feature Extraction to find low-level Abstractions in local sensor data, Abstraction from raw data to higher-level Abstractions and finally semantic representations to make the abstracted data available for the end-user and/or machines that interpret the data.

![alt tag](http://kat.ee.surrey.ac.uk/graph/flow.png)

(Source: Frieder Ganz, Daniel Puschmann, Payam Barnaghi, Francois Carrez, "A Practical Evaluation of Information Processing and Abstraction Techniques for the Internet of Things", IEEE Internet of Things Journal, 2015.)

# Pre-Processing
The raw sensory data is pre-processed stage to prepare the data for information acquisition. Pre-processing can be done on sensor nodes to reduce transmission cost or filter unwanted data and can include mathematical/statistical methods to smooth the data by applying moving average windows, or methods from signal processing such as band-, low-, high pass filtering to focus on a certain frequency spectrum.

Transmission cost can be reduced by only sending aggregated information or a selection of data to a base-station or a gateway; e.g. sending minimum and/or maximum values or the mean value of the current window. The pre-processing is not only limited to a single sensor node; some solutions use in-network processing to aggregate the data before further processing it by finding the minimum, mean or maximum value in a set of sensor nodes and before transmitting the data to a base station. In addition to data aggregation, in-network techniques can also be used to improve the accuracy of the data by calculating correlation with data from neighbouring nodes.

# Dimensionality Reduction
To handle the large amount of data that has to be processed and stored. Dimensionality reduction can decrease the size and length of samples by applying different methods on the data while preserving the important features and patterns.

This section presents a simple example based on a dataset gathered in an office environment consisting of several hundred thousand sensor readings. The sensor was deployed near an office desk and measured light level, PIR, sound, and energy consumption of an office workstation. The dataset can be downloaded here: http://kat.ee.surrey.ac.uk/download.html


# Data Import
The first step is the data import. KAT currently supports CSV and MS Excel formats. To import data click on the Load Data button and select a comma separated file or an MS Excel file. You can download the sample dataset (http://kat.ee.surrey.ac.uk/download.html), save it as a csv file and import it to KAT.

![alt tag](https://github.com/UniSurreyIoT/KAT-v2/blob/master/imgs/Sc1.PNG)


Once the data is imported, the labels will appear on the screen. Select "light" check box from the data labels to show the data in a diagram (as shown below). In case that the data is not shown, select check box and left click on empty diagram.

The current version uses the ‘timestamp’ to provide some information about the dataset, e.g. number of days included, number of samples per day/hour (To use this feature, the time label should be called ‘timestamp’). 

Furthermore, this version provides additional visual settings, such as moving along the plotted data and zooming in for a desired window. For instance, the following figure shows a zoomed-in section of the uploaded data.




# Data Pre-Processing
To highlight features of the data set, a mean filter (i.e. moving average) is used in this example. The mean filter divides the data into windows (where window length is selected as a parameter) and replaces each window with the mean value. This filter can highlight outliers and reduces the noise. Please select the desired algorithm and its parameter (if required) and click ‘Run’ to see the output. 

Note that the new version allows you to save your output at each step. To this end, click on the corresponding press button (in front of ‘Save Output’), select the name and format, and save the data.


![alt tag](https://github.com/UniSurreyIoT/KAT-v2/blob/master/imgs/Sc2.PNG)

The use of more than one pre-processing algorithm is supported. For example, the following figure shows the dataset after applying the ‘outlier removal’ on the previous output.


![alt tag](https://github.com/UniSurreyIoT/KAT-v2/blob/master/imgs/Sc3.PNG)

![alt tag](https://github.com/UniSurreyIoT/KAT-v2/blob/master/imgs/Sc4.PNG)



# Dimension Reduction

Due to the large number of sensor nodes and high sampling rates of sensor data, the amount of data is not bearable for many data processing algorithms. Therefore, dimensionality reduction techniques are usually used to reduce the number of features from a high dimensional space to a low-dimensional representation.  Here we use a technique called PAA (Piecewise Aggregate Approximation). PAA requires a parameter, which defines the ratio of reduction. For instance, the PAA parameter is set as 100 in our example, meaning that the number of samples per hour is changing from 361 to ~3.61 

![alt tag](https://github.com/UniSurreyIoT/KAT-v2/blob/master/imgs/Sc5.PNG)


#Contributers
KAT was developed as part of the EU project CityPulse. The consortium member University of Surrey provided the main contributions for this component.
