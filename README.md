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


## Installing OMUSE and DALES without Singularity

First install dependencies:
  * netCDF (including Fortran bindings)
  * MPI
  * gfortran
  * gcc
  * cmake
  * make

The following sets up a virtual Python environment, and installs OMUSE in it.

```
hg clone https://bitbucket.org/omuse/omuse/
pip-2.7  install --user virtualenv
virtualenv sp_env
source sp_env/bin/activate

cd omuse/
pip install psutil f90nml numpy scipy  

pip install -e .

export DOWNLOAD_CODES=all
export SYST=gnu-fast

# python setup.py --help-commands
python setup.py develop_build
```



## Using the Omuse Dales interface

See the examples in notebooks/, in particular
    * `dales-interface-basic.ipynb` - basics of the dales interface
    * `interactive_nudge.ipynb`     - nudging Dales towards an interactively set profile


