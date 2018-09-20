from omuse.units import units
from omuse.community.dales.interface import Dales

d=Dales()

print "parameters:"
print d.parameters
print 
print "data stores:", d.data_store_names()
print
print "evolve.."
d.evolve_model(60 | units.s)

print "..done!"
