"""Stream tubes originating from a probing grid of points.
Data is from CFD analysis of airflow in an office with
ventilation and a burning cigarette"""
from vedo import *
from off_furniture import furniture

fpath = download(dataurl + 'office.binary.vtk')
sgrid = loadStructuredGrid(fpath)

# Create a grid of points and use those as integration seeds
seeds = Grid(pos=[2,2,1], normal=[1,0,0], res=[2,3], c="gray")

# Now we will generate multiple streamlines in the data
slines = StreamLines(
    sgrid,
    seeds,
    initialStepSize=0.01,
    maxPropagation=15,
    tubes=dict(radius=0.005, mode=2, ratio=1),
)
slines.cmap("Reds").addScalarBar3D(c='white')
slines.scalarbar.x(5) # reposition scalarbar at x=5

show(slines, seeds, furniture(), __doc__, axes=1, bg='bb').close()
