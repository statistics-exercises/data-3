# Calculating the data range

You have now written your first program to perform statistical analysis. 

The mean you have just calculated is an example of something called a summary statistic.  Summary statistics are useful because they allow us to summarise information contained in our data set using fewer number.  In the example you have just completed, for example, we reduced a set of 200 numbers to a single number by calculating the mean.

The mean is not the only summary statistic we can compute.  For example, if we were writing a report about our results we might want to summarise the experimental data that we obtained using a sentence like the one below:

_N measurements of this quantity were obtained.  The lowest value obtained was L, while the highest value was U._

This sentence provides a one-line summary of the range of results that we obtained in the experiment.  Furthermore, we can use python to determine the largest and smallest values in a np.array called myarray by using the commands:

````
lowest = min( myarray )
highest = max( myarray )
````

To complete this task write a program that determines the values that should be used to replace `L` and `U` in the sentence in italics above given the data in the `data.dat` file.  I have loaded this data into an array called `x` for you.  To pass the test you will need to define two variables called `L` and `U` in your code.  The values of these variables should be set so that the sentence in italics above is true.     
