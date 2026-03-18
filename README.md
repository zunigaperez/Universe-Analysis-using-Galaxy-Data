**Domain Area**
<br>

The Domain area will be Observational Cosmology, focusing specifically on the motion of spiral galaxies to model the expansion rate of the universe as a continuation from a previous project. Linear regression is used quite often in astronomy, as it can handle large datasets quickly and produce visualizations.


**Objectives**
<br>

In this project, we will go deeper and find the distance of each spiral galaxy from Earth using two different methods to plot the linear relationship between recessional velocity and distance and to find the slope ( Hubble's constant). Although Hubble's constant has already been calculated, this project will show why there is still much debate and uncertainty. 

The two different methods we will use to analyze spiral galaxies are the Fixed Diameter method and the Fixed Magnitude method. We will then calculate the age of our universe for both constants and show the discrepancies compared to Hubble's constant estimated from the cosmic microwave background, 67km/s/Mpc. 

**Contributions**
<br>

The discrepancy between early universe Hubble's constant and late universe Hubble's constant is called Hubble's Tension. An inaccurate constant affects our ability to find the correct distances of galaxies and other celestial objects, as well as the age and behavior of the universe. For example, having a universe with a rate of expansion faster than when it was a baby leads us to think that there could be dark energy or some other thing that is causing it to expand faster. On the other hand, if the rate is lower in our late universe than early universe, we assume that the universe is slowing down.


**The Fixed Diameter Method**
<br>

The first method will come from an online science lab from the University of Washington, where they use 27 galaxy images from the University of Arizona and the equation below to calculate distance. This is assuming the true diameter of the galaxy is about the same as that of the M31 Andromeda Galaxy, 22 kpc.

$$d = s / a$$

* d is the distance to the galaxy 
* s is the true diameter of the galaxy 
* a is the apparent angular size

  
**The Fixed Magnitude Method** 
<br>

The second method will use the distance modulus and assume that the absolute magnitude, M = -20.5. This is because we do not have the absolute magnitude, but we do have the apparent magnitude. With over 1000 spiral galaxies in our data, hopefully, the small differences don't drastically change the results. 

$$d = 10^{\frac{m-M+5}{5}}$$

* d is the distance to the galaxy
* m is the apparent magnitude
* M is the absolute Magnitude

<br>

**Hubble's Law**
<br>

After we find the distance for each spiral galaxy using both methods, we will use linear regression to find Hubble's constant with the equation and model it.

$$ v = H_{0}D $$

* v is the recession velocity from Earth
* $H_{0}$ is the slope, Hubble's constant
* D is the distance from the Earth
  
<br>
