import bpy
import os


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

        bpy.ops.wm.read_factory_settings(use_empty=True)

        bpy.ops.import_anim.bvh(filepath=bvh_filepath, update_scene_fps=True, update_scene_duration=True)

        # Ensure correct scene frame range
        assert len(bpy.data.actions) == 1
        frame_range = bpy.data.actions[0].frame_range
        bpy.context.scene.frame_start = int(frame_range[0])
        bpy.context.scene.frame_end = int(frame_range[1])

        # Add some mesh data so UE allows import
        bpy.data.objects[filename].name = "animation"
        bpy.ops.mesh.primitive_plane_add()
        bpy.data.objects["Plane"].name = filename
        bpy.data.objects["animation"].select_set(True)
        bpy.ops.object.parent_set()  # Parent the "animation" object to cube

        # Export
        bpy.ops.export_scene.fbx(filepath=fbx_filepath, check_existing=False)

        raise Exception('Need to figure out how to fix UE incorrect frame rate issue')
