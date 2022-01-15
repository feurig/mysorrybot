import bpy
import math
import mathutils

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
bpy.data.objects['BigHole'].select_set(state=True)
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.5, depth=5.0, location=(0,55.0, 1.25))
screwHole = bpy.context.selected_objects[0]
screwHole.name="ScrewHole"

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=4.0, depth=3.0, location=(0,55.0, 1.5))
stand = bpy.context.selected_objects[0]
stand.name="Stand"


bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = screwHole
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['ScrewHole'].select_set(state=True)
bpy.ops.object.delete()

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Stand'].select_set(state=False)
bpy.data.objects['NextLayer'].select_set(state=True)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = nextLayer
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['NextLayer'].select_set(state=True)
bpy.ops.object.delete()

bpy.data.objects['Stand'].select_set(state=True)
nextLayer = bpy.context.selected_objects[0]
nextLayer.name="NextLayer"

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.5, depth=5.0, location=(0,-55.0, 1.25))
screwHole = bpy.context.selected_objects[0]
screwHole.name="ScrewHole"

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=4.0, depth=3.0, location=(0,-55.0, 1.5))
stand = bpy.context.selected_objects[0]
stand.name="Stand"


bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = screwHole
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['ScrewHole'].select_set(state=True)
bpy.ops.object.delete()

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Stand'].select_set(state=False)
bpy.data.objects['NextLayer'].select_set(state=True)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = nextLayer
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['NextLayer'].select_set(state=True)
bpy.ops.object.delete()

bpy.data.objects['Stand'].select_set(state=True)
nextLayer = bpy.context.selected_objects[0]
nextLayer.name="NextLayer"


bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.5, depth=5.0, location=(55.0, 0.0, 1.25))
screwHole = bpy.context.selected_objects[0]
screwHole.name="ScrewHole"

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=4.0, depth=3.0, location=(55.0, 0.0, 1.5))
stand = bpy.context.selected_objects[0]
stand.name="Stand"


bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = screwHole
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['ScrewHole'].select_set(state=True)
bpy.ops.object.delete()

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Stand'].select_set(state=False)
bpy.data.objects['NextLayer'].select_set(state=True)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = nextLayer
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['NextLayer'].select_set(state=True)
bpy.ops.object.delete()

bpy.data.objects['Stand'].select_set(state=True)
nextLayer = bpy.context.selected_objects[0]
nextLayer.name="NextLayer"
#
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.5, depth=5.0, location=(-55.0, 0.0, 1.25))
screwHole = bpy.context.selected_objects[0]
screwHole.name="ScrewHole"

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=4.0, depth=3.0, location=(-55.0, 0.0, 1.5))
lastStand = bpy.context.selected_objects[0]
lastStand.name="LastStand"


bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = screwHole
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['ScrewHole'].select_set(state=True)
bpy.ops.object.delete()

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['LastStand'].select_set(state=False)
theStand=bpy.data.objects['LastStand']
nextLayer = bpy.data.objects['NextLayer']
nextLayer.select_set(state=True)
#bpy.context.active_object = nextLayer

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = nextLayer
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['NextLayer'].select_set(state=True)
bpy.ops.object.delete()
nextLayer = bpy.data.objects['LastStand']
#bpy.data.objects['Stand'].select_set(state=True)
nextLayer.name="NextLayer"
bpy.ops.object.select_all(action='DESELECT')
nextLayer.select_set(state=True)

bpy.context.scene.cursor.location = mathutils.Vector((0.0,0.0,0.0))
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
nextLayer.rotation_euler[2] = math.radians(-45.0)