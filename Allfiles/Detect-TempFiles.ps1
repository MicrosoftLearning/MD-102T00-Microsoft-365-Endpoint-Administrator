$tempPath = "$env:TEMP"
$oldFiles = Get-ChildItem -Path $tempPath -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) }

if ($oldFiles.Count -gt 0) {
    Write-Output "Found $($oldFiles.Count) old temp files"
    exit 1
}

Write-Output "No old temp files found"
exit 0