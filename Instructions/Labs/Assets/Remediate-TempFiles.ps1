$tempPath = "$env:TEMP"

try {
    Get-ChildItem -Path $tempPath -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
        Remove-Item -Force -ErrorAction Stop
    Write-Output "Cleared old temp files"
    exit 0
} catch {
    Write-Error "Failed to clear temp files: $_"
    exit 1
}