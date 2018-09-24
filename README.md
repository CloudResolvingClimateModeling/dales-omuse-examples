# dales-omuse-examples
The repo contains example scripts and data for using the OMUSE-wrapper of the Dutch Atmospheric Large Eddy Simulation (DALES)

(https://github.com/dalesteam/dales)[Official DALES GitHub page]



# Usage:
```
# Build container
sudo singularity build Singularity dales.img

# Create directories which the container needs at runtime
mkdir notebooks
mkdir run

# Launch the container - starts jupyter server inside
singularity run -B notebooks:/opt/notebooks/,run:/run/user/ ./dales.img 
```

