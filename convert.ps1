$env:Path += "C:\Program Files\Blender Foundation\Blender 3.6;"
Start-Process -FilePath "blender.exe" -ArgumentList "empty.blend --background --python convert.py"