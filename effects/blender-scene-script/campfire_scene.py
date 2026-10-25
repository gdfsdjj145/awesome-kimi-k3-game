"""
低多边形「林间营地」场景脚本（Blender 4.x）
用法：
  1) Blender → Scripting 工作区 → 打开本文件 → Run Script；或
  2) 命令行：blender --background --python campfire_scene.py -- --render out.png [--glb scene.glb]
生成：地面、帐篷、篝火（木柴+火焰+点光源）、松树、石头、原木凳、相机、太阳光与世界背景。
参考实现：由 Grok Bot 代 kajian du 编写，非 Kimi 生成。
"""
import bpy, bmesh, math, random, sys

random.seed(7)

# ---------- 工具函数 ----------
def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras):
        for b in list(block):
            block.remove(b)

def mat(name, rgb, emission=0.0, rough=0.9):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
    bsdf.inputs["Roughness"].default_value = rough
    if emission > 0:
        bsdf.inputs["Emission Color"].default_value = (*rgb, 1)
        bsdf.inputs["Emission Strength"].default_value = emission
    return m

def flat(obj, material):
    obj.data.materials.append(material)
    for p in obj.data.polygons:
        p.use_smooth = False
    return obj

def add(kind, loc, scale=(1, 1, 1), rot=(0, 0, 0), material=None, **kw):
    getattr(bpy.ops.mesh, "primitive_%s_add" % kind)(location=loc, rotation=rot, **kw)
    o = bpy.context.active_object
    o.scale = scale
    if material:
        flat(o, material)
    return o

def jitter(obj, amount):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    for v in bm.verts:
        v.co.z += random.uniform(-amount, amount)
    bm.to_mesh(obj.data)
    bm.free()

# ---------- 场景 ----------
clear_scene()
M = {
    "grass": mat("草地", (0.30, 0.55, 0.25)),
    "dirt": mat("泥土", (0.45, 0.32, 0.20)),
    "tent": mat("帐篷", (0.85, 0.40, 0.20)),
    "tent2": mat("帐篷暗面", (0.60, 0.25, 0.12)),
    "wood": mat("木头", (0.35, 0.20, 0.10)),
    "leaf": mat("松针", (0.12, 0.38, 0.22)),
    "leaf2": mat("松针亮", (0.20, 0.50, 0.28)),
    "rock": mat("石头", (0.50, 0.50, 0.52)),
    "fire": mat("火焰", (1.0, 0.45, 0.08), emission=8.0),
    "fire2": mat("火芯", (1.0, 0.85, 0.30), emission=12.0),
}

# 地面：16 边形圆盘 + 顶点抖动
ground = add("cylinder", (0, 0, -0.25), (12, 12, 0.25), material=M["grass"], vertices=16)
# 篝火周围泥土
add("cylinder", (0, 0, 0.01), (1.6, 1.6, 0.02), material=M["dirt"], vertices=10)

# 帐篷：四棱锥（cone vertices=4）
tent = add("cone", (-3.2, 2.2, 1.1), (1.8, 1.4, 1.1), rot=(0, 0, math.radians(30)), material=M["tent"], vertices=4, radius1=1, depth=2)
add("cone", (-2.55, 1.55, 0.55), (0.5, 0.35, 0.55), rot=(0, 0, math.radians(30)), material=M["tent2"], vertices=3, radius1=1, depth=2)

# 篝火：5 根交叉木柴 + 火焰
for i in range(5):
    a = i / 5 * math.tau
    add("cylinder", (math.cos(a) * 0.35, math.sin(a) * 0.35, 0.18), (0.08, 0.08, 0.55),
        rot=(math.radians(70), 0, a + math.pi / 2), material=M["wood"], vertices=6)
add("cone", (0, 0, 0.75), (0.45, 0.45, 0.75), material=M["fire"], vertices=6, radius1=1, depth=1)
add("cone", (0, 0, 0.6), (0.25, 0.25, 0.5), material=M["fire2"], vertices=5, radius1=1, depth=1)
# 篝火周围石头
for i in range(9):
    a = i / 9 * math.tau
    add("ico_sphere", (math.cos(a) * 0.95, math.sin(a) * 0.95, 0.08), (0.2, 0.18, 0.14), material=M["rock"], subdivisions=1)

# 原木凳
for (x, y, r) in [(2.2, 0.6, 15), (0.4, -2.3, 100)]:
    add("cylinder", (x, y, 0.25), (0.25, 0.25, 0.9), rot=(math.radians(90), 0, math.radians(r)), material=M["wood"], vertices=7)

# 松树（环形分布，确定性随机）
TREES = []
for i in range(22):
    a = i / 22 * math.tau + random.uniform(-0.12, 0.12)
    r = random.uniform(6.5, 10.5)
    TREES.append((math.cos(a) * r, math.sin(a) * r, random.uniform(0.8, 1.4)))
for (x, y, s) in TREES:
    add("cylinder", (x, y, 0.5 * s), (0.18 * s, 0.18 * s, 0.5 * s), material=M["wood"], vertices=6)
    add("cone", (x, y, 1.6 * s), (1.1 * s, 1.1 * s, 1.0 * s), material=M["leaf"], vertices=7, radius1=1, depth=2)
    add("cone", (x, y, 2.5 * s), (0.75 * s, 0.75 * s, 0.8 * s), material=M["leaf2"], vertices=7, radius1=1, depth=2)

# 散落石头
for i in range(8):
    a = random.uniform(0, math.tau); r = random.uniform(3, 6)
    s = random.uniform(0.25, 0.6)
    add("ico_sphere", (math.cos(a) * r, math.sin(a) * r, s * 0.3), (s, s * 0.8, s * 0.6), material=M["rock"], subdivisions=1)

# ---------- 灯光、相机、世界 ----------
bpy.ops.object.light_add(type="SUN", location=(10, -10, 15))
sun = bpy.context.active_object
sun.data.energy = 2.0
sun.data.color = (1.0, 0.85, 0.7)
sun.rotation_euler = (math.radians(50), 0, math.radians(35))

bpy.ops.object.light_add(type="POINT", location=(0, 0, 1.2))
fire_light = bpy.context.active_object
fire_light.data.energy = 300
fire_light.data.color = (1.0, 0.55, 0.2)
fire_light.data.shadow_soft_size = 0.4

bpy.ops.object.camera_add(location=(11, -11, 7.5))
cam = bpy.context.active_object
cam.data.lens = 35
# 让相机对准营地中心：用空物体 + Track To 约束
bpy.ops.object.empty_add(location=(0, 0, 0.8))
target = bpy.context.active_object
target.name = "相机目标"
track = cam.constraints.new("TRACK_TO")
track.target = target
track.track_axis = "TRACK_NEGATIVE_Z"
track.up_axis = "UP_Y"
bpy.context.scene.camera = cam

world = bpy.context.scene.world or bpy.data.worlds.new("World")
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes["Background"]
bg.inputs["Color"].default_value = (0.25, 0.30, 0.45, 1)  # 黄昏蓝紫
bg.inputs["Strength"].default_value = 0.6

# ---------- 渲染设置 ----------
scene = bpy.context.scene
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 32
scene.view_settings.view_transform = "AgX" if "AgX" in [i.identifier for i in scene.view_settings.bl_rna.properties["view_transform"].enum_items] else "Filmic"

# 命令行参数：-- --render 输出路径
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if "--render" in argv:
    scene.render.filepath = argv[argv.index("--render") + 1]
    bpy.ops.render.render(write_still=True)
    print("已渲染到", scene.render.filepath)
if "--glb" in argv:
    bpy.ops.export_scene.gltf(filepath=argv[argv.index("--glb") + 1], export_format="GLB",
                              export_lights=False, export_cameras=False, export_apply=True)
    print("已导出 glTF：", argv[argv.index("--glb") + 1])
print("营地场景生成完成：对象数 =", len(bpy.data.objects))
