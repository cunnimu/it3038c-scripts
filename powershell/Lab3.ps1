function getIP{

    (Get-NetIPAddress).IPv4Address | Select-String "192*"

}



$IP = getIP
$VERSION = $host.Version | Select-Object -ExpandProperty "Major"
$USER = $env:USERNAME
$HOSTNAME = $env:COMPUTERNAME
$DATE = Get-Date -Format "dddd, MMMM dd, yyyy"

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. Powershell version $VERSION. Today's Date is $DATE."

write-host($BODY)
$BODY | Out-File C:\Lab3.txt
