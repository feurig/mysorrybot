import bpy

holeDepth=5
holeRadius=1.5

bpy.ops.mesh.primitive_cube_add()
gearHole = bpy.context.selected_objects[0]
gearHole.name="GearHole"
bpy.ops.transform.resize(value=(9, 14, holeDepth/2.0))
gearHole.location = (0,0,2)

bpy.ops.mesh.primitive_cube_add()
rightWheel = bpy.context.selected_objects[0]
rightWheel.name="RightWheel"
bpy.ops.transform.resize(value=(14, 4, holeDepth/2.0))
rightWheel.location = (0,49,2)

#bpy.ops.object.select_all(action='DESELECT')
#bpy.context.scene.objects.active = bpy.data.objects['GearHole']

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = gearHole   
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles = bpy.context.selected_objects[0]
newHoles.name="NewHoles"

# reselect the first cylinder and delete it (the only one worked!!!)
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_pattern(pattern = 'GearHole')
bpy.ops.object.delete()
bpy.ops.object.select_pattern(pattern = 'RightWheel')
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cube_add()
leftWheel = bpy.context.selected_objects[0]
leftWheel.name="LeftWheel"
bpy.ops.transform.resize(value=(14, 4, holeDepth/2.0))
leftWheel.location = (0,-49,2)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles   
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles1 = bpy.context.selected_objects[0]
newHoles1.name = "NewHoles1"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles1'].select_set(state=False)
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(4.5, 20.0, 2.0))
screw1 = bpy.context.selected_objects[0]
screw1.name="Screw1"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles1   
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles2 = bpy.context.selected_objects[0]
newHoles2.name = "NewHoles2"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles2'].select_set(state=False)
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(4.5, 38, 2.0))
screw2 = bpy.context.selected_objects[0]
screw2.name="Screw2"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles2   
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles3 = bpy.context.selected_objects[0]
newHoles3.name = "NewHoles3"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles3'].select_set(state=False)
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(4.5, -20.0, 2.0))
screw3 = bpy.context.selected_objects[0]
screw3.name="Screw3"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles3   
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles4 = bpy.context.selected_objects[0]
newHoles4.name = "NewHoles4"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles4'].select_set(state=False)
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(4.5, -38, 2.0))
screw4 = bpy.context.selected_objects[0]
screw4.name="Screw4"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles4
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles5 = bpy.context.selected_objects[0]
newHoles5.name = "NewHoles5"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles5'].select_set(state=False)
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(-37.5, 0, 2.0))
screw5 = bpy.context.selected_objects[0]
screw5.name="Screw5"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles5
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles6 = bpy.context.selected_objects[0]
newHoles6.name = "NewHoles6"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles6'].select_set(state=False)
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(-12, 22.5, 2.0))
screw6 = bpy.context.selected_objects[0]
screw6.name="Screw6"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles6
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
newHoles7 = bpy.context.selected_objects[0]
newHoles7.name = "NewHoles7"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['NewHoles7'].select_set(state=False)
bpy.ops.object.delete()


bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=holeRadius, depth=holeDepth, location=(-12, -22.5, 2.0))
screw7 = bpy.context.selected_objects[0]
screw7.name="Screw7"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = newHoles7
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
allTheHoles = bpy.context.selected_objects[0]
allTheHoles.name = "AllTheHoles"

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['AllTheHoles'].select_set(state=False)
bpy.ops.object.delete()

#bpy.data.objects['AllTheHoles'].select_set(state=False)
bpy.data.objects["AllTheHoles"].location.x += 12.0

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=62, depth=2.0, location=(0,0, 1.0))
baseplate = bpy.context.selected_objects[0]
baseplate.name="BasePlate"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = allTheHoles
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['BasePlate'].select_set(state=False)
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=59, depth=5.0, location=(0,0, 1.25))
bigHole = bpy.context.selected_objects[0]
bigHole.name="BigHole"

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=61, depth=3.0, location=(0,0, 1.5))
nextLayer = bpy.context.selected_objects[0]
nextLayer.name="NextLayer"

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bigHole
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_pattern(pattern = 'BigHole')
bpy.ops.object.delete()

#newHoles8 = bpy.context.selected_objects[0]
#newHoles8.name = ""


##bpy.ops.object.select_all(action='DESELECT')
#bpy.context.scene.objects.active = bpy.data.objects['Cylinder']
# bpy.ops.object.select_pattern(pattern = 'tube')
#motormount mount hole 11,22 11,-22, 35,0
