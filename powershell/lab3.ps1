function getIP{

    (Get-NetIPAddress).IPv4Address | Select-String "192*"

}



$IP = getIP
$VERSION = $host.Version | Select-Object -ExpandProperty "Major"
$DATE = Get-Date -Format "dddd, MMMM dd, yyyy"

$BODY = "This machine's IP is $IP. User is $env:USERNAME. Hostname is $env:COMPUTERNAME. Powershell version $VERSION. Today's Date is $Date."

write-host($BODY)
$BODY | Out-File C:\Lab3.txt