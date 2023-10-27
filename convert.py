import bpy
import os


BLENDER_DIR = "C:\\Program Files\\Blender Foundation\\Blender 3.6"
BVH_DIR = "C:\\Users\\gf321\\Research\\lafan1\\lafan1\\lafan1"
FBX_DIR = ".\\output"


if __name__ == "__main__":
    assert os.path.isdir(BVH_DIR)
    if not os.path.isdir(FBX_DIR):
        os.mkdir(FBX_DIR)

    filenames = map(
        lambda f: os.path.splitext(f)[0],
        filter(
            lambda f: os.path.splitext(f)[1] == '.bvh',
            os.listdir(BVH_DIR)
        )
    )

    for filename in filenames:
        bvh_filepath = os.path.join(BVH_DIR, filename + '.bvh')
        fbx_filepath = os.path.join(FBX_DIR, filename + '.fbx')
        bpy.ops.import_anim.bvh(filepath=bvh_filepath, update_scene_fps=True, update_scene_duration=True)
        bpy.ops.export_scene.fbx(filepath=fbx_filepath)
        break
