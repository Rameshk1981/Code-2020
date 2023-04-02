# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(10.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    3.89486694335938, -3.79907417297363), value=5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    13.9566116333008, 8.97228622436523), value=15, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='CylindricalSpec', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['CylindricalSpec'].BaseSolidRevolve(angle=360.0, 
    flipRevolveDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['CylindricalSpec'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['CylindricalSpec'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[0], MIDDLE), point2=
    mdb.models['Model-1'].parts['CylindricalSpec'].vertices[0], point3=
    mdb.models['Model-1'].parts['CylindricalSpec'].vertices[1])
mdb.models['Model-1'].parts['CylindricalSpec'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['CylindricalSpec'].cells.getSequenceFromMask((
    '[#3 ]', ), ), point1=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[5], MIDDLE), point2=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[6], MIDDLE), point3=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[7], MIDDLE))
mdb.models['Model-1'].parts['CylindricalSpec'].Set(edges=
    mdb.models['Model-1'].parts['CylindricalSpec'].edges.getSequenceFromMask((
    '[#1 ]', ), ), name='centreline')
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((107370.0, 0.3), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=None)
mdb.models['Model-1'].parts['CylindricalSpec'].Set(cells=
    mdb.models['Model-1'].parts['CylindricalSpec'].cells.getSequenceFromMask((
    '[#f ]', ), ), name='Set-2')
mdb.models['Model-1'].parts['CylindricalSpec'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['CylindricalSpec'].sets['Set-2'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name=
    'CylindricalSpec-1', part=mdb.models['Model-1'].parts['CylindricalSpec'])
mdb.models['Model-1'].parts['CylindricalSpec'].seedEdgeByNumber(constraint=
    FINER, edges=
    mdb.models['Model-1'].parts['CylindricalSpec'].edges.getSequenceFromMask((
    '[#8a080 ]', ), ), number=6)
mdb.models['Model-1'].parts['CylindricalSpec'].seedEdgeByNumber(constraint=
    FINER, edges=
    mdb.models['Model-1'].parts['CylindricalSpec'].edges.getSequenceFromMask((
    '[#40124 ]', ), ), number=12)
mdb.models['Model-1'].parts['CylindricalSpec'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['CylindricalSpec-1'].faces.getSequenceFromMask(
    ('[#8488 ]', ), ), name='Set-1')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Base fixed', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=SET, u2=SET, 
    u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Centreline', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['CylindricalSpec-1'].sets['centreline']
    , u1=SET, u2=UNSET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].rootAssembly.Surface(name='Surf-1', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['CylindricalSpec-1'].faces.getSequenceFromMask(
    ('[#3050 ]', ), ))
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, field='', magnitude=90.0, name='Pressure90', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['Surf-1'])
# Save by r on 2022_01_04-20.03.01; build 2017 2016_09_28-03.24.59 126836
