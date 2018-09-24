Bootstrap: docker
From: centos:7

%setup
mkdir ${SINGULARITY_ROOTFS}/opt/splib

%files
#splib/*.py      /opt/splib/
#spmaster.py     /opt/
# oifs-input/     /opt/
#dales-input/    /opt/



%post
yum -y update
yum install -y epel-release
yum groupinstall -y "Development Tools"
yum install -y git mercurial gcc-gfortran cmake python-devel python-pip python-wheel wget openmpi-devel mpi4py-openmpi netcdf-devel netcdf-fortran-devel fftw-devel gmp-devel mpfr-devel gsl-devel atls atlas-devel blas-devel lapack-devel perl-Digest-MD5 perl-Time-Piece perl-IO-Compress
pip install --upgrade --ignore-installed pip setuptools
pip install moviepy f90nml numpy scipy matplotlib nose h5py docutils netCDF4 shapely psutil cython

pip install jupyter
mkdir /opt/notebooks


cd /opt

# official amuse
#git clone  --single-branch --depth=1 https://github.com/amusecode/amuse.git
#cd amuse
## NOTE: update PYTHONPATH if switching between the amuse versions 

# alternative: smaller development version of amuse
git clone --single-branch -b development --depth=1 https://github.com/ipelupessy/amuse-framework.git 
cd amuse-framework

export PYTHON=python
export MODULEPATH=/etc/modulefiles
eval `/usr/bin/modulecmd sh load mpi/openmpi-x86_64`
./configure FC=gfortran FCFLAGS="-I/usr/include -I/usr/lib64/gfortran/modules"
make framework
cd src

hg clone -r new_parameterapproach_dales  https://bitbucket.org/omuse/omuse
cd omuse

export DOWNLOAD_CODES=1


cd community/dales
# builds dales_worker, and stand-alone dales
# make  
# build only the dales_worker, for faster compilation
make dales_worker 



%environment
PYTHONPATH=/opt/amuse-framework/src/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/
#  LD_LIBRARY_PATH=/.singularity.d/libs:/usr/local/lib/
MODULEPATH=/etc/modulefiles

export PYTHONPATH  LD_LIBRARY_PATH MODULEPATH


%runscript
     echo "Starting notebook..."
     # echo "Open browser to localhost:8888"
     exec /usr/bin/jupyter notebook --notebook-dir=/opt/notebooks --port=8888 --no-browser


