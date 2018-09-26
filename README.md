# dales-omuse-examples
The repo contains example scripts and data for using the OMUSE-wrapper of the Dutch Atmospheric Large Eddy Simulation (DALES)

(https://github.com/dalesteam/dales)[Official DALES GitHub page]



# Usage:

## Launch Jupyter server from container
```
# Build container
sudo singularity build dales.img Singularity 

# Create directories which the container needs at runtime
mkdir notebooks
mkdir run

# Launch the container - starts jupyter server inside
singularity run -B notebooks:/opt/notebooks/,run:/run/user/ ./dales.img 
```


## Using the Omuse Dales interface

```
# imports
from omuse.units import units
from omuse.community.dales.interface import Dales

# create a dales object
d=Dales()

# set parameters

d.itot = 32  # number of grid cells in x
d.jtot = 32  # number of grid cells in y


# time step the model
d.evolve_model(60 | units.s)

```

## Viewing documentation in Python

```
d = Dales()
```

```
#documentation of the interface fuctions:
help(d)

#documentation of the parameters:
help(d.parameters)
```



