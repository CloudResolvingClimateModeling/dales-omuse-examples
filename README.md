# dales-omuse-examples
The repo contains example scripts and data for using the OMUSE-wrapper of the Dutch Atmospheric Large Eddy Simulation (DALES)

(https://github.com/dalesteam/dales)[Official DALES GitHub page]



# Usage:

## Launch Jupyter server from container
```
# Build container
sudo singularity build dales.img Singularity 

# Create directories which the container needs at runtime
mkdir run

# Launch the container - starts jupyter server inside
singularity run -B notebooks:/opt/notebooks/,run:/run/user/ ./dales.img 
```


## Using the Omuse Dales interface

See the examples in notebooks/, in particular
    * `dales-interface-basic.ipynb` - basics of the dales interface
    * `interactive_nudge.ipynb`     - nudging Dales towards an interactively set profile

